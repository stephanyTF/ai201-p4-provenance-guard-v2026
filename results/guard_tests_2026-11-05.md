# Abuse guard tests — 2026-11-05

| Criterion | Scenario | Expected | Actual | Result |
|---|---|---|---|---|
| No collateral damage | 1 client, 1 creator_id, 5 posts | `[200, 200, 200, 200, 200]` | `[200, 200, 200, 200, 200]` | PASS |
| 1. Max 2 creator_ids per client | 1 client rotates 5 creator_ids, 1 post each | `[200, 200, 403, 403, 403]` | `[200, 200, 403, 403, 403]` | PASS |
| 1. Max 2 creator_ids per client | same client reuses an id it already holds | `[200]` | `[200]` | PASS |
| 2. Per-client limit (7/min across ids) | 1 client, 2 creator_ids alternating, 15 posts | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 429, 429, 429]` | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 429, 429, 429]` | PASS |
| 3. Global limit (20/min total) | 5 clients x 5 posts = 25 posts | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 429, 429, 429, 429, 429]` | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 429, 429, 429, 429, 429]` | PASS |
| Cost: shared network (legit users) | 1 classroom IP, 10 students, 1 post each | `[200, 200, 403, 403, 403, 403, 403, 403, 403, 403]` | `[200, 200, 403, 403, 403, 403, 403, 403, 403, 403]` | PASS |

**Cost:** 8 / 10 legitimate requests blocked unfairly (80%) — 1 classroom IP, 10 legit students, 1 post each
