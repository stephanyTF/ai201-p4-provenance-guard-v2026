# Capstone Criteria (Unit 9-10)

1. Baseline: 1 good user w/ 1 client id is able to submit 5 posts under the 7 per post per minute rate 


2. Per-creator limit: 7 posts per minute per creator_id (Unit 8).

3. Per-client limit: 7 client's posts per minute max across all its creator_ids combined based on IP address. 

4. Global limit: 20 posts per minute for the whole service.

5. Identity cap: At most 2 MAX_CREATOR_IDS_PER_CLIENT distinct creator_ids per IP.


# Acceptance criteria — Provenance Guard Unit 8


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
## 1. At most 2 false positives in 9 

<!-- Your criterion. It must name a number. -->

**Why this target:** The number of allowed false positives is low because on a writing site a wrong accusation costs more than a missed detection, however appeals should allow for those false positives be cleared as the system shouldn't be too lenient as well. 


---

## 2. (Distinguishable) A clearly-AI and clearly-human text score difference should be at least .5

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
