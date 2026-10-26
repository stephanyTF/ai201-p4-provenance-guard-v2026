# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-10-25 19:53
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `63cb5920-69b2-4f22-bf27-0891190d832b` | human | 0.164 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `2a4fe66b-961d-4b32-918b-43a2186746de` | ai | 0.594 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `18eeedfe-6a10-4b15-ab51-873e37e70fba` | ai | 0.666 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `fca10000-0543-4cee-a7e1-d1d2e2f33bc9` | ai | 0.611 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `63e64331-31f6-4141-a39b-816eba7f0f15` | unsure | 0.321 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d53f1b03-9d66-4367-b3da-fcc703a63dde` | ai | 0.573 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c3f6f980-6cc1-4c1f-85aa-f1b429fb42d7` | ai | 0.586 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `1ad6ac0d-3fcd-41fa-ab63-8ed2de4bd6de` | human | 0.245 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `edf2d780-345b-43ff-9f4e-0e778eda924b` | ai | 0.704 |  |
| EV10 | evasion | signal two: repeated stanza structure | 400 | `—` | — | — |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3320613f-947b-4702-8873-3a36f30e7ec3` | ai | 0.618 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `fe750d11-13eb-40d5-846d-b1e374b9c141` | ai | 0.739 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `86bd643e-c1b0-4e62-9e33-1a7bcf3de29a` | ai | 0.805 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `7a689522-0d5d-489c-b84d-4b36bccfd241` | ai | 0.833 |  |
| FP05 | false_positive | technical documentation written by a person | 400 | `—` | — | — |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `10c4cffb-294c-4dac-9e1d-667761118533` | ai | 0.881 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 400 | `—` | — | — |  |
| FP08 | false_positive | very short genuine human submission | 200 | `f7a07aa9-f13b-4786-97d6-b62daf2d09ae` | unsure | 0.322 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `837a578f-50a8-468b-8251-22a17322bd21` | ai | 0.463 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `42948c71-865d-4961-8176-8ebaeb59b9c1` | human | 0.204 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f6a08548-9f13-4471-b942-a1b0aba4bbf8` | ai | 0.594 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4079115a-6ea9-44a3-b4ca-e5cc4f53a582` | ai | 0.500 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `56311efa-6dc7-40f9-8b28-dda12dae8008` | ai | 0.640 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6163805e-9ccd-42f3-bcc5-6aee28780519` | ai | 0.558 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `8fdc3681-4ff7-4b44-b9d7-545919b6804e` | human | 0.000 |  |
| MF04 | malformed | text is only punctuation | 200 | `4ce8cfab-7ca0-4d82-b869-7a2eb5d3f8ac` | human | 0.011 |  |
| MF05 | malformed | text is a very long single word | 200 | `dcbf7de9-2e03-4d76-b268-ccf59cd3bc9c` | ai | 0.998 |  |
| MF06 | malformed | text is emoji only | 200 | `c14fc435-4270-4198-a988-a755074e736c` | ai | 0.997 |  |
| MF07 | malformed | text is right-to-left script | 200 | `9ab17db3-28a4-49c3-b6ee-8781e22bef80` | ai | 0.906 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `354f9cfc-9193-4d3e-9328-0846a93d1451` | human | 0.029 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `49ad9430-552c-493d-8f05-696e3bbc545f` | human | 0.029 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5f9fb85c-d2bd-494e-a596-b0646768b10c` | human | 0.029 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1de798d1-00a8-4f77-9948-5b8b1a03088c` | human | 0.029 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `35c9b933-e43d-488f-992c-c3b60d8c9705` | human | 0.029 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b327b139-e951-4bf9-bb7f-2034d295a580` | human | 0.029 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6ce8434b-c6f4-4fa9-8043-f5d8fb83c178` | human | 0.029 |  |
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
| `malformed` | 20 | 2 | 18 |
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
  "content_id": "63cb5920-69b2-4f22-bf27-0891190d832b",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.1635,
  "model_score": 0.1635,
  "style_score": 0.367,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "2a4fe66b-961d-4b32-918b-43a2186746de",
  "creator_id": "attacker_EV02",
  "guess": "ai",
  "confidence": 0.5943,
  "model_score": 0.5943,
  "style_score": 0.154,
  "label": "Most likely written by an AI.",
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
  "content_id": "18eeedfe-6a10-4b15-ab51-873e37e70fba",
  "creator_id": "attacker_EV03",
  "guess": "ai",
  "confidence": 0.6662,
  "model_score": 0.6662,
  "style_score": 0.286,
  "label": "Most likely written by an AI.",
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
  "content_id": "fca10000-0543-4cee-a7e1-d1d2e2f33bc9",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6114,
  "model_score": 0.6114,
  "style_score": 0.363,
  "label": "Most likely written by an AI.",
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
  "content_id": "63e64331-31f6-4141-a39b-816eba7f0f15",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3212,
  "model_score": 0.3212,
  "style_score": 0.249,
  "label": "Difficult to tell whether this was written by a person or an AI. It could be either.",
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
  "content_id": "d53f1b03-9d66-4367-b3da-fcc703a63dde",
  "creator_id": "attacker_EV06",
  "guess": "ai",
  "confidence": 0.5727,
  "model_score": 0.5727,
  "style_score": 0.132,
  "label": "Most likely written by an AI.",
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
  "content_id": "c3f6f980-6cc1-4c1f-85aa-f1b429fb42d7",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.5862,
  "model_score": 0.5862,
  "style_score": 0.295,
  "label": "Most likely written by an AI.",
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
  "content_id": "1ad6ac0d-3fcd-41fa-ab63-8ed2de4bd6de",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.2452,
  "model_score": 0.2452,
  "style_score": 0.285,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "edf2d780-345b-43ff-9f4e-0e778eda924b",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.7042,
  "model_score": 0.7042,
  "style_score": 0.276,
  "label": "Most likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV10",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "3320613f-947b-4702-8873-3a36f30e7ec3",
  "creator_id": "attacker_FP01",
  "guess": "ai",
  "confidence": 0.6175,
  "model_score": 0.6175,
  "style_score": 0.344,
  "label": "Most likely written by an AI.",
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
  "content_id": "fe750d11-13eb-40d5-846d-b1e374b9c141",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7387,
  "model_score": 0.7387,
  "style_score": 0.403,
  "label": "Most likely written by an AI.",
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
  "content_id": "86bd643e-c1b0-4e62-9e33-1a7bcf3de29a",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.8051,
  "model_score": 0.8051,
  "style_score": 0.382,
  "label": "Most likely written by an AI.",
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
  "content_id": "7a689522-0d5d-489c-b84d-4b36bccfd241",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.8329,
  "model_score": 0.8329,
  "style_score": 0.326,
  "label": "Most likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "10c4cffb-294c-4dac-9e1d-667761118533",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.8814,
  "model_score": 0.8814,
  "style_score": 0.309,
  "label": "Most likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "f7a07aa9-f13b-4786-97d6-b62daf2d09ae",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3223,
  "model_score": 0.3223,
  "style_score": 0.254,
  "label": "Difficult to tell whether this was written by a person or an AI. It could be either.",
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
  "content_id": "837a578f-50a8-468b-8251-22a17322bd21",
  "creator_id": "attacker_PI01",
  "guess": "ai",
  "confidence": 0.4625,
  "model_score": 0.4625,
  "style_score": 0.181,
  "label": "Most likely written by an AI.",
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
  "content_id": "42948c71-865d-4961-8176-8ebaeb59b9c1",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2044,
  "model_score": 0.2044,
  "style_score": 0.174,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "f6a08548-9f13-4471-b942-a1b0aba4bbf8",
  "creator_id": "attacker_PI03",
  "guess": "ai",
  "confidence": 0.5943,
  "model_score": 0.5943,
  "style_score": 0.299,
  "label": "Most likely written by an AI.",
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
  "content_id": "4079115a-6ea9-44a3-b4ca-e5cc4f53a582",
  "creator_id": "attacker_PI04",
  "guess": "ai",
  "confidence": 0.4998,
  "model_score": 0.4998,
  "style_score": 0.307,
  "label": "Most likely written by an AI.",
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
  "content_id": "56311efa-6dc7-40f9-8b28-dda12dae8008",
  "creator_id": "attacker_PI05",
  "guess": "ai",
  "confidence": 0.6401,
  "model_score": 0.6401,
  "style_score": 0.239,
  "label": "Most likely written by an AI.",
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
  "content_id": "6163805e-9ccd-42f3-bcc5-6aee28780519",
  "creator_id": "attacker_PI06",
  "guess": "ai",
  "confidence": 0.5583,
  "model_score": 0.5583,
  "style_score": 0.346,
  "label": "Most likely written by an AI.",
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
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "8fdc3681-4ff7-4b44-b9d7-545919b6804e",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0,
  "style_score": 0.198,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "4ce8cfab-7ca0-4d82-b869-7a2eb5d3f8ac",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.0112,
  "model_score": 0.0112,
  "style_score": 0.737,
  "label": "Most likely written without the use of an AI.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "dcbf7de9-2e03-4d76-b268-ccf59cd3bc9c",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9976,
  "model_score": 0.9976,
  "style_score": 0.167,
  "label": "Most likely written by an AI.",
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
  "content_id": "c14fc435-4270-4198-a988-a755074e736c",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9969,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "Most likely written by an AI.",
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
  "content_id": "9ab17db3-28a4-49c3-b6ee-8781e22bef80",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9064,
  "model_score": 0.9064,
  "style_score": 0.551,
  "label": "Most likely written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
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
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
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

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
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
  "content_id": "354f9cfc-9193-4d3e-9328-0846a93d1451",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.215,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "49ad9430-552c-493d-8f05-696e3bbc545f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.215,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "5f9fb85c-d2bd-494e-a596-b0646768b10c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.215,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "1de798d1-00a8-4f77-9948-5b8b1a03088c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.215,
  "label": "Most likely written without the use of an AI.",
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
  "content_id": "35c9b933-e43d-488f-992c-c3b60d8c9705",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.215,
  "label": "Most likely written without the use of an AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "b327b139-e951-4bf9-bb7f-2034d295a580",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.215,
  "label": "Most likely written without the use of an AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "6ce8434b-c6f4-4fa9-8043-f5d8fb83c178",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.0287,
  "model_score": 0.0287,
  "style_score": 0.215,
  "label": "Most likely written without the use of an AI.",
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
