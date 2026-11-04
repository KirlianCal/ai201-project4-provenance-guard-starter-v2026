# Milestone 1: Design Notes



## 1. The path of a submission

1. **Request arrives at `POST /submit`** with JSON `{"text": "...", "creator_id": "..."}`. Handler checks the input before any model runs, and a request that fails a check is rejected with an error and written to the audit log:
    - Body isn't a JSON object: reject/400 error.
    - `text` missing, empty, or only whitespace: reject/400 error.
    - `text` too short to score (`detector.py` raises `ValueError` under 3 tokens): reject/400 error.
    - `creator_id` missing or empty: reject/400 error.
    - `text` longer than 1,800 characters: reject/413 error. The limit is tied to the detector: `config.DETECTOR_MAX_TOKENS` is 400 tokens (~300 words/~1,800 characters) and `detector.py` truncates anything longer. Rejecting means most accepted submission are  judged on all of its text.

2. **A `content_id` is created** (`uuid` is already imported in `app.py`). It adds the identifier that `/appeal` needs to find this item later.

3. **Signal one: `detector.model_signal(text)`.** A local GPT-2 model reads the text and returns a 0-1 score (higher = more likely AI). It adds a judgment on how predictable the text is.

4. **Signal two: `stylometry.style_signal(text)`.** It measures the text as text (sentence-length spread, word variety, punctuation) and returns a 0-1 score (higher = more likely AI). It adds a judgment on the shape of the text.

5. **`scoring.combine_signals(model_score, style_score)`** returns a weighted average (0.5 each). If the two signals differ by more than 0.35, the result is clamped into the unsure band, because two methods disagreeing is uncertainty. Only when both signals agree can a score reach the human label (0.38 or lower) or the AI label (0.75 or higher). Numbers live in `config.py`.

6. **`scoring.score_to_label(score)`** returns `(guess, label_text)`: `"ai"`, `"human"` or `"unsure"`, plus the full sentence a reader sees. It adds plain English. The three labels are written out in the README under Label Variants.

7. **`audit.log_decision(...)` writes one entry to `logs/audit.jsonl`, then the response is returned.** The entry holds timestamp, content_id, creator_id, guess, model_score, style_score, combined_score, label and status (`decided`). The response carries content_id, guess, confidence, label, model_score and style_score.

## 2. The two signals

### Signal one: GPT-2 predictability (`detector.py`)

- **Measures:** how predictable the text is to a language model. Text a model finds easy to predict tends to be text a model wrote.
- **Why it might differ:** AI text tends toward likely words, so it is easier to predict.
- **What it can't see:** authorship. Predictability isn't authorship: plain writing in common words and short sentences (second-language writers, younger writers, anyone writing plainly on purpose) scores as machine-like, while dense, ornate prose often reads as human. `detector.py` also truncates text at 400 tokens, so anything past that point is never scored. On four fresh paragraph-length texts the perplexity was 19.8 to 23.2 for all of them, so it scored 0.74 to 0.79 whatever the author; on long text it did not discriminate.
- **Test runs of detector.py:**

    | Text | Perplexity | model_signal |
    |---|---|---|
    | "I like my dog. He is big. He runs fast. We go to the park." | 20.0 | 0.7848 |
    | "The labyrinthine bureaucracy, ostensibly designed to expedite grievances, instead metastasized into an inscrutable apparatus." | 59.8 | 0.3884 |
    | "Neatness was crucial since we would be judged on it. When a wrench clattered out of someone's bag onto the pavement, I felt a pang in my chest." (my own writing) | 54.7 | 0.4225 |

  The third row is my own writing, so it is a verified human sample. The first two are short test sentences, not verified samples of human or AI writing. Together they show the direction of the blind spot, not a measured error rate. My own sample landed in the unsure band (0.4225), not the human band, so signal one alone would not confidently clear a real writer.

### Signal two: stylometry (`stylometry.py`)

- **Measures:** sentence-length spread (stdev / mean of sentence lengths), type-token ratio over the first 100 words, and punctuation density (commas, semicolons, colons, dashes, brackets, quotes and spaced hyphens per word). Combined with weights 0.70, 0.10 and 0.20 in `config.py`.
- **Why it might differ:** AI text tends toward even sentence lengths and steady vocabulary and punctuation, while human writing is lumpier. Tested on four fresh paragraphs: sentence spread separated them (human 0.434 and 0.531, AI 0.263 and 0.141), type-token ratio pointed the wrong way (clearly AI 0.830, human 0.690 and 0.740), and punctuation did not separate them.
- **What it can't see:** meaning. It cannot read: typos, broken-up sentences or a pasted quotation change the shape without changing the substance, and that is cheap to do on purpose.

