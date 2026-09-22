#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# One-shot: init this folder as a git repo and push it to GitHub.
#
# Usage:
#   ./push.sh                    # default: dataroots/rootsacademy-2026-data-quality
#   ./push.sh myorg my-repo-name # push somewhere else
#
# Needs:
#   - git (you have it)
#   - one of:
#       * gh CLI (`brew install gh && gh auth login`) — creates the repo AND pushes
#       * OR an already-created empty repo on github.com; script falls back to plain git
# -----------------------------------------------------------------------------
set -euo pipefail

ORG="${1:-dataroots}"
NAME="${2:-rootsacademy-2026-data-quality}"
BRANCH="main"

# Sanity: are we in the repo root?
if [[ ! -f "pyproject.toml" || ! -d "soda" ]]; then
  echo "❌  Run this from the repo root (where pyproject.toml lives)."
  exit 1
fi

# Init if needed
if [[ ! -d .git ]]; then
  echo "→  git init"
  git init -q -b "$BRANCH"
fi

# Stage & commit
git add .
if git diff --cached --quiet; then
  echo "→  nothing new to commit"
else
  echo "→  git commit"
  git commit -q -m "Initial commit: Roots Academy 2026 Data Quality session

- Full slide deck (slides/DataQuality-RA2026.pptx)
- Soda Core hands-on: starter + extended check files
- 3 exercises (markdown) + optional Jupyter notebook
- Dirty avocado dataset generator (DuckDB, deterministic)
- GitHub Actions workflow: DQ scan in CI
"
fi

# Path A: gh CLI available → create + push in one shot
if command -v gh >/dev/null 2>&1; then
  echo "→  gh detected — creating repo dataroots/${NAME} and pushing"
  gh repo create "${ORG}/${NAME}" \
      --public \
      --description "Data Quality session for Roots Academy 2026 (Dataroots)" \
      --source=. \
      --remote=origin \
      --push
  echo ""
  echo "✅  Done. View at: https://github.com/${ORG}/${NAME}"
  exit 0
fi

# Path B: no gh → tell the user what to do
echo ""
echo "⚠  gh CLI not found."
echo ""
echo "Do one of these two things, then re-run this script (or follow along manually):"
echo ""
echo "  Option 1 — install gh (recommended, 30s):"
echo "      brew install gh && gh auth login"
echo "      ./push.sh"
echo ""
echo "  Option 2 — create the empty repo yourself via web UI, then run:"
echo "      git remote add origin git@github.com:${ORG}/${NAME}.git"
echo "      git branch -M ${BRANCH}"
echo "      git push -u origin ${BRANCH}"
echo ""
echo "The local commit is ready — this is only about wiring the remote."
