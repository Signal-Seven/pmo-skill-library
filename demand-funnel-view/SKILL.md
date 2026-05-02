---
name: demand-funnel-view
description: Generate an on-demand demand funnel intelligence view showing intake
  volume, acceptance rates, classification breakdown, and submission trends by
  team. Use when asked for demand trends, intake analysis, pipeline visibility,
  or submission volume data.
---

# On-Demand Demand Funnel Intelligence Skill

## Trigger Phrases
"show me demand trends" | "intake volume" | "which teams are submitting the most"
"demand funnel" | "pipeline trends" | "what is coming in"

## Data Sources [CUSTOMIZE]
PRIMARY: Slack MCP — all messages in [#YOUR_INTAKE_CHANNEL] since [QUARTER_START]
SECONDARY: /PMO/Intake/Processed/ — all intake summaries with scores and dispositions

## Calculations
Weekly: total submissions, advanced, parked, acceptance rate (advanced/submitted)
By classification: count per type
By team: submissions per submitting team
Demand acceleration index: submissions this 4 weeks / prior 4 weeks
  (index > 1.2 = accelerating significantly, flag in output)
Top parked items: highest-scored items not currently active

## Output Sections
1. Summary: total submissions, acceptance rate, average scores (advanced vs parked)
2. Weekly table: submissions, advanced, parked, acceptance rate per week
3. Classification breakdown
4. By-team breakdown with top three highlighted
5. Demand acceleration note if index > 1.2
6. Top three parked items ready to activate when capacity opens
7. Generated timestamp
