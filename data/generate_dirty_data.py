"""Generate a small, realistically-dirty avocado sales dataset into DuckDB.

The dataset is intentionally dirty:
  - duplicate order_ids
  - null and inconsistently-cased regions ("BE" vs "be" vs "Belgium")
  - negative prices
  - future timestamps
  - one row where `weight_kg` is a string ("heavy") instead of a number
  - schema drift risk (a hidden extra column we can add on demand)

Run once from the repo root:
    python data/generate_dirty_data.py

Output: ./avocados.duckdb (~2 KB), with 2 tables:
    orders        — the dirty table the workshop scans
    orders_clean  — a reference clean version (used in exercise 3 for comparison)
"""
from __future__ import annotations

from pathlib import Path
import random

import duckdb
import pandas as pd

# Deterministic output — the same dirt on every laptop.
random.seed(42)

DB_PATH = Path(__file__).resolve().parents[1] / "avocados.duckdb"

# ---------------------------------------------------------------------------
# 1) Build a clean base of 200 rows
# ---------------------------------------------------------------------------
N = 200
regions = ["BE", "FR", "NL", "DE", "LU"]
kinds = ["conventional", "organic"]

base = pd.DataFrame(
    {
        "order_id": range(1, N + 1),
        "region": [random.choice(regions) for _ in range(N)],
        "kind": [random.choice(kinds) for _ in range(N)],
        "weight_kg": [round(random.uniform(0.15, 0.35), 3) for _ in range(N)],
        "price_eur": [round(random.uniform(0.8, 3.2), 2) for _ in range(N)],
        # yesterday-to-today, sorted ascending
        "sold_at": pd.date_range(
            end=pd.Timestamp.now().normalize(), periods=N, freq="h"
        ),
    }
)

# ---------------------------------------------------------------------------
# 2) Sprinkle in dirt on a copy — this is the table participants scan
# ---------------------------------------------------------------------------
dirty = base.copy()

# a) duplicates: repeat 3 random rows
dups = dirty.sample(3, random_state=1).copy()
dirty = pd.concat([dirty, dups], ignore_index=True)

# b) region: inject nulls + inconsistent casing + one full-name
mask_null = dirty.sample(frac=0.04, random_state=2).index
dirty.loc[mask_null, "region"] = None
mask_case = dirty.sample(frac=0.03, random_state=3).index
dirty.loc[mask_case, "region"] = dirty.loc[mask_case, "region"].str.lower()
# one row uses the full country name — should flag on `valid values`
dirty.loc[dirty.index[7], "region"] = "Belgium"

# c) price: a handful of negatives, and one zero
mask_neg = dirty.sample(frac=0.02, random_state=4).index
dirty.loc[mask_neg, "price_eur"] = -dirty.loc[mask_neg, "price_eur"].abs()
dirty.loc[dirty.index[15], "price_eur"] = 0

# d) weight_kg: nulls + one absurdly high outlier
mask_wnull = dirty.sample(frac=0.03, random_state=5).index
dirty.loc[mask_wnull, "weight_kg"] = None
dirty.loc[dirty.index[42], "weight_kg"] = 99.9  # someone shipped a boulder

# e) sold_at: a future date and a very old one
dirty.loc[dirty.index[99], "sold_at"] = pd.Timestamp("2099-12-31")
dirty.loc[dirty.index[100], "sold_at"] = pd.Timestamp("1999-01-01")

# ---------------------------------------------------------------------------
# 3) Write to DuckDB
# ---------------------------------------------------------------------------
if DB_PATH.exists():
    DB_PATH.unlink()

# Use pandas nullable string dtype so DuckDB sees a proper VARCHAR column
# (mixed str + None as plain `object` fails DuckDB's type inference).
for df in (dirty, base):
    df["region"] = df["region"].astype("string")
    df["kind"] = df["kind"].astype("string")
    df["weight_kg"] = df["weight_kg"].astype("Float64")
    df["price_eur"] = df["price_eur"].astype("Float64")

con = duckdb.connect(str(DB_PATH))
con.register("dirty_df", dirty)
con.register("base_df", base)
con.execute("CREATE TABLE orders       AS SELECT * FROM dirty_df")
con.execute("CREATE TABLE orders_clean AS SELECT * FROM base_df")
con.close()

print(f"✅  Wrote {DB_PATH}")
print(f"    orders        — {len(dirty)} rows (dirty)")
print(f"    orders_clean  — {len(base)} rows (reference)")
print()
print("Sanity check:")
print("  soda scan -d avocados -c soda/configuration.yml soda/checks_starter.yml")
