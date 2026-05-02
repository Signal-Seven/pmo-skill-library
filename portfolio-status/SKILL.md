---
name: portfolio-status
description: Classify epic status across portfolio using consistent On Track, At Risk,
  and Critical definitions. Applies to weekly reporting, escalation triage, and
  on-demand portfolio health checks. Use when generating any portfolio status view,
  weekly report, or leadership update.
---

# Portfolio Status Classification Skill

## Status Definitions

**ON TRACK**
- Velocity within 10% of four-sprint rolling average
- Delivery date confidence rated 4 or 5 by owning team
- No unresolved blockers older than one sprint
- All known dependencies confirmed or resolved

**AT RISK** (any one condition)
- Velocity 10-30% below four-sprint rolling average
- Delivery confidence rated 3 by owning team
- Two or more unresolved blockers open
- One unconfirmed dependency on a constrained team

**CRITICAL** (any one condition)
- Velocity more than 30% below four-sprint rolling average
- Delivery confidence rated 1 or 2 by owning team
- Three or more unresolved blockers
- Hard dependency blocking delivery with no resolution path

---

## Data Sources [CUSTOMIZE]
PRIMARY: Jira MCP connector
- Active epics in projects: [YOUR_PROJECT_KEYS]
- Fields: completion %, velocity (current vs 4-sprint avg), open blockers, team confidence

SECONDARY: Slack #[YOUR_TEAM_UPDATES_CHANNEL] for this week's status posts

---

## Portfolio-Level Summary
Health score = percentage of epics On Track
Report structure:
1. Health score: X of Y epics On Track (Z%)
2. Requires immediate attention: [Critical epics]
3. Monitoring closely: [At Risk epics]
4. Director decision needed: [trade-off flags]

---

## Reporting Standards
- Two sentences maximum per epic status narrative
- Lead with WHAT CHANGED since last week, not current state
- Flag blockers with owning team name and age in sprints
- Never use "challenges" — name the specific issue
- Never use passive constructions that hide ownership

---

## Output File
Format using template at: [CUSTOMIZE: /PMO/Templates/weekly-status.docx]
Save to: [CUSTOMIZE: /PMO/Reports/Weekly/] with date in filename
