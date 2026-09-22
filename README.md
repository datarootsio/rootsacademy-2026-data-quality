# Roots Academy 2026 — Data Quality

Materials for the **Data Quality** morning session at Roots Academy 2026 (Dataroots).

> **Instructor:** Eya Akrimi · Data Engineer @ Dataroots
> **When:** Wed 23 Sept 2026 · 9:00 → 12:00
> **Format:** ~2h theory + ~50min hands-on with [Soda Core](https://www.soda.io/)

---

## For the participants — 5-minute setup

You will need **Python 3.10+** and **git**. Everything else is installed by `uv sync` (or `pip install -e .`).

```bash
# 1. Clone
git clone https://github.com/dataroots/rootsacademy-2026-data-quality.git
cd rootsacademy-2026-data-quality

# 2. Install (choose one)
uv sync                              # ← fast, recommended
# or
python -m venv .venv && source .venv/bin/activate && pip install -e .

# 3. Generate the dirty dataset
python data/generate_dirty_data.py

# 4. First scan (should show 4 fails, 1 pass — that's the point)
soda scan -d avocados -c soda/configuration.yml soda/checks_starter.yml
```

If the last command prints check results, **you're ready** — close the terminal until 11am.

---

## Agenda

| Time          | Block                                                   |
| ------------- | ------------------------------------------------------- |
| 9:00 – 9:15   | Intro + agenda + knowledge check                        |
| 9:15 – 9:35   | 01 · **Why data quality**                               |
| 9:35 – 10:00  | 02 · **What is DQ + the 6 dimensions**                  |
| 10:00 – 10:15 | 03 · **Profiling**                                      |
| 10:15 – 10:30 | ☕ **Break**                                             |
| 10:30 – 10:50 | 04 · **Where DQ lives in a pipeline** (shift-left)      |
| 10:50 – 11:00 | 05 · **Tool landscape** (Soda, GX, dbt tests, …)        |
| 11:00 – 11:50 | 06 · **Hands-on with Soda** 🛠️                          |
| 11:50 – 12:00 | 07 · **Wrap & Q&A**                                     |

---

## Repo layout

```
.
├── README.md
├── pyproject.toml            ← deps: soda-core-duckdb, pandas, jupyter
├── data/
│   └── generate_dirty_data.py    ← creates avocados.duckdb with realistic dirt
├── soda/
│   ├── configuration.yml         ← the DuckDB data source
│   ├── checks_starter.yml        ← the 5 checks we run first
│   └── checks_extended.yml       ← more checks for exercise 2
├── exercises/
│   ├── 01_first_scan.md          ← guided walkthrough
│   ├── 02_add_your_checks.md     ← write your own
│   ├── 03_break_it_on_purpose.md ← inject bad data, watch it fail
│   └── notebook.ipynb            ← optional Jupyter path
├── solutions/
│   ├── checks_solution.yml
│   └── SOLUTIONS.md              ← DO NOT PEEK 👀
├── slides/
│   └── DataQuality-RA2026.pptx
└── .github/workflows/
    └── soda-ci.yml               ← DQ in CI (bonus discussion at the end)
```

---

## About Soda in one paragraph

**Soda Core** is an open-source data quality framework. You write human-readable
checks in YAML (`SodaCL`) — things like *"no missing values in `region`"* or
*"row count > 0"* — and `soda scan` runs them against a database. It supports
DuckDB, PostgreSQL, Snowflake, BigQuery, Databricks and more. If you like what
you see today, its bigger sibling **Soda Cloud** adds a UI, scheduling,
notifications and a data catalog integration — same YAML checks, hosted.

---

## Credits & prior art

Builds on the prior Dataroots RA data-quality sessions (2023 Great Expectations
by the KBC team; 2024 Data Quality). Story arc & 6-dimensions taxonomy adapted
from those decks; hands-on rebuilt around Soda + DuckDB so nothing needs cloud
credentials.

## License

MIT — see [LICENSE](./LICENSE).
