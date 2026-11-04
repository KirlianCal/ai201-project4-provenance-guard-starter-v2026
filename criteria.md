# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Own writing is rarely flagged

Of 12 pieces I wrote myself, at most 2 get a combined score of 0.58 or higher, in each of three runs. I will save the 12 pieces as files in the repo before scoring any of them.

**Why this target:** One flagged piece out of 12 is an accident. Two is the most I would accept in the real world, because a wrongly flagged writer is accused of something they didn't do. I want my own honest writing to land on the cusp of "unsure" (0.42 to 0.58), not past it.

---

## 2. AI and human text score far apart

I will use 6 clearly-AI samples (output from one saved prompt, files committed) and 6 clearly-human samples (history or other nonfiction book excerpts, 1,800 characters or less, book and section recorded). All 6 human samples score 0.38 or lower, and at least 5 of the 6 AI samples score 0.75 or higher. The same samples land on the same side of those lines in each of three runs.

**Why this target:** Clear examples of each kind should be able to meet the bar, and "unsure" covers everything in between. The human bar is stricter (all 6) because wrongly calling a person's work AI costs more than missing some AI text. The AI samples are Claude-written, so this only covers that style of AI text.

---

## 3. All three labels are reachable

I can name one submission that produces each label: high-confidence human (0.00 to 0.38), unsure (0.38 to 0.75), and high-confidence AI (0.75 to 1.00). Each of the three submissions produces the same label in all three runs. I will record the three filenames in the README.

**Why this target:** My human label needs a score of 0.38 or lower, and `config.py` warns that the combined score can't go that low until the style signal actually varies. A label nobody can reach is a gap in my thresholds, and I want to find it by testing, not after a real writer is stuck with the wrong one.

---

## 4. Appeals always change status and always get recorded

I send 8 appeals, each with a real `content_id`. Every one returns 200 with status `under_review`, and `GET /log` shows the appeal beside the original decision, which stays unchanged. An appeal with an unknown `content_id` returns 404 `unknown_content_id`, one with a missing `content_id` returns 400 `missing_content_id`, and one with empty `reasoning` returns 400 `missing_reasoning`. Appealing the same item twice returns 200 both times and logs both appeals.

**Why this target:** The appeal is the only thing between a wrong accusation and nothing. If it fails silently, a falsely accused writer has no recourse and no one would know.

---

## 5. Bad input gets a specific error, never a crash

For each bad-input case in design.md Section 4 (both endpoints), I send one request. Each returns the exact status and `error` name in the table, with a `message` that names the field that is wrong and what to send instead, and each appears in the audit log. Exactly 1,800 characters is accepted and 1,801 is rejected. I also send inputs my table doesn't list: JSON `null`, a list as the body, `text` sent as a number, and punctuation-only text. None returns a 500.

**Why this target:** A crash gives the site and the writer nothing, while a wrong label can at least be appealed. Writing the table myself means those cases will pass, so I am also testing inputs I didn't plan for.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
