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
1. A text enters by client request where its text and creator_id is extracted from sommething like `curl -X POST /submit with a JSON body of {"text": "...", "creator_id": "..."}.`
2. The first signal is in detector.py which tokenizes it, truncated to the max tokens, and rejects text that is too short.
3. Model_signal computes GPT-2 perplexity and makes it fit on a 0–1 score, where high means AI.
4. Stylometry is the 2nd signal, measuring sentence-length spread, type-token ratio, and punctuation density.
5. Style_signal normalizes, flips, and combines those into a 0–1 score, where high means AI.
6. Combine_signals merges the two signals into one score.
7. The score is mapped to the label the reader sees


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** Measures how well each word fits its context, using GPT-2's trained language based on predictability of text

**Why that might differ between human and AI writing:** 
     For humans, their writing tend to be less predictable (like odd or informal word choices). 
     For AI, its writing can be repetitive thus more predictable than humans as it tends to iterate the same words.

**What it can't see:** 
     The signal has 3 blindspots:
          1. Someone writing in a second language as they may stick to using words they're familiar with or write more formally depending on their background or culture or polite caution when writing in a new language
          2. A younger writer. They may repeat or use basic vocabulary as they're still learning
          3. Anyone writing plainly on purpose for a research paper or other strictly formal event. 


### Signal two — the style signal

**What it measures:**  Stylometry analyze the text's shape (without context unlike detector) soley based on stats like sentence-length spread, type-token ratio, and punctuation density

**Why that might differ between human and AI writing:**
     Human's sentences have a wider range in their length w/n a text
     AI writing tend to have even, mid-length sentences and a narrower band of vocabulary.


**What it can't see:**
     Since it's mainly based on stats, it can't see context of the text altogether.


### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->
    

**The rule:**
 When the difference between the two signals is greater than or equal to .2, I would take the average of the sum of the weighted model scores and subtract .1 from it to make it lean toward human written.


**The numbers:**
#Kept
WEIGHT_MODEL_SIGNAL = 0.5
WEIGHT_STYLE_SIGNAL = 0.5

#for ensuring the score leans toward human written:
combined_score = max(0.0, combined_score - 0.1)


**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

Example Text:
> “I learned that cats kneaded blankets from my younger brother who seems to know little fun facts about all types of animals. He told me that cats sometimes knead blankets or softly pound their paws in a “kneading” motion like they’re kneading dough as an old behavior that newborn kittens may do when they’re feeding from their mother’s milk and may knead the area to get more milk out. Ever since I learned about it, I kept seeing posts of cats kneading in my feed (my social media feed may have been eavesdropping on me). Its so cute to watch cats knead their pillows, stuffed toys, and even their owners. I learned it's a sign of affection but it’s also very cute to watch!”

Model Signal: .5
Style Signal: .3






---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | score < 0.3 | Most likely written without the use of an AI.|
| unsure | .3 <= score <= .4  | Difficult to tell whether this was human written. It could be either.|
| high-confidence AI | score >= .4  | Most likely written by an AI. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
     I explicity give a quick reason why there's no clear answer and avoid using the phrase "AI generated" to avoid the reader jumping at the sight of AI and instead try to replace with a calmer alternative "human written". I avoid accusations to the reader and just admit a limit on either the system or on the text given. 



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```terminal

 curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"creator_id\":\"u1\", \"content_id\":\"4db5c97c-c88d-400d-a3c5-b87c343b23b9\", \"reasoning\": \"I try to study with the Pomodoro strategy but sometimes it does not help with my focus. I get distracted so easily. idk why.\"}'
```

**JSON OUTPUT**
```json
{
  "combined_score": 0.039,
  "confidence": 0.4655,
  "content_id": "4db5c97c-c88d-400d-a3c5-b87c343b23b9",
  "guess": "ai",
  "label": "Most likely written by an AI.",
  "model_score": 0.4655,
  "style_score": 0.092
}
```

**An appeal**

```bash
 curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{\"creator_id\":\"u1\", \"content_id\":\"4db5c97c-c88d-400d-a3c5-b87c343b23b9\", \"reasoning\": \"I wrote this informally by myself."}'
```

