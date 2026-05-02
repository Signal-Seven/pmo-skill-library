---
name: enterprise-portfolio-status
description: Generate a consolidated portfolio status view across multiple business
  units, teams, and Jira instances. Use when producing executive-level portfolio
  health reports that span more than one portfolio or business unit. Applies
  consistent status definitions across all connected data sources and produces
  a single coherent view regardless of how many systems or teams are involved.
  Different from portfolio-status which operates on a single portfolio.
---

# Enterprise Portfolio Status Skill

## When to Use This Skill
Use this Skill when you need to:
- Consolidate portfolio health across multiple Jira instances or projects
- Produce a cross-business-unit executive portfolio view
- Generate the quarterly or monthly board-level portfolio report
- Compare portfolio health across business units side by side
- Surface enterprise-level risks that span multiple portfolios

For a single-portfolio view, use portfolio-status.

---

## Data Sources [CUSTOMIZE]
Pull from all connected Jira instances and projects:

PRODUCT PORTFOLIO: [YOUR_PRODUCT_JIRA_PROJECTS]
PLATFORM PORTFOLIO: [YOUR_PLATFORM_JIRA_PROJECTS]
INFRASTRUCTURE PORTFOLIO: [YOUR_INFRA_JIRA_PROJECTS]
ADDITIONAL BU: [YOUR_ADDITIONAL_PROJECTS]

Also pull from:
- Slack [#YOUR_PORTFOLIO_UPDATES_CHANNEL] for qualitative signals this week
- Capacity model at [YOUR_CAPACITY_MODEL_PATH] for cross-team utilization

---

## Consistent Status Definitions Across All Business Units
Apply these definitions uniformly regardless of which BU or Jira instance the data comes from.

**ON TRACK**
- Velocity within 10% of four-sprint rolling average
- Delivery confidence rated 4 or 5 by owning team
- No unresolved blockers older than one sprint
- All known cross-team dependencies confirmed

**AT RISK** (any one condition)
- Velocity 10-30% below four-sprint average
- Delivery confidence rated 3
- Two or more unresolved blockers
- One unconfirmed dependency on a constrained team

**CRITICAL** (any one condition)
- Velocity more than 30% below average
- Delivery confidence rated 1 or 2
- Three or more unresolved blockers
- Hard dependency blocking delivery with no resolution path

**CROSS-PORTFOLIO RISK** (additional flag for enterprise view)
- An initiative in one portfolio has a dependency on a CRITICAL or AT RISK
  initiative in another portfolio
- Flag both initiatives and name the dependency explicitly

---

## Enterprise-Level Aggregation

**Portfolio Health Score per BU:**
For each business unit, calculate: percentage of epics On Track
Report as: X of Y epics On Track (Z%) — [STATUS]

**Enterprise Health Score:**
Aggregate across all BUs: total On Track / total active epics
Report as a single enterprise percentage with BU breakdown

**Cross-Portfolio Risk Map:**
Identify initiatives whose blockers or dependencies span portfolio boundaries.
These require Director-level visibility because no single portfolio owner
can resolve them unilaterally.

**Capacity Hotspots:**
Identify any team supporting multiple portfolios simultaneously whose
utilization exceeds 85%. Flag the portfolios dependent on that team.

---

## Output Structure

### Section 1: Enterprise Executive Summary
- Enterprise health score (single number)
- Health score by business unit (table)
- Top three enterprise-level risks requiring leadership attention
- Decisions needed at the leadership team level before next review

### Section 2: Portfolio Health by Business Unit
For each BU: health score, epic count by status, top At Risk and Critical items,
cross-portfolio dependency flags

### Section 3: Cross-Portfolio Risk Register
For each cross-portfolio dependency conflict:
- Initiative A (BU, status, risk)
- Depends on: Initiative B (BU, status, risk)
- Resolution owner: [who needs to make the call]
- Recommended action

### Section 4: Capacity Hotspot Report
For each team supporting multiple portfolios above 85% utilization:
- Team name, current utilization percentage
- Portfolios depending on this team
- Risk to each portfolio if team capacity is constrained further

### Section 5: Trend Line
This week vs. last week: enterprise health score change
Note any portfolios where health score dropped more than 10 points
Note any portfolios where health score improved more than 10 points

---

## Reporting Standards
- Lead with what CHANGED since last report, not current state description
- Name the owning team and portfolio for every At Risk and Critical epic
- Never use "challenges" — describe the specific issue
- Cross-portfolio risks get their own named section, not buried in BU detail
- Executive summary fits on one page when formatted

---

## Output Format
Format using template at: [CUSTOMIZE: /PMO/Templates/enterprise-portfolio-report.docx]
Save to: [CUSTOMIZE: /PMO/Reports/Enterprise/] with date in filename

For board-level reports, also generate a PowerPoint version using:
[CUSTOMIZE: /PMO/Templates/board-portfolio-review.pptx]

---

## Scheduling
Recommend running this Skill on the following cadence:
- Weekly: Sections 1, 2, and 3 only (15-minute read)
- Monthly: Full report all five sections
- Quarterly: Full report plus trend analysis comparing last three months
