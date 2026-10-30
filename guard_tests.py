#!/usr/bin/env python3
"""
Abuse-guard tests — no server and no model needed.

    python guard_tests.py

Drives the Flask app in-process with the test client, faking a different caller
address per scenario via REMOTE_ADDR, and stubs the two signals so the run takes
seconds. Each scenario resets the limiter and the creator_id tracker, then
checks the status codes against the criterion it covers.

Writes results/guard_tests_<date>.md, which is what the README pastes.
"""

import datetime as dt
import sys

import app as app_module
import config
import detector
import stylometry

# The guard is about who sends, not what the signals say.
detector.model_signal = lambda text: 0.5
stylometry.style_signal = lambda text: 0.5

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

    def check(criterion, scenario, expected, actual):
        results.append((criterion, scenario, expected, actual, expected == actual))

    # 0. Baseline — a normal client is untouched.
    reset()
    check("No collateral damage",
          "1 client, 1 creator_id, 5 posts",
          [200] * 5,
          codes([("10.0.0.1", "alice")] * 5))

    # 1. Identity cap — rotating creator_ids.
    reset()
    got = codes([("10.0.0.2", f"rot{i}") for i in range(5)])
    check("1. Max 2 creator_ids per client",
          "1 client rotates 5 creator_ids, 1 post each",
          [200, 200, 403, 403, 403],
          got)
    check("1. Max 2 creator_ids per client",
          "same client reuses an id it already holds",
          [200],
          codes([("10.0.0.2", "rot0")]))

    # 2. Per-client limit — two ids, one address, 10 posts (5 each, under 7/creator).
    reset()
    got = codes([("10.0.0.3", "pair_a" if i % 2 == 0 else "pair_b") for i in range(10)])
    check("2. Per-client limit (7/min across ids)",
          "1 client, 2 creator_ids alternating, 10 posts",
          [200] * config.CLIENT_RATE_LIMIT_PER_MINUTE + [429] * 3,
          got)

    # 3. Global limit — five clients, five posts each = 25 in a minute.
    reset()
    got = codes([(f"10.0.1.{c}", f"g{c}") for c in range(5) for _ in range(5)])
    check("3. Global limit (20/min total)",
          "5 clients x 5 posts = 25 posts",
          [200] * config.GLOBAL_RATE_LIMIT_PER_MINUTE + [429] * 5,
          got)

    return results


def main():
    if not config.RATE_LIMITING_ENABLED or not config.ABUSE_GUARD_ENABLED:
        print("Rate limiting and the abuse guard must both be ON for this test.")
        return 2

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
    report = "\n".join(lines) + "\n"

    print(report)
    config.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = config.RESULTS_DIR / f"guard_tests_{dt.date.today()}.md"
    out.write_text(report, encoding="utf-8")
    print(f"Wrote {out}")
    return 0 if all(r[-1] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