```json
{
  "content_id": "4db5c97c-c88d-400d-a3c5-b87c343b23b9",
  "message": "Your appeal has been recorded and is under review.",
  "ok": true
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.039,
      "content_id": "4db5c97c-c88d-400d-a3c5-b87c343b23b9",
      "creator_id": "u1",
      "guess": "ai",
      "label": "Most likely written by an AI.",
      "model_score": 0.4655,
      "status": "decided",
      "style_score": 0.092,
      "timestamp": "2026-10-21T17:11:53+00:00"
    },
    {
      "combined_score": 0.039,
      "content_id": "d7a61224-fb70-42f0-96ce-87956dea6257",
      "creator_id": "u1",
      "guess": "ai",
      "label": "Most likely written by an AI.",
      "model_score": 0.4655,
      "status": "decided",
      "style_score": 0.092,
      "timestamp": "2026-10-21T17:12:04+00:00"
    },
    {
      "content_id": "4db5c97c-c88d-400d-a3c5-b87c343b23b9",
      "creator_id": "u1",
      "event": "appeal",
      "reasoning": "I wrote this informally by myself.",
      "status": "under_review",
      "timestamp": "2026-10-21T17:47:01+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Give me a random but light topic that i can make a human, ai generated, formal human writing, and lightly edited ai version to test with
- *What came back:* Topic: why cats knead blankets. It's light and low-stakes, and nobody needs expertise to write about it. It also gives each version room to sound different.

Here's how I'd use it for the four samples:

Human, casual: Write about your own cat, or one you know. Use a personal anecdote, tangents, a fragment or two, uneven sentence lengths, and some quirky punctuation like dashes and parentheses.
AI-generated: Prompt: "Write a short essay about why cats knead blankets." Paste the output as-is.
Formal human: Write an essay-style piece, like a school assignment. Use a clear thesis, topic sentences, and no slang. Keep your own word choices and rhythm.
Lightly edited AI: Take sample 2 and change only about 10–15%. Swap a few words, tweak an opening line, and add one personal detail.
Samples 3 and 4 are the hard cases. Formal human writing tends to look "AI-like" (low punctuation variety, even sentences), and lightly edited AI tends to look human. They should show whether your combining rule holds up.

If you want a backup topic, try "why people put pineapple on pizza" or "the best way to organize a bookshelf."
- *What I changed:* I took its advice and wrote my own human answer to the "Cat Kneading Question" while also shortenting the essay rec to a formal introduction paragraph with a thesis to cut short on text. 

**Moment 2** Debugging

- *What I asked for:*  The code [app.py::submit] i highlighted that you mentioned had a bug, did i fix it?
- *What came back:* It mentioned that I partially had fixed it but forgot another check to validate that the passed value was non empty before passing
- *What I changed:* I added in the non empty check in the code and commented the reasons for it. 

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 7 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
     A real writer may spend some time revisioning or check if a text is human written. They may take some time to read and understand the outcome hence, I think at most 7 posts per minute should be generously realisitic. I lowered it from 10 because it seemed like too many posts to run per minute. 

     I left the rate at 200 however since it seems like a reasonable amount without allowing massive flooding of potentially malicious texts to occur. 


**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
Caller is counted as creator_id. However, counting per creator_id makes the system vulnerable to scripts that tries to look like many callers but actually is just rotating IDs and never hits the limit. The attack set shows that each row submits as a different attacker_<id>. On the otherhand, a shared household is the opposite, since each person has their own ID and gets their own allowance.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 429 429 429 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

#1. Why ai was considred human?
{"timestamp": "2026-10-25T03:12:08+00:00", "content_id": "5e0d41b9-5632-42a8-837b-224ac77860e3", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.367, "combined_score": 0.033, "label": "Most likely written without the use of an AI.", "status": "decided"}

#2. Why "unsure" when it should be "AI" 
{"timestamp": "2026-10-25T03:12:10+00:00", "content_id": "d17cac93-d8c2-4899-800a-72e57c07f317", "creator_id": "attacker_EV05", "guess": "unsure", "model_score": 0.3212, "style_score": 0.249, "combined_score": 0.143, "label": "Difficult to tell whether this was written by a person or an AI. It could be either.", "status": "decided"}

#4. 
{"timestamp": "2026-10-25T03:12:12+00:00", "content_id": "bf6a59da-b498-4aff-8db7-67c488f77b32", "creator_id": "attacker_EV08", "guess": "human", "model_score": 0.2452, "style_score": 0.285, "combined_score": 0.133, "label": "Most likely written without the use of an AI.", "status": "decided"}

#5. Human Read as AI
{"timestamp": "2026-10-25T03:12:13+00:00", "content_id": "9d358641-d159-472d-86a9-5d05a4137cd4", "creator_id": "attacker_FP01", "guess": "ai", "model_score": 0.6175, "style_score": 0.344, "combined_score": 0.14, "label": "Most likely written by an AI.", "status": "decided"}

#6.
{"timestamp": "2026-10-25T03:12:14+00:00", "content_id": "8304f279-5c96-482b-b3fc-c4b1019a8b16", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.403, "combined_score": 0.185, "label": "Most likely written by an AI.", "status": "decided"}

#7.
{"timestamp": "2026-10-25T03:12:14+00:00", "content_id": "4d967342-9842-45b6-8f43-7e87234c1460", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.382, "combined_score": 0.197, "label": "Most likely written by an AI.", "status": "decided"}

#8.
{"timestamp": "2026-10-25T03:12:14+00:00", "content_id": "4099c93e-d00d-4937-952a-497fe3d9232e", "creator_id": "attacker_FP04", "guess": "ai", "model_score": 0.8329, "style_score": 0.326, "combined_score": 0.19, "label": "Most likely written by an AI.", "status": "decided"}

#9. If combined score is low, why still score "AI"
{"timestamp": "2026-10-25T03:12:18+00:00", "content_id": "c33eecfb-bba6-4a4b-a463-d2bb794984d0", "creator_id": "attacker_PI05", "guess": "ai", "model_score": 0.6401, "style_score": 0.239, "combined_score": 0.12, "label": "Most likely written by an AI.", "status": "decided"}

#10. 
{"timestamp": "2026-10-25T03:12:19+00:00", "content_id": "2562950b-ab71-48fd-8763-a3956f315108", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.198, "combined_score": 0.05, "label": "Most likely written without the use of an AI.", "status": "decided"}






```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

{"timestamp": "2026-10-25T03:12:13+00:00", "content_id": "9d358641-d159-472d-86a9-5d05a4137cd4", "creator_id": "attacker_FP01", "guess": "ai", "model_score": 0.6175, "style_score": 0.344, "combined_score": 0.14, "label": "Most likely written by an AI.", "status": "decided"}



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

 Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | 2/9 | MET  | MET  | MET  | PASSED |
| 2. Distinguishable |  |   |   |   |  |
| 3. label coverage |  |   |   |   |  |
| 4. Appeal Test |  |   |   |   |  |
| 5. Handling Invalid Text |  |   |   |   |  |

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
