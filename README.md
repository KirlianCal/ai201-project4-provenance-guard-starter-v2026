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

**Are all three labels reachable?** Yes, but only with unusual text. Human: one ornate sentence ("The labyrinthine bureaucracy...") scored 0.3692 (model 0.3884, style 0.35), only 0.011 under the 0.38 line. AI: a contrived repetitive text ("The cat sat on the mat. The dog sat on the mat...") scored 0.9762 (model 0.9524, style 1.0). Unsure: my ordinary sentence ("We walked to the park...") scored 0.599. None of my realistic paragraph-length human or AI texts reached either confident label, so in practice almost everything lands in unsure.


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

**Moment 1: building the style signal**

- *What I asked for:* Help building `stylometry.py`: which measures to use and how to combine them into one 0-1 score.
- *What came back:* Three measures (sentence-length spread, type-token ratio, punctuation density) with starting weights and scale cutoffs. When I ran it on four fresh paragraphs, it scored my plain human paragraph as more AI-like (0.481) than my clearly AI one (0.389), the opposite of what I expected.
- *What I changed:* I printed each measure separately. Type-token ratio pointed the wrong way (AI 0.830, human 0.690 and 0.740), and the punctuation regex missed the spaced hyphens used as dashes in my Congress paragraph. I fixed the regex and moved the weights to 0.70 for sentence spread, 0.10 for vocabulary and 0.20 for punctuation. Style scores then separated the texts (human 0.397 and 0.280, AI 0.529 and 0.712).

**Moment 2: the character limit**

- *What I asked for:* Whether a 2,000-character limit would cover fringe cases like rare words or other languages, since the detector reads tokens, not characters.
- *What came back:* A character limit can't guarantee that, because unusual text uses more tokens per character. The 1,800 figure was rough arithmetic from "400 tokens is about 300 words", not a measurement.
- *What I changed:* I set the limit to 1,800 characters, tied it to the detector's 400-token cap, and adjusted the design claim to a softer, "most accepted submissions are judged on all of their text."

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 125 per day

**Why those numbers and not others:** A real writer creating a draft, tweaking it and resubmitting might try three or five times in a minute, so 5 per minute lets that through while a script hits the wall after five requests. The daily cap matters because a patient script could stay under the per-minute limit but still send thousands of requests a day to map my thresholds. At 125 per day, an honest writer would never get close, but a thousand-variation probe from one identity would take about eight days. The cost is that a writer who retries many times quickly would get a 429 and have to wait a minute.

