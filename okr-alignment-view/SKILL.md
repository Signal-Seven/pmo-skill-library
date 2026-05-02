---
name: okr-alignment-view
description: Generate an on-demand OKR alignment intelligence view showing
  portfolio contribution scores per organizational goal. Surfaces under-invested
  OKRs and misaligned active initiatives. Use when asked for OKR alignment,
  goal contribution, strategic alignment analysis, or investment prioritization.
---

# On-Demand OKR Alignment Intelligence Skill

## Trigger Phrases
"show me OKR alignment" | "which OKRs are at risk" | "goal contribution"
"what is our portfolio contributing to" | "alignment check"

## Data Sources [CUSTOMIZE]
PRIMARY: Jira MCP — all active epics in [YOUR_PROJECT_KEYS]
SECONDARY: OKR framework at [YOUR_OKR_DOCUMENT_PATH]

## Apply goal-alignment Skill definitions for scoring.

## Output Sections
1. OKR summary table: OKR name, total contribution score, threshold, status (Met / At Risk)
2. Contribution matrix: initiatives as rows, OKRs as columns, scores in each cell
3. Under-invested OKRs: below threshold with top intake queue candidates that address gap
4. Misaligned actives: epics contributing to no current goal (total score <= 2)
5. Generated timestamp