## 3. Tracing the false positive

A second-language student writes an essay in plain, common-word sentences and submits their own work. Following them through the service as it stands today:

- **Score:** a plain writer would likely get a high signal one score, as the plain dog sentence did (0.7848). On four fresh paragraphs signal one scored 0.74 to 0.79 whatever the author, so it adds little. Signal two separated human from AI better, and the plain human paragraph scored 0.397 there. The combined score was 0.592, inside the unsure band, because the two signals disagreed by 0.39 and the rule clamps disagreement toward unsure.
- **Current thresholds:** `config.py` has `HUMAN_THRESHOLD = 0.38` and `AI_THRESHOLD = 0.75`. A plain writer needs both signals to agree before they could be labeled AI.
- **What the label said:** "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess." It reads as ...
- **What they can do:** `POST /appeal` with `content_id` and `reasoning`. `audit.log_appeal` sets the status to `under_review` and records it beside the original decision. No automatic re-check, so this is the only thing between a wrong accusation and nothing.
- **What it decides for the thresholds:** widening the unsure band means fewer wrong accusations and more AI text getting through. The thresholds decide who pays for that trade. Mine are 0.38 and 0.75, which keep a wide unsure band: fewer wrong accusations, and more AI text left unlabeled.

## 4. Endpoint contracts

### `POST /submit`

- **In:** `{"text": "...", "creator_id": "..."}`
- **Out, at minimum:** `content_id`, `guess` (`"ai"`, `"human"` or `"unsure"`), `confidence` (0.0 to 1.0), `label` (the reader-facing sentence), `model_score` (0.0 to 1.0), `style_score` (0.0 to 1.0)
- **Bad input:** every rejection returns a JSON error with a stable `error` name and a `message` that says what was wrong and what to send instead, and is written to the audit log with `audit.log_rejection`.

    | Case | Status | `error` | `message` |
    |---|---|---|---|
    | Body isn't a JSON object | 400 | `invalid_json` | The request body must be a JSON object with `text` and `creator_id`. |
    | `text` missing, empty or whitespace | 400 | `missing_text` | No text was provided. Send the writing to check in the `text` field. |
    | `text` too short to score (under 3 tokens) | 400 | `text_too_short` | The text is too short to check. Send at least a few sentences. |
    | `creator_id` missing or empty | 400 | `missing_creator_id` | No `creator_id` was provided. Send the writer's id in the `creator_id` field. |
    | `text` over 1,800 characters | 413 | `text_too_long` | The text is over the 1,800-character limit. Send a shorter piece. |
    | detector model not available | 503 | `detector_unavailable` | The detector model isn't available. Run `python detector.py` once to download it. |

### `POST /appeal`

- **In:** `{"content_id": "...", "reasoning": "..."}`
- **Out (200):** `{"content_id": "...", "status": "under_review", "message": "..."}`. The `message` confirms the appeal was received and makes no promise about a review timeline, since no automatic re-check happens.
- **Repeat appeals:** an item can be appealed more than once. Each appeal returns 200 and is logged, and the status stays `under_review`.
- **Bad input:** every rejection returns a JSON error with a stable `error` name and a `message` that says what was wrong and what to send instead.

  | Case | Status | `error` | `message` |
  |---|---|---|---|
  | Body isn't a JSON object | 400 | `invalid_json` | The request body must be a JSON object with `content_id` and `reasoning`. |
  | `content_id` missing or empty | 400 | `missing_content_id` | No `content_id` was provided. Send the id returned when the text was submitted. |
  | `reasoning` missing or empty | 400 | `missing_reasoning` | No reasoning was provided. Explain in the `reasoning` field why the result is wrong. |
  | `content_id` not in the log (checked with `audit.entries_for(id)`) | 404 | `unknown_content_id` | No submission was found with that `content_id`. Check the id and try again. |

- **On success:** the `creator_id` is read from the original log entry (found with `audit.entries_for(content_id)`), then `audit.log_appeal(content_id, creator_id, reasoning)` writes the appeal beside the original decision and sets the status to `under_review`.