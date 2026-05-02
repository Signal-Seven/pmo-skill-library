---
name: continuous-planning
description: Run the seven-stage continuous planning pipeline and generate the
  six-week planning review package. Use when preparing for planning review
  sessions, when evaluating the full pipeline state, or when generating the
  automated review package before a planning cadence meeting.
---

# Continuous Planning Skill

## The Seven-Stage Pipeline

**Stage 1: Intake and Classification**
All new submissions processed through intake-triage Skill.
Nothing waits for a planning meeting to be acknowledged.

**Stage 2: Goal Alignment Check**
Score against current OKRs using goal-alignment Skill before advancing.
Items with total OKR score <= 2 flagged for clarification, not advanced.

**Stage 3: Capacity Availability Check**
Query rolling 6-week model using capacity-planning Skill.
Items with no capacity home held in staging with projected window.

**Stage 4: Prioritization and Sequencing**
Generate ranked recommendation for items passing Stages 2 and 3.
Include rationale for each placement and sequencing risks.
PMO Director reviews and adjusts — recommendation only, not decision.

**Stage 5: Activation**
Generate activation artifacts for approved items:
- Capacity allocation confirmation
- Success metric and measurement date
- Dependency map with owning teams
- Team briefing paragraph
- Review cadence

**Stage 6: Active Monitoring**
Apply portfolio-status Skill to all in-flight epics weekly.
Feed capacity actuals back into Stage 3 model each Monday.

**Stage 7: Close and Signal Capture**
On epic completion, generate close summary:
- Velocity vs. estimate (story points and calendar time)
- Dependencies resolved vs. still open
- What changed from original scope
- Signals that should adjust future intake scoring

## Six-Week Review Package
Generate before each planning review session. Include:
1. Portfolio status for all active epics (portfolio-status Skill output)
2. Full scored intake queue sorted by priority score
3. Capacity availability per team for next 6 weeks (capacity-planning output)
4. Goal alignment scores for active and pending work (goal-alignment output)
5. Trade-off flags requiring Director decision
6. Staging queue items with projected activation windows

Format using: [CUSTOMIZE: /PMO/Templates/continuous-planning-review.docx]
Save to: [CUSTOMIZE: /PMO/Planning/Reviews/] with review date in filename
