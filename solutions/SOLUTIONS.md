# Solutions & instructor notes

> **For the room:** try not to open this until you've had a real go. The point
> is to build the *hesitation* muscle, not the copy-paste one.

## Exercise 01 — mapping fails to dimensions

| Failed check                    | DQ dimension        |
| ------------------------------- | ------------------- |
| `region is never null`          | **Completeness**    |
| `order_id is unique`            | **Uniqueness**      |
| `price is positive`             | **Validity**        |
| `sold_at is not in the future`  | **Timeliness**      |

The passing check (`row_count > 0`) is a **completeness** claim about the
table as a whole.

**Where to run this scan:** at the transformation layer (right after dbt),
so you catch dirt without also catching every upstream hiccup you can't
fix. Checks at the source belong to the producer.

## Exercise 02

See [`checks_solution.yml`](./checks_solution.yml).

Common ways participants get it wrong:

- Using `missing_percent > 0` instead of `missing_count > 0` when they want
  zero-tolerance. Both work — the threshold semantics differ.
- Forgetting that `duplicate_count(a, b)` takes columns as arguments (no
  quotes, no list-of-lists).
- Writing `fail condition: price_eur < 0` without a `name:` — the check
  works but the report is unreadable at 3am.

## Exercise 03

The rough on-call playbook we expect them to converge on:

1. **Freshness check** — is today's data even there?
2. **Schema check** — did the shape change?
3. **Row-count anomaly** — is the volume in the usual band?
4. **Value-range checks** — are the numbers sane?

That order matters. If freshness fails, don't page anyone about row-count
anomalies — the upstream is broken.

**Shift-left question:** the negative-price check belongs at the source
(producer contract), the schema check at ingestion, the row-count anomaly
at the transformation layer. Only "the dashboard looks weird" belongs at
serving — and that's not a DQ check, that's a monitoring alert.

## Timing

If the room is faster than expected, the "bonus" is:

- Wire a scan into the CI pipeline (`.github/workflows/soda-ci.yml`
  already does exactly that — walk through it as a bonus).
- Discuss what changes when the checks live in **Soda Cloud** (scheduled,
  UI, incidents, notifications) vs. Soda Core.
