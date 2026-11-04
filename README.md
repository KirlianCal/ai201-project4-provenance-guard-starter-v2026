# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

A submission goes through seven steps:

1. **`POST /submit` receives the request** and checks the input before any model runs. A bad request (not a JSON object, missing or empty `text`, `text` too short to score, missing `creator_id`, or text over 1,800 characters) gets a specific error and is written to the audit log.
2. **A `content_id` is created** (a UUID) so the audit log and `/appeal` can find the item later.
3. **Signal one (`detector.py`)** runs the text through a local GPT-2 model and returns a 0-1 score for how predictable it is (higher = more likely AI).
4. **Signal two (`stylometry.py`)** measures the shape of the text and returns a 0-1 score (higher = more likely AI).
5. **`scoring.py::combine_signals`** merges the two scores into one.
6. **`scoring.py::score_to_label`** turns that score into a guess (`ai`, `human` or `unsure`) and the sentence a reader sees.
7. **`audit.py` writes the decision to `logs/audit.jsonl`**, and the response returns the `content_id`, guess, confidence, label, and both signal scores.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a small language model (GPT-2), turned into a 0-1 score.

**Why that might differ between human and AI writing:** AI text tends toward likely words, so a model finds it easier to predict. Human writing tends to be more surprising.

**What it can't see:** Authorship. Predictability isn't authorship, so plain writing in common words and short sentences scores as machine-like, while dense, ornate prose often reads as human. It also scores only the first 400 tokens, so anything after that is never seen. My test runs: plain dog sentences 0.7848, an ornate sentence 0.3884, my own writing 0.4225, a plain casual sentence 0.648. On four fresh paragraph-length texts its perplexity was 19.8 to 23.2 for all of them, so it did not discriminate.

### Signal two — the style signal

**What it measures:** The shape of the text without reading it: sentence-length spread (stdev divided by mean), type-token ratio over the first 100 words, and punctuation density (commas, semicolons, colons, dashes, brackets, quotes and spaced hyphens per word). Weights 0.70, 0.10 and 0.20.

**Why that might differ between human and AI writing:** AI text tends toward even sentence lengths and steady vocabulary and punctuation, while human writing is lumpier. On four fresh paragraphs only sentence spread behaved that way (human 0.434 and 0.531, AI 0.263 and 0.141). Type-token ratio pointed the wrong way and punctuation did not separate them, so I weighted spread most. Four texts is a small sample, so I treat this as a hypothesis.

**What it can't see:** Meaning. Typos, split sentences or a pasted quotation change the shape without changing the substance, and that is cheap to do on purpose.

### The combining rule

**The rule:** A weighted average of the two signals. If they differ by more than 0.35, the result is clamped into the unsure band, because two methods disagreeing is uncertainty and a wrong accusation costs more than a missed detection.

**The numbers:** Weights 0.5 and 0.5, disagreement gap 0.35, thresholds 0.38 (human) and 0.75 (AI), all in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** My dense scientific paragraph scored 0.743 on signal one (reads as AI) and 0.280 on signal two (reads as human), a gap of 0.46. The rule treated that as disagreement and kept the result in the unsure band (combined 0.511). The plain average was already inside the band there, so the clamp did not change the number. It does for more extreme splits: model 0.99 with style 0.55 averages 0.77 (an AI label), and the rule returns 0.74.

**Result against the milestone check:** clearly AI and clearly human text did not score noticeably apart. On four fresh paragraphs the combined scores ran 0.511 to 0.746 and all landed in the unsure band, because signal one scored every paragraph 0.74 to 0.79. Signal two separated them better, but not enough to move any text into a confident label.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.38 | We think this was probably written by a person. |
| unsure | 0.38 – 0.75 | We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess. |
| high-confidence AI | 0.75 – 1.00 | We think this may have been written with an AI tool. This is only an estimate, not proof. If you wrote it yourself, you may appeal and your work will be marked for review. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
     I did not want the person to think they were being accused of something. In my tests, plain writing by real people often landed in this band, so many of the people reading this label will have written every word themselves. I named the word "accusation" and called the result "only a guess" so the label says plainly that it is not a finding about them.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{"text": "We walked to the park after school and talked about the game.", "creator_id": "me"}'
```

```json
{
  "confidence": 0.599,
  "content_id": "5c61b2c3-46ef-43ba-8101-f8b827df6553",
  "guess": "unsure",
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "model_score": 0.648,
  "style_score": 0.55
}
```

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->


**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{"content_id": "5c61b2c3-46ef-43ba-8101-f8b827df6553", "reasoning": "I wrote this myself after a school trip."}'
```

```json
{
  "content_id": "5c61b2c3-46ef-43ba-8101-f8b827df6553",
  "message": "We've recorded your appeal and marked this item as under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.599,
      "content_id": "5c61b2c3-46ef-43ba-8101-f8b827df6553",
      "creator_id": "me",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
      "model_score": 0.648,
      "status": "decided",
      "style_score": 0.55,
      "timestamp": "2026-11-04T06:39:59+00:00"
    },
    {
      "content_id": "5c61b2c3-46ef-43ba-8101-f8b827df6553",
      "creator_id": "me",
      "event": "appeal",
      "reasoning": "I wrote this myself after a school trip.",
      "status": "under_review",
      "timestamp": "2026-11-04T06:42:25+00:00"
    }
  ]
}
```

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
