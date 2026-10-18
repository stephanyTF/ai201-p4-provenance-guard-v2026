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
## 1. At most 2 false positives in 10 

<!-- Your criterion. It must name a number. -->

**Why this target:** The number of allowed false positives is low because on a writing site a wrong accusation costs more than a missed detection, however appeals should allow for those false positives be cleared as the system shouldn't be too lenient as well. 


---

## 2. A clearly-AI and clearly-human text score should score difference should be at least .5

<!-- Your criterion. -->

**Why this target:**
  .2 is a significanlty large enough distance to differentiate the scores.



---

## 3. Across a test set of 9 pieces (3 clearly human, 3 clearly AI, 3 borderline), each of the three labels (human, ai, unsure) is returned at least once, in each of the 3 trials.

<!-- Your criterion. -->


**Why this target:** 3 is the minimum number for ensuring that each label is correctly identified and the same number of trials help make it fair. Unsure has to be reachable because its gap helps differentiate clearly between AI and human writing.



---

## 4. At least 7 in 10 appeals should lead to a status change and be recorded

<!-- Your criterion. -->


**Why this target:**
This helps ensure that any false positives would have a chance of being correctly identified however we want to ensure that this is not always true to ensure we're not easily allowing correctly AI identified text to pass through as human.


---

## 5. Missing and/or empty test should always avoid scoring and request the user again to submit a non empty text while an enormous text should also be avoided to score and instead notify the user to shorten their content

<!-- Your criterion. -->

**Why this target:** This ensures that the flow of the model's service is not interuppted but encourages continued action on the user part by asking them to alter their input in a different way



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
