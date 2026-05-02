---
name: portfolio-health-view
description: Generate an on-demand portfolio health intelligence view from live
  Jira data. Produces status classification, completion metrics, velocity trends,
  and blocker summary across all active epics. Use when asked for portfolio health,
  epic status, weekly snapshot, or leadership health check.
---

# On-Demand Portfolio Health Dashboard Skill

## Trigger Phrases
"show me portfolio health" | "portfolio status" | "health snapshot"
"which epics are at risk" | "give me the dashboard"

## Data Sources [CUSTOMIZE]
PRIMARY: Jira MCP — all active epics in [YOUR_PROJECT_KEYS]
SECONDARY: Slack [#YOUR_TEAM_CHANNEL] — status posts this week

## Calculations
Apply portfolio-status Skill definitions to each epic.
Portfolio health score = percentage of epics On Track.

## Output Sections
1. Executive summary: health score, counts by status, top concern in one sentence
2. Epic table: name, team, completion %, velocity %, blocker count, status badge
3. Critical section: specific blocker detail for each Critical epic
4. At Risk section: primary risk factor for each At Risk epic
5. Recommended actions: one line per At Risk or Critical epic
6. Generated timestamp and data source note
