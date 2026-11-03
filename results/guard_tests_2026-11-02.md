# Abuse guard tests — 2026-11-02

| Criterion | Scenario | Expected | Actual | Result |
|---|---|---|---|---|
| No collateral damage | 1 client, 1 creator_id, 5 posts | `[200, 200, 200, 200, 200]` | `[200, 200, 200, 200, 200]` | PASS |
| 1. Max 2 creator_ids per client | 1 client rotates 5 creator_ids, 1 post each | `[200, 200, 403, 403, 403]` | `[200, 200, 403, 403, 403]` | PASS |
| 1. Max 2 creator_ids per client | same client reuses an id it already holds | `[200]` | `[200]` | PASS |
| 2. Per-client limit (7/min across ids) | 1 client, 2 creator_ids alternating, 10 posts | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 429, 429, 429]` | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200]` | FAIL |
| 3. Global limit (20/min total) | 5 clients x 5 posts = 25 posts | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 429, 429, 429, 429, 429]` | `[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 429, 429, 429, 429, 429]` | PASS |
