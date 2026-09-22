# Exercise 01 · Your first Soda scan

**⏱ 10 min**

## Goal

Get comfortable with the Soda loop: **write a check → scan → read the report**.

## Steps

1. Make sure the dataset exists:

   ```bash
   python data/generate_dirty_data.py
   ```

   You should see a message that `avocados.duckdb` was written with 203 rows.

2. Open `soda/checks_starter.yml`. Read the five checks. Notice the shape:

   ```yaml
   checks for orders:
     - <metric>(<column>) <operator> <threshold>:
         name: "human-readable label"
   ```

3. Run the scan:

   ```bash
   soda scan -d avocados -c soda/configuration.yml soda/checks_starter.yml
   ```

4. **Read the output.** You should see **1 PASS and 4 FAIL**. That's expected —
   the dataset is intentionally dirty. For each failed check, jot down:
   - which DQ dimension it covers (completeness / uniqueness / validity / …)
   - what "fix" would make it pass

## Discussion

- Which check is a **structural** claim about the table, and which are
  **content** claims about the rows?
- What happens if you rename `order_id` to `id` in the check but not the
  table? (Try it — then undo.)
- Where in the pipeline would you run this scan — before the data lands in
  the warehouse, or after? Why?
