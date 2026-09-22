# Exercise 02 · Write your own checks

**⏱ 15 min**

## Goal

Practise the SodaCL vocabulary by writing three new checks yourself.

## The playing field

Look at `soda/checks_extended.yml` — it introduces four things the starter
file didn't cover:

- a **schema** check (structural claim about columns)
- **`valid values`** for categorical consistency
- **`valid min` / `valid max`** for numeric ranges
- a **`failed rows`** check — the escape hatch when built-in metrics aren't enough

Run it and observe:

```bash
soda scan -d avocados -c soda/configuration.yml soda/checks_extended.yml
```

## Your turn

Create a new file `soda/checks_yourname.yml`. Add **three** checks — one from
each family below.

### 1) A completeness check on a different column

Pick any column other than `region`. Aim for zero (or bounded) nulls.

<details>
<summary>Hint</summary>

```yaml
- missing_count(weight_kg) = 0
```

</details>

### 2) A uniqueness check on a combination of columns

*"No two orders were placed for the same `(region, sold_at)` pair"* — express
that as a Soda check.

<details>
<summary>Hint</summary>

Look up `duplicate_count` in the [SodaCL reference](https://docs.soda.io/soda-cl/duplicate.html).
It accepts a list.

</details>

### 3) A custom business rule

Write a `failed rows` check that encodes a rule of your own invention. Some ideas:

- "Organic avocados sold in Belgium never cost more than €3"
- "No row's `weight_kg` is more than 3× the median"
- "Every order in September 2026 has a non-null `region`"

<details>
<summary>Hint</summary>

```yaml
- failed rows:
    name: "your rule in plain English"
    fail condition: <any SQL predicate>
```

</details>

## Run it

```bash
soda scan -d avocados -c soda/configuration.yml soda/checks_yourname.yml
```

## Sanity check

- Does the check FAIL when you expect it to fail?
- Does it PASS after you tweak the threshold?
- Does the check **name** read like something you'd put in a Slack alert? If
  not, rewrite it.
