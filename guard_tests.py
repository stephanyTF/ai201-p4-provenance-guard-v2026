#!/usr/bin/env python3
"""
Abuse-guard tests — no server and no model needed.

    python guard_tests.py

Drives the Flask app in-process with the test client, faking a different caller
address per scenario via REMOTE_ADDR, and stubs the two signals so the run takes
seconds. Each scenario resets the limiter and the creator_id tracker, then
checks the status codes against the criterion it covers.

Does 3 things:

    1. Writes results/guard_tests_<date>.md (in README)
    
    2. Adds JSON line per scenario to logs/guard_tests.jsonl (timestamp, run_id, input, output, duration_ms). 

    3. Test traffic goes to logs/guard_tests_audit.jsonl so it never lands in the real logs/audit.jsonl.
"""

import datetime as dt
import json
import sys
import time
import uuid

import app as app_module
import config
import detector
import stylometry

# Signals are set at .5 to simulate moderate risk but the focus in on the rate limiting behavior 
# to protect the system against bad actors.
detector.model_signal = lambda text: 0.5
stylometry.style_signal = lambda text: 0.5

# Keep test traffic out of the real audit log. audit.py reads config.AUDIT_LOG
# on every write, so repointing it here is enough.
config.AUDIT_LOG = config.LOG_DIR / "guard_tests_audit.jsonl"

# One structured record per scenario, appended across runs and told apart by run_id.
TEST_LOG = config.LOG_DIR / "guard_tests.jsonl"
RUN_ID = uuid.uuid4().hex[:8]

client = app_module.app.test_client()
_counter = 0


def fresh_text():
    """Unique words every time, so the repetitive-text check never fires."""
    global _counter
    _counter += 1
    return " ".join(f"word{_counter}x{i}" for i in range(20))


def reset():
    app_module.limiter.reset()
    app_module._creator_ids_by_client.clear()


def post(ip, creator_id):
    resp = client.post(
        "/submit",
        json={"text": fresh_text(), "creator_id": creator_id},
        environ_base={"REMOTE_ADDR": ip},
    )
    return resp.status_code


def codes(pairs):
    return [post(ip, cid) for ip, cid in pairs]


def run():
    results = []

    def check(criterion, scenario, expected, pairs):
        """Send `pairs` as /submit calls, time them, log the scenario, record the result."""
        start = time.perf_counter()
        actual = codes(pairs)
        duration_ms = round((time.perf_counter() - start) * 1000, 1)
        ok = expected == actual
        results.append((criterion, scenario, expected, actual, ok))
        log_scenario(criterion, scenario, pairs, expected, actual, ok, duration_ms)

    # 0. Baseline — a normal client is untouched.
    reset()
    check("No collateral damage",
          "1 client, 1 creator_id, 5 posts",
          [200] * 5,
          [("10.0.0.1", "alice")] * 5)

    # 1. Identity cap — rotating creator_ids.
    reset()
    check("1. Max 2 creator_ids per client",
          "1 client rotates 5 creator_ids, 1 post each",
          [200, 200, 403, 403, 403],
          [("10.0.0.2", f"rot{i}") for i in range(5)])
    check("1. Max 2 creator_ids per client",
          "same client reuses an id it already holds",
          [200],
          [("10.0.0.2", "rot0")])

    # 2. Per-client limit — two ids, one address, 15 posts (5 each, under 7 per creator).
    reset()
    check("2. Per-client limit (7/min across ids)",
          "1 client, 2 creator_ids alternating, 15 posts",
          [200] * config.CLIENT_RATE_LIMIT_PER_MINUTE + [429] * 3,
          [("10.0.0.3", "pair_a" if i % 2 == 0 else "pair_b") for i in range(15)])

    # 3. Global limit — five clients, five posts each = 25 in a minute.
    reset()
    check("3. Global limit (20/min total)",
          "5 clients x 5 posts = 25 posts",
          [200] * config.GLOBAL_RATE_LIMIT_PER_MINUTE + [429] * 5,
          [(f"10.0.1.{c}", f"g{c}") for c in range(5) for _ in range(5)])

    # 4.  Cost — a shared classroom. 10 different legit students on ONE address,
    # one post each. Nobody is abusing anything, so every non-200 is an unfair block.
    reset()
    classroom = [("10.0.2.1", f"student{i}") for i in range(10)]
    check("Cost: shared network (legit users)",
          "1 classroom IP, 10 students, 1 post each",
          [200] * config.MAX_CREATOR_IDS_PER_CLIENT
          + [403] * (10 - config.MAX_CREATOR_IDS_PER_CLIENT),
          classroom)
    blocked = sum(1 for c in results[-1][3] if c != 200)
    COSTS.append({"scenario": "1 classroom IP, 10 legit students, 1 post each",
                  "legit_requests": len(classroom),
                  "blocked": blocked,
                  "blocked_pct": round(100 * blocked / len(classroom))})

    return results


COSTS = []


def log_scenario(criterion, scenario, pairs, expected, actual, ok, duration_ms):
    """Append one JSON line to logs/guard_tests.jsonl."""
    record = {
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "run_id": RUN_ID,
        "criterion": criterion,
        "scenario": scenario,
        "input": [{"client_ip": ip, "creator_id": cid} for ip, cid in pairs],
        "expected": expected,
        "output": actual,
        "passed": ok,
        "duration_ms": duration_ms,
    }
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    with TEST_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def main():
    if not config.RATE_LIMITING_ENABLED or not config.ABUSE_GUARD_ENABLED:
        print("Rate limiting and the abuse guard must both be ON for this test.")
        return 2

    # Start each run with an empty test audit log so it only holds this run.
    config.AUDIT_LOG.unlink(missing_ok=True)

    results = run()

    lines = [
        f"# Abuse guard tests — {dt.date.today()}",
        "",
        "| Criterion | Scenario | Expected | Actual | Result |",
        "|---|---|---|---|---|",
    ]
    for criterion, scenario, expected, actual, ok in results:
        lines.append(f"| {criterion} | {scenario} | `{expected}` | `{actual}` | "
                     f"{'PASS' if ok else 'FAIL'} |")
    for c in COSTS:
        lines.append("")
        lines.append(f"**Cost:** {c['blocked']} / {c['legit_requests']} legitimate requests "
                     f"blocked unfairly ({c['blocked_pct']}%) — {c['scenario']}")
    report = "\n".join(lines) + "\n"

    print(report)
    config.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = config.RESULTS_DIR / f"guard_tests_{dt.date.today()}.md"
    out.write_text(report, encoding="utf-8")
    print(f"Wrote {out}")
    return 0 if all(r[-1] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
