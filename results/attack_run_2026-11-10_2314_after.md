# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 23:14
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `6ded155b-1e5f-4861-8365-34a6d1696718` | unsure | 0.390 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `21418f40-bfc0-43a7-9205-0effdc0d74e3` | unsure | 0.418 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8f5c036d-7b4e-40ca-bcb0-2b5e0c210c19` | unsure | 0.545 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c025ead0-7ef2-460f-af1c-858a547183b2` | unsure | 0.634 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `eacb971d-14a7-436c-91b7-695d5a7fccbb` | human | 0.253 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2c9e67d2-e510-4f05-8446-af155d141042` | unsure | 0.415 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `86b95959-e48d-4ca3-96d9-ece8351895e5` | unsure | 0.502 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `db3dc16d-7599-40f4-869c-ee7b8f5d038b` | unsure | 0.394 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `beb2ad33-d654-4e74-9fef-86cf028d6d0a` | unsure | 0.566 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `8b4dde8c-a086-4c17-9500-93fad09ccc8e` | unsure | 0.740 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c47471a0-0691-44e6-ae9c-eeddde60621a` | unsure | 0.554 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `3e99f64d-6ed3-4d05-9fe8-1ebda06246a1` | unsure | 0.717 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `942c8c63-9917-4a6a-988d-5fb721c4bcff` | unsure | 0.729 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `0de8d735-7fe2-478d-9574-d08455533c1c` | unsure | 0.709 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `e971a1e4-0ecc-4d82-b088-e66bcadc8187` | unsure | 0.746 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `59ff47d6-7883-42c2-9b3d-3492b25cca43` | unsure | 0.686 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `eba71a8f-b0d9-4651-8e6e-7900ac30277c` | unsure | 0.626 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `15cfb52b-6f43-48ea-b06d-7cfdff4c018b` | unsure | 0.380 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `78e09006-5a81-4f60-969e-79b36c75d584` | human | 0.372 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2350e281-871f-475c-bb09-06279982bf30` | human | 0.192 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `7bc64bee-be38-4b05-910f-5163a9a06540` | unsure | 0.543 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `962f4b94-a47e-4900-b89d-996260164465` | unsure | 0.449 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `ed7c39ad-ff68-4875-b39c-64157416b1ef` | unsure | 0.475 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `cc22c250-d913-441d-81b2-bcfcb4e29ca3` | unsure | 0.521 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `97834c86-c05c-4adc-ac71-c104df038609` | unsure | 0.390 |  |
| MF04 | malformed | text is only punctuation | 200 | `ded413ed-1b45-4c4e-9d6e-020baa74393c` | unsure | 0.390 |  |
| MF05 | malformed | text is a very long single word | 413 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 200 | `135d113e-5aee-4e38-a1db-58e7dff11052` | ai | 0.858 |  |
| MF07 | malformed | text is right-to-left script | 200 | `92e04474-89a8-4a16-9d98-82c5d9c74fe1` | ai | 0.804 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f61f107b-a25f-47a1-a9e5-2a0491d1bcae` | unsure | 0.390 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1728f967-cfbc-44c6-8c1e-c7c1b354c7de` | unsure | 0.390 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d0ba812f-53d9-4aed-b57d-80fd2841427a` | unsure | 0.390 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1886d4ed-8027-4317-8b85-a70a8dcca23a` | unsure | 0.390 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3ce4e2a7-d91e-4e5f-96b5-75c18fca4e9d` | unsure | 0.390 |  |
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
  "content_id": "6ded155b-1e5f-4861-8365-34a6d1696718",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.39,
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
  "content_id": "21418f40-bfc0-43a7-9205-0effdc0d74e3",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4181,
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
  "content_id": "8f5c036d-7b4e-40ca-bcb0-2b5e0c210c19",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5446,
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
  "content_id": "c025ead0-7ef2-460f-af1c-858a547183b2",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.634,
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
  "content_id": "eacb971d-14a7-436c-91b7-695d5a7fccbb",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2528,
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
  "content_id": "2c9e67d2-e510-4f05-8446-af155d141042",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4152,
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
  "content_id": "86b95959-e48d-4ca3-96d9-ece8351895e5",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.502,
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
  "content_id": "db3dc16d-7599-40f4-869c-ee7b8f5d038b",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.394,
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
  "content_id": "beb2ad33-d654-4e74-9fef-86cf028d6d0a",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5655,
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
  "content_id": "8b4dde8c-a086-4c17-9500-93fad09ccc8e",
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
  "content_id": "c47471a0-0691-44e6-ae9c-eeddde60621a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5545,
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
  "content_id": "3e99f64d-6ed3-4d05-9fe8-1ebda06246a1",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7169,
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
  "content_id": "942c8c63-9917-4a6a-988d-5fb721c4bcff",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7287,
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
  "content_id": "0de8d735-7fe2-478d-9574-d08455533c1c",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7087,
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
  "content_id": "e971a1e4-0ecc-4d82-b088-e66bcadc8187",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7457,
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
  "content_id": "59ff47d6-7883-42c2-9b3d-3492b25cca43",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6862,
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
  "content_id": "eba71a8f-b0d9-4651-8e6e-7900ac30277c",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6264,
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
  "content_id": "15cfb52b-6f43-48ea-b06d-7cfdff4c018b",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3802,
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
  "content_id": "78e09006-5a81-4f60-969e-79b36c75d584",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3724,
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
  "content_id": "2350e281-871f-475c-bb09-06279982bf30",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1923,
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
  "content_id": "7bc64bee-be38-4b05-910f-5163a9a06540",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.543,
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
  "content_id": "962f4b94-a47e-4900-b89d-996260164465",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4489,
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
  "content_id": "ed7c39ad-ff68-4875-b39c-64157416b1ef",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4755,
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
  "content_id": "cc22c250-d913-441d-81b2-bcfcb4e29ca3",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.521,
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
  "content_id": "97834c86-c05c-4adc-ac71-c104df038609",
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
  "content_id": "ded413ed-1b45-4c4e-9d6e-020baa74393c",
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
  "content_id": "135d113e-5aee-4e38-a1db-58e7dff11052",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8581,
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
  "content_id": "92e04474-89a8-4a16-9d98-82c5d9c74fe1",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8038,
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
  "content_id": "f61f107b-a25f-47a1-a9e5-2a0491d1bcae",
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
  "content_id": "1728f967-cfbc-44c6-8c1e-c7c1b354c7de",
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
  "content_id": "d0ba812f-53d9-4aed-b57d-80fd2841427a",
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
  "content_id": "1886d4ed-8027-4317-8b85-a70a8dcca23a",
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
  "content_id": "3ce4e2a7-d91e-4e5f-96b5-75c18fca4e9d",
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
