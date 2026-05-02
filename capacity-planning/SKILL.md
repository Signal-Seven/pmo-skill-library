---
name: capacity-planning
description: Generate rolling capacity availability view by team from Jira sprint
  data and your Excel capacity model. Use for intake trade-off checks, scenario
  modeling when comparing competing initiatives, and the weekly demand loop
  re-scoring. Identifies constrained teams and calculates absorption capacity
  for new work.
---

# Capacity Planning Skill

## Data Sources [CUSTOMIZE]
PRIMARY: Jira MCP connector
- Query: current sprint allocation for all active teams in [YOUR_PROJECTS]
- Fields: team, committed story points, capacity points, velocity (current vs planned)

SECONDARY: Capacity model at [CUSTOMIZE: /PMO/Capacity/Q[N]-capacity-model.xlsx]
- Pull: headcount by team, planned PTO, committed allocation by week

## Calculations

Per team:
- current_utilization = committed / available_capacity (as percentage)
- rolling_availability = available capacity over next 6 weeks by week
- constraint_flag = any 2-week window projected above 90%
- absorption_capacity = bandwidth available for new intake (team-weeks)

Portfolio:
- total_available_capacity in team-weeks across all teams
- constrained_teams list (>90% average utilization)
- open_teams list (<80% average, available for new intake)

## Scenario Modeling
When modeling impact of activating a new initiative:
1. Identify required team(s) and estimated duration
2. Calculate week-by-week utilization impact
3. Flag any 2-week window exceeding 90% threshold
4. Calculate delivery date impact on top five existing commitments
5. Return: feasibility rating, constrained weeks, delivery impact summary

## Trade-Off Input for intake-triage
Provide absorption_capacity percentage per team in target quarter
so intake-triage Skill can calculate trade-off flag accurately.

## Output Format
1. Portfolio availability summary: total team-weeks available for new work
2. Team table: team, current utilization %, 6-week trend, constraint flag, absorption capacity
3. Constrained teams section: projected bottleneck weeks highlighted
4. Scenario output (if requested): utilization impact and delivery risk per scenario
