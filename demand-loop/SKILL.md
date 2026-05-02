---
name: demand-loop
description: Manage the autonomous weekly demand pipeline. Re-scores the intake
  queue against the current capacity model, generates parking lot communications
  for deprioritized requests, and produces demand trend summaries for the weekly
  portfolio report. Runs on Monday morning schedule via Cowork.
---

# Autonomous Demand Loop Skill

## Weekly Execution Steps
Run in this order every Monday at [CUSTOMIZE: 7am]:

1. Pull new intake submissions from [CUSTOMIZE: #pmo-intake] Slack channel since last run
2. Pull new submissions from [CUSTOMIZE: intake@company.com] email alias since last run
3. Process each new submission through the intake-triage Skill
4. Re-score full intake queue against current capacity model
5. Flag items now within capacity window for Director review
6. Generate parking lot communications for items not advancing this cycle
7. Save communications to [CUSTOMIZE: /PMO/Communications/Outbox/] for Director review before sending
8. Produce demand volume summary section for weekly portfolio report

---

## Queue Re-Scoring Logic
For each item in the pending intake queue:
- Pull current capacity availability for the target quarter (from capacity model)
- Recalculate feasibility score if team allocation has changed
- Update trade-off flag status if capacity changed since last scoring
- Re-sort queue by total score descending
- Surface items where projected activation window opened this week

---

## Parking Lot Communication Template [CUSTOMIZE]

Subject: Update on your initiative — [INITIATIVE_TITLE]

[REQUESTER_NAME],

Your initiative [INITIATIVE_TITLE] was reviewed in this week's prioritization cycle.

**Priority Score:** [SCORE]/25
**Classification:** [CLASSIFICATION]

**Why it is not advancing this cycle:**
[One sentence on the specific reason: capacity constraint, trade-off, or timing]

**What it traded against:**
To activate in [TARGET_QUARTER], this would have required trading against
[TOP_COMPETITOR_TITLE] (score: [SCORE], currently [STATUS]).

**Re-evaluation:**
This request will be automatically re-evaluated on [NEXT_REVIEW_DATE].
If your situation changes or you have additional context, reply to this message.

No action is needed from you at this time.

[YOUR_NAME]
Portfolio Management Office

---

## Demand Trend Metrics (include in weekly report)
- Total submissions this week vs. prior week
- Acceptance rate (advanced / total submitted)
- Breakdown by classification (Strategic / Platform / Change / Operational)
- Breakdown by submitting team (top five)
- Demand acceleration index: submissions this 4 weeks / prior 4 weeks
  (index > 1.2 = accelerating, flag in report)
- Top three highest-scored parked items (may be ready to activate if capacity opens)

---

## File Paths [CUSTOMIZE]
Intake queue: /PMO/Demand/[QUARTER]-queue.xlsx
Outbox: /PMO/Communications/Outbox/
Weekly report section: append to /PMO/Reports/Weekly/[DATE]-portfolio-report.docx
