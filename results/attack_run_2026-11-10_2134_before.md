# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 21:34
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f8e0e8f3-d6d2-4246-97ce-d2a33285a745` | unsure | 0.422 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `0e59808d-8e02-46fd-965e-b6d9a0105128` | unsure | 0.390 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `a4c214b9-ad3d-4c45-8a65-21568695395c` | unsure | 0.514 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `eab78078-4bd6-46e2-bd2f-358ebfd492c6` | unsure | 0.640 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `1d30f7b6-082b-48c4-a0eb-fc12889b0d7e` | human | 0.236 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `09e9cb9e-a56b-4ed2-a8a1-6bdb158d7dfe` | unsure | 0.390 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `6dcdabdf-c3b6-4188-96d2-ae6c19bd8ab7` | unsure | 0.481 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a980695a-3d99-4e72-97a1-d9990d437052` | unsure | 0.431 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `5b8ff013-2156-465a-a5b9-be8cadcb70f0` | unsure | 0.531 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `af6ff1b1-e76a-4805-8ed1-cc8c8a8c87c8` | unsure | 0.740 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `80166f2c-cb70-4f05-ba20-72c7a4f63b04` | unsure | 0.539 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `165a3198-c139-4784-8c8f-1de7a738ae5c` | unsure | 0.712 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c86582a9-5f24-4f07-b50d-ae2250607fb1` | unsure | 0.710 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `bcc5993d-7e59-4965-bafd-116cfdebd8d5` | unsure | 0.678 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `3d47bc7c-6b07-45af-937d-9a57f554477d` | unsure | 0.732 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `97a91835-efec-4cc3-b25c-f8d8e00393e9` | unsure | 0.637 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `eb8c4eb0-9b82-4c86-8eea-98aa3129cf31` | unsure | 0.562 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `e7f6870f-b4a9-4d51-8d31-4a0f345c13fb` | unsure | 0.395 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b3e562b3-9375-4a9e-a869-dfd139dbc06f` | human | 0.350 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `f2f6a5cb-b211-4040-845c-b7143c646fc0` | human | 0.189 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `4b44a6a7-e398-4cc8-b9f8-bcf9ac4bc846` | unsure | 0.530 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `441c33d5-a204-469a-8a31-99d441250e1c` | unsure | 0.436 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c0bedd52-9fc7-4bff-91e4-1bdb29890f19` | unsure | 0.434 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `2f6552f2-0fb8-4d44-9c41-c043f47077a7` | unsure | 0.512 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `e687c385-8c6f-41d0-9629-d0d294d7b109` | unsure | 0.390 |  |
| MF04 | malformed | text is only punctuation | 200 | `891a86bc-8151-4228-86f2-fdc36e51b2e6` | unsure | 0.390 |  |
| MF05 | malformed | text is a very long single word | 413 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 200 | `7e82f615-1691-4fba-842d-715590c624c9` | ai | 0.824 |  |
| MF07 | malformed | text is right-to-left script | 200 | `7ac8365e-c511-4c6b-88fc-86522853fe2f` | ai | 0.778 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `63db0615-c35b-4d46-9de3-7bb00e8a6231` | unsure | 0.390 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7052a286-49f9-447e-a33e-a98e2292e862` | unsure | 0.390 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cd862f49-e0f6-4158-aac9-3b06604e95b2` | unsure | 0.390 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5ce685c9-7253-4ca8-ad63-872ea26ce12c` | unsure | 0.390 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f79cf794-1e76-4820-a690-f297681fe431` | unsure | 0.390 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "f8e0e8f3-d6d2-4246-97ce-d2a33285a745",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4219,
  "model_score": 0.1635,
  "style_score": 0.6804,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "0e59808d-8e02-46fd-965e-b6d9a0105128",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.5943,
  "style_score": 0.1537,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "a4c214b9-ad3d-4c45-8a65-21568695395c",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5142,
  "model_score": 0.6662,
  "style_score": 0.3623,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "eab78078-4bd6-46e2-bd2f-358ebfd492c6",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6396,
  "model_score": 0.6114,
  "style_score": 0.6678,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "1d30f7b6-082b-48c4-a0eb-fc12889b0d7e",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2357,
  "model_score": 0.3212,
  "style_score": 0.1503,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "09e9cb9e-a56b-4ed2-a8a1-6bdb158d7dfe",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.5727,
  "style_score": 0.179,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "6dcdabdf-c3b6-4188-96d2-ae6c19bd8ab7",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4809,
  "model_score": 0.5862,
  "style_score": 0.3756,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "a980695a-3d99-4e72-97a1-d9990d437052",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4312,
  "model_score": 0.2452,
  "style_score": 0.6172,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "5b8ff013-2156-465a-a5b9-be8cadcb70f0",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5308,
  "model_score": 0.7042,
  "style_score": 0.3574,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "af6ff1b1-e76a-4805-8ed1-cc8c8a8c87c8",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.74,
  "model_score": 0.9792,
  "style_score": 0.6061,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "80166f2c-cb70-4f05-ba20-72c7a4f63b04",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5388,
  "model_score": 0.6175,
  "style_score": 0.4601,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "165a3198-c139-4784-8c8f-1de7a738ae5c",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7115,
  "model_score": 0.7387,
  "style_score": 0.6842,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c86582a9-5f24-4f07-b50d-ae2250607fb1",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7097,
  "model_score": 0.8051,
  "style_score": 0.6142,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "bcc5993d-7e59-4965-bafd-116cfdebd8d5",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6777,
  "model_score": 0.8329,
  "style_score": 0.5225,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "3d47bc7c-6b07-45af-937d-9a57f554477d",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.732,
  "model_score": 0.8005,
  "style_score": 0.6636,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "97a91835-efec-4cc3-b25c-f8d8e00393e9",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6373,
  "model_score": 0.8814,
  "style_score": 0.3933,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "eb8c4eb0-9b82-4c86-8eea-98aa3129cf31",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5625,
  "model_score": 0.8816,
  "style_score": 0.2435,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "e7f6870f-b4a9-4d51-8d31-4a0f345c13fb",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3947,
  "model_score": 0.3223,
  "style_score": 0.467,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b3e562b3-9375-4a9e-a869-dfd139dbc06f",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3499,
  "model_score": 0.4625,
  "style_score": 0.2373,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "f2f6a5cb-b211-4040-845c-b7143c646fc0",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1893,
  "model_score": 0.2044,
  "style_score": 0.1741,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "4b44a6a7-e398-4cc8-b9f8-bcf9ac4bc846",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5302,
  "model_score": 0.5943,
  "style_score": 0.466,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "441c33d5-a204-469a-8a31-99d441250e1c",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4362,
  "model_score": 0.4998,
  "style_score": 0.3726,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c0bedd52-9fc7-4bff-91e4-1bdb29890f19",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4344,
  "model_score": 0.6401,
  "style_score": 0.2286,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "2f6552f2-0fb8-4d44-9c41-c043f47077a7",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5117,
  "model_score": 0.5583,
  "style_score": 0.4651,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "e687c385-8c6f-41d0-9629-d0d294d7b109",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.0,
  "style_score": 0.55,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "891a86bc-8151-4228-86f2-fdc36e51b2e6",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.0112,
  "style_score": 0.65,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "7e82f615-1691-4fba-842d-715590c624c9",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8235,
  "model_score": 0.9969,
  "style_score": 0.65,
  "label": "We think this may have been written with an AI tool. This is only an estimate, not proof. If you wrote it yourself, you may appeal and your work will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "7ac8365e-c511-4c6b-88fc-86522853fe2f",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7782,
  "model_score": 0.9064,
  "style_score": 0.65,
  "label": "We think this may have been written with an AI tool. This is only an estimate, not proof. If you wrote it yourself, you may appeal and your work will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "63db0615-c35b-4d46-9de3-7bb00e8a6231",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "7052a286-49f9-447e-a33e-a98e2292e862",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "cd862f49-e0f6-4158-aac9-3b06604e95b2",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "5ce685c9-7253-4ca8-ad63-872ea26ce12c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "f79cf794-1e76-4820-a690-f297681fe431",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.39,
  "model_score": 0.0287,
  "style_score": 0.55,
  "label": "We can't tell whether this was written by a person or by an AI tool. This is not an accusation, it is only a guess.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
