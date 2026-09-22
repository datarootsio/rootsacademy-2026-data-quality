# Exercise 03 · Break it on purpose

**⏱ 15 min**

## Goal

Build muscle memory for the **failure loop**: something went wrong upstream,
your DQ checks caught it, now what?

## Scenario

You're on-call for the `orders` pipeline. It's Monday 8am. Slack blew up
because "the dashboard looks weird". You suspect the upstream extract
mangled today's rows.

## Setup

The `orders_clean` table in the same DuckDB file is a reference clean
version (200 rows, no dirt). We'll use it as our "yesterday's known-good
state" and simulate today's disaster.

## Part A — reproduce a real incident

Open a Python shell and inject a specific kind of dirt into a copy of the
clean table:

```python
import duckdb
con = duckdb.connect("avocados.duckdb")

# Start from the known-good copy
con.execute("DROP TABLE IF EXISTS orders_today")
con.execute("CREATE TABLE orders_today AS SELECT * FROM orders_clean")

# --- Choose ONE incident to inject and comment the others ---

# Incident A: a producer bug set 30% of prices to negative
con.execute("UPDATE orders_today SET price_eur = -price_eur WHERE order_id % 3 = 0")

# Incident B: a schema-drift rename broke the pipeline (region → country_code)
# con.execute("ALTER TABLE orders_today RENAME region TO country_code")

# Incident C: the CDC batch double-inserted every row
# con.execute("INSERT INTO orders_today SELECT * FROM orders_today")

con.close()
```

Now write a `soda/checks_today.yml` that runs against `orders_today` (not
`orders`) and would catch **all three** incident types above. Then flip
the comments to switch incidents and re-scan.

## Part B — the checks that would have caught it *before* it landed

Which of your checks belong at the **source** (before ingestion)?
Which belong at the **transformation** layer (dbt tests)?
Which are only detectable at the **serving** layer?

There's no single right answer — argue it with the person next to you.

## Discussion

- What's the difference between a **check** that fails once (bad row) and a
  **check** that fails silently forever (bad rule)?
- If your on-call phone rings for a DQ check failure at 3am, what should the
  check output include so you can act without opening a laptop?
- Should a failed DQ check block the pipeline (fail-loud) or just alert
  (fail-open)? Give a case for each.
