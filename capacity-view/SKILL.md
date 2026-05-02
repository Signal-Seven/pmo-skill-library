---
name: capacity-view
description: Generate an on-demand capacity utilization view by team from live
  Jira and capacity model data. Shows current utilization, 6-week rolling forecast,
  constraint flags, and absorption capacity for new intake. Use when asked for
  capacity, availability, team bandwidth, or utilization data.
---

# On-Demand Capacity Intelligence Skill

## Trigger Phrases
"show me capacity by team" | "team availability" | "which teams are constrained"
"capacity check" | "how much bandwidth do we have"

## Data Sources [CUSTOMIZE]
PRIMARY: Jira MCP — current sprint allocation per team in [YOUR_PROJECTS]
SECONDARY: Capacity model at [YOUR_CAPACITY_MODEL_PATH]

## Output Sections
1. Portfolio summary: total available capacity in team-weeks
2. Team table: team, current utilization %, 6-week trend, constraint flag, absorption capacity
3. Constrained section: teams above 90% with projected bottleneck weeks highlighted
4. Available section: teams below 80% ready for new intake
5. Recommended intake candidates: highest-scored pending items that fit current availability
6. Generated timestamp
