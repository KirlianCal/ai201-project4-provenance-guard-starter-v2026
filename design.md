# Milestone 1: Design Notes



## 1. The path of a submission

1. **Request arrives at `POST /submit`** with JSON `{"text": "...", "creator_id": "..."}`. Handler checks the input before any model runs, and a request that fails a check is rejected with an error and written to the audit log:
    - Body isn't a JSON object: reject/400 error.
    - `text` missing, empty, or only whitespace: reject/400 error.
    - `text` too short to score (`detector.py` raises `ValueError` under 3 tokens): reject/400 error.
    - `creator_id` missing or empty: reject/400 error.
    - `text` longer than 2,000 characters: reject/413 error. The limit is tied to the detector: `config.DETECTOR_MAX_TOKENS` is 400 tokens (~300 words/~1,800 characters) and `detector.py` truncates anything longer. Rejecting means every accepted submission is judged on all of its text.

2. **A `content_id` is created** (`uuid` is already imported in `app.py`). It adds the identifier that `/appeal` needs to find this item later.

3. **Signal one: `detector.model_signal(text)`.** A local GPT-2 model reads the text and returns a 0-1 score (higher = more likely AI). It adds a judgment on how predictable the text is.

4. **Signal two: `stylometry.style_signal(text)`.** It measures the text as text (for example sentence-length spread, word variety, punctuation) and returns a 0-1 score (higher = more likely AI). It adds a judgment on the shape of the text.

5. **`scoring.combine_signals(model_score, style_score)`** merges both into one 0-1 score using the rule and weights in `config.py`. The rule itself is **TO DECIDE** in Milestone 4.

6. **`scoring.score_to_label(score)`** returns `(guess, label_text)`: `"ai"`, `"human"` or `"unsure"`, plus the full sentence a reader sees. It adds plain English. The label wording is **TO DECIDE** in Milestone 5.

7. **`audit.log_decision(...)` writes one entry to `logs/audit.jsonl`, then the response is returned.** The entry holds timestamp, content_id, creator_id, guess, model_score, style_score, combined_score, label and status (`decided`). The response carries content_id, guess, confidence, label, model_score and style_score.

## 2. The two signals

### Signal one: GPT-2 predictability (`detector.py`)

- **Measures:** how predictable the text is to a language model. Text a model finds easy to predict tends to be text a model wrote.
- **Why it might differ:** AI text tends toward likely words, so it is easier to predict.
- **What it can't see:** authorship. Predictability isn't authorship: plain writing in common words and short sentences (second-language writers, younger writers, anyone writing plainly on purpose) scores as machine-like, while dense, ornate prose often reads as human. `detector.py` also truncates text at 400 tokens, so anything past that point is never scored.
- **Test runs of detector.py:**

    | Text | Perplexity | model_signal |
    |---|---|---|
    | "I like my dog. He is big. He runs fast. We go to the park." | 20.0 | 0.7848 |
    | "The labyrinthine bureaucracy, ostensibly designed to expedite grievances, instead metastasized into an inscrutable apparatus." | 59.8 | 0.3884 |
    | "Neatness was crucial since we would be judged on it. When a wrench clattered out of someone's bag onto the pavement, I felt a pang in my chest." (my own writing) | 54.7 | 0.4225 |

  The third row is my own writing, so it is a verified human sample. The first two are short test sentences, not verified samples of human or AI writing. Together they show the direction of the blind spot, not a measured error rate. My own sample landed in the unsure band (0.4225), not the human band, so signal one alone would not confidently clear a real writer.

### Signal two: stylometry (`stylometry.py`, not built yet)

- **Measures:** two or three of sentence-length spread, ratio of unique words to total words, and punctuation density. Which ones I use is **TO DECIDE** (Milestone 4).
- **Why it might differ:** hypothesis, to be tested in Milestone 4. AI text may keep sentence lengths and punctuation more uniform, while human writing varies more from sentence to sentence.
- **What it can't see:** meaning. It cannot read: typos, broken-up sentences or a pasted quotation change the shape without changing the substance, and that is cheap to do on purpose.

## 3. Tracing the false positive

A second-language student writes an essay in plain, common-word sentences and submits their own work. Following them through the service as it stands today:

- **Score:** the plain test sentence above gave signal one 0.7848, and a plain writer like this student would likely land in the same range. That is an expectation from one test sentence, not a measurement of a real student, so it needs checking in Milestone 4 with a plainly written human paragraph. Signal two is not built, so the combined score is **TO DECIDE / measure in Milestone 4**.
- **Current threshold:** `config.py` has `AI_THRESHOLD = 0.65`. The plain test sentence's signal one score (0.7848) is already above that line.
- **What the label said:** **TO DECIDE** in Milestone 5. It has to read as a likelihood, not an accusation, because the person may have written every word.
- **What they can do:** `POST /appeal` with `content_id` and `reasoning`. `audit.log_appeal` sets the status to `under_review` and records it beside the original decision. No automatic re-check, so this is the only thing between a wrong accusation and nothing.
- **What it decides for the thresholds:** widening the unsure band means fewer wrong accusations and more AI text getting through. The thresholds decide who pays for that trade, and the numbers are **TO DECIDE**.

## 4. Endpoint contracts

### `POST /submit`

- **In:** `{"text": "...", "creator_id": "..."}`
- **Out, at minimum:** `content_id`, `guess` (`"ai"`, `"human"` or `"unsure"`), `confidence` (0.0 to 1.0), `label` (the reader-facing sentence), `model_score` (0.0 to 1.0), `style_score` (0.0 to 1.0)
- **Bad input:** every rejection returns a JSON error with a stable `error` name and a plain-English `message`, and is written to the audit log with `audit.log_rejection`.

  | Case | Status | `error` |
  |---|---|---|
  | Body isn't a JSON object | 400 | `invalid_json` |
  | `text` missing, empty or whitespace | 400 | `missing_text` |
  | `text` too short to score (under 3 tokens) | 400 | `text_too_short` |
  | `creator_id` missing or empty | 400 | `missing_creator_id` |
  | `text` over 2,000 characters | 413 | `text_too_long` |

### `POST /appeal`

- **In:** `{"content_id": "...", "reasoning": "..."}`
- **Out (200):** `{"content_id": "...", "status": "under_review", "message": "..."}`. The `message` confirms the appeal was received and makes no promise about a review timeline, since no automatic re-check happens.
- **Bad input:** every rejection returns a JSON error with a stable `error` name and a plain-English `message`.

  | Case | Status | `error` |
  |---|---|---|
  | Body isn't a JSON object | 400 | `invalid_json` |
  | `content_id` missing or empty | 400 | `missing_content_id` |
  | `reasoning` missing or empty | 400 | `missing_reasoning` |
  | `content_id` not in the log (checked with `audit.entries_for(id)`) | 404 | `unknown_content_id` |

- **On success:** the `creator_id` is read from the original log entry (found with `audit.entries_for(content_id)`), then `audit.log_appeal(content_id, creator_id, reasoning)` writes the appeal beside the original decision and sets the status to `under_review`.