**What a caller counts as:** Each `creator_id` is counted separately, and a request with no usable `creator_id` falls back to the caller's address. This stops one identity from flooding the service. It does not stop a script that sends a different `creator_id` on every request, which is how each row of the attack set is built. Counting by address would catch that, but it would also clump together everyone on shared network, so I choose per-creator.
The attack run showed the fallback in action: requests with no usable creator_id shared one address bucket, and the sixth and seventh of them (RQ10, RQ11) were rejected as rate limited before my route saw them.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
10 of 15 were rate limited.
```

---

## Attack Run — Before

I marked an attack BROKE when AI text was not labeled AI, including when it landed in unsure, because the attack succeeded if my detector failed to flag it. I marked a false-positive attack BROKE only if it was labeled AI. 56 attacks: 15 BROKE, 41 HELD. Full output: `results/attack_run_2026-11-10_2134_before.md`.

| ID | What it was going for | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|
| EV01 | signal two: typos raise word variety | 200 | unsure | 0.422 | BROKE |
| EV02 | signal two: broken-up sentences raise length spread | 200 | unsure | 0.390 | BROKE |
| EV03 | signal two: a pasted quotation changes the shape | 200 | unsure | 0.514 | BROKE |
| EV04 | signal one: unusual words raise perplexity | 200 | unsure | 0.640 | BROKE |
| EV05 | both signals: heavy human editing pass | 200 | human | 0.236 | BROKE |
| EV06 | signal two: one very long sentence and one very short | 200 | unsure | 0.390 | BROKE |
| EV07 | signal two: padding with punctuation | 200 | unsure | 0.481 | BROKE |
| EV08 | signal one: text below the token window | 200 | unsure | 0.431 | BROKE |
| EV09 | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.531 | BROKE |
| EV10 | signal two: repeated stanza structure | 200 | unsure | 0.740 | BROKE |
| FP01 | plain, clear human writing | 200 | unsure | 0.539 | HELD |
| FP02 | human writing in a formal register | 200 | unsure | 0.712 | HELD |
| FP03 | non-native English speaker writing carefully | 200 | unsure | 0.710 | HELD |
| FP04 | student essay written to a rubric | 200 | unsure | 0.678 | HELD |
| FP05 | technical documentation written by a person | 200 | unsure | 0.732 | HELD |
| FP06 | a person imitating a formal template | 200 | unsure | 0.637 | HELD |
| FP07 | human writing that repeats a phrase deliberately | 200 | unsure | 0.562 | HELD |
| FP08 | very short genuine human submission | 200 | unsure | 0.395 | HELD |
| PI01 | instruction to ignore the check | 200 | human | 0.350 | BROKE |
| PI02 | instruction disguised as a system message | 200 | human | 0.189 | BROKE |
| PI03 | instruction wrapped in the writer's voice | 200 | unsure | 0.530 | BROKE |
| PI04 | attempt to make the label text hostile | 200 | unsure | 0.436 | HELD |
| PI05 | attempt to inject into the audit log | 200 | unsure | 0.434 | HELD |
| PI06 | instruction plus real human text | 200 | unsure | 0.512 | HELD |
| MF01 | text is only whitespace | 400 | — | — | HELD |
| MF02 | text is a single character | 400 | — | — | HELD |
| MF03 | text is control characters | 200 | unsure | 0.390 | HELD |
| MF04 | text is only punctuation | 200 | unsure | 0.390 | HELD |
| MF05 | text is a very long single word | 413 | — | — | HELD |
| MF06 | text is emoji only | 200 | ai | 0.824 | BROKE |
| MF07 | text is right-to-left script | 200 | ai | 0.778 | BROKE |
| MF08 | text is 60,000 characters | 413 | — | — | HELD |
| RQ01 | no text field at all | 400 | — | — | HELD |
| RQ02 | no creator_id | 400 | — | — | HELD |
| RQ03 | text is a number | 400 | — | — | HELD |
| RQ04 | text is a list | 400 | — | — | HELD |
| RQ05 | text is null | 400 | — | — | HELD |
| RQ06 | creator_id is an object | 400 | — | — | HELD |
| RQ07 | body is a JSON array, not an object | 400 | — | — | HELD |
| RQ08 | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | body is empty | 400 | — | — | HELD |
| RQ10 | body is form-encoded, not JSON | 429 | — | — | HELD (rejected by the limiter, never reached my route) |
| RQ11 | body is JSON claiming to be plain text | 429 | — | — | HELD (rejected by the limiter, never reached my route) |
| RQ12 | deeply nested JSON | 400 | — | — | HELD |
| FL01_01 to FL01_05 | 20 rapid submissions from one creator | 200 | unsure | 0.390 | HELD (under the limit) |
| FL01_06 to FL01_12 | same | 429 | — | — | HELD (limiter fired at the sixth request) |

**Ten audit log entries from the run**

```json
[
  {
    "combined_score": 0.7782,
    "content_id": "7ac8365e-c511-4c6b-88fc-86522853fe2f",
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "label": "We think this may have been written with an AI tool. This is only an estimate, not proof. If you wrote it yourself, you may appeal and your work will be marked for review.",
    "model_score": 0.9064,
    "status": "decided",
    "style_score": 0.65,
    "timestamp": "2026-11-11T02:34:53+00:00"
  },
  {
    "combined_score": 0.8235,
    "content_id": "7e82f615-1691-4fba-842d-715590c624c9",
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "label": "We think this may have been written with an AI tool. This is only an estimate, not proof. If you wrote it yourself, you may appeal and your work will be marked for review.",
    "model_score": 0.9969,
    "status": "decided",
    "style_score": 0.65,
    "timestamp": "2026-11-11T02:34:53+00:00"
  },
  {
    "combined_score": 0.1893,
    "content_id": "f2f6a5cb-b211-4040-845c-b7143c646fc0",
    "creator_id": "attacker_PI02",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.2044,
    "status": "decided",
    "style_score": 0.1741,
    "timestamp": "2026-11-11T02:34:52+00:00"
  },
  {
    "combined_score": 0.3499,
    "content_id": "b3e562b3-9375-4a9e-a869-dfd139dbc06f",
    "creator_id": "attacker_PI01",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.4625,
    "status": "decided",
    "style_score": 0.2373,
    "timestamp": "2026-11-11T02:34:52+00:00"
  },
  {
    "combined_score": 0.2357,
    "content_id": "1d30f7b6-082b-48c4-a0eb-fc12889b0d7e",
    "creator_id": "attacker_EV05",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.3212,
    "status": "decided",
    "style_score": 0.1503,
    "timestamp": "2026-11-11T02:34:50+00:00"
  },
  {
    "combined_score": 0.74,
    "content_id": "af6ff1b1-e76a-4805-8ed1-cc8c8a8c87c8",
    "creator_id": "attacker_EV10",
    "guess": "unsure",
    "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
    "model_score": 0.9792,
    "status": "decided",
    "style_score": 0.6061,
    "timestamp": "2026-11-11T02:34:51+00:00"
  },
  {
    "combined_score": 0.732,
    "content_id": "3d47bc7c-6b07-45af-937d-9a57f554477d",
    "creator_id": "attacker_FP05",
    "guess": "unsure",
    "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
    "model_score": 0.8005,
    "status": "decided",
    "style_score": 0.6636,
    "timestamp": "2026-11-11T02:34:51+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "5 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-11T02:34:54+00:00"
  },
  {
    "creator_id": "attacker_MF01",
    "event": "rejected",
    "reason": "missing_text",
    "status": "rejected",
    "timestamp": "2026-11-11T02:34:52+00:00"
  },
  {
    "creator_id": "unknown",
    "event": "rejected",
    "limit": "5 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-11T02:34:53+00:00"
  }
]

```

**The single worst outcome** — The one I'd least want to explain to a writer
whose work got caught: MF07. A writer submitted one ordinary sentence in Arabic. My system returned `guess: ai` with a combined score of 0.7782 (model_score 0.9064, style_score 0.65) and told them: "We think this may have been written with an AI tool. This is only an estimate, not proof. If you wrote it yourself, you may appeal and your work will be marked for review." They did nothing wrong, and their only remedy is to appeal, which they would have to know to do. It is worse than the evasion misses because those let AI text through, while this accuses a real person.

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
