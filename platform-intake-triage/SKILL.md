---
name: platform-intake-triage
description: Process incoming initiative requests specifically for a platform or
  infrastructure portfolio. Weighted toward dependency impact, reliability outcomes,
  developer experience, and technical debt reduction. Use when evaluating infrastructure
  investments, platform enablement work, technical debt initiatives, or internal
  tooling requests submitted to the platform PMO or portfolio team.
---

# Platform Portfolio Intake Triage Skill

## When to Use This Skill
Use this Skill when the intake request is:
- Infrastructure investment or cloud architecture work
- Platform capability or internal API development
- Developer tooling or developer experience improvement
- Technical debt or system reliability initiative
- Security, compliance, or observability work
- Shared services or enablement for other teams

For product feature requests, use product-intake-triage.
For enterprise-wide strategic initiatives, use intake-triage.

---

## Classification Framework

**PLATFORM INITIATIVE (STRATEGIC)**
- Net-new platform capability enabling multiple consuming teams
- Tied to a reliability, velocity, or cost OKR
- Has clear engineering owner and consuming team buy-in
- Delivery timeline greater than one quarter

**RELIABILITY AND RESILIENCE**
- Work that directly improves uptime, incident response, or failure recovery
- Has a named SLA or uptime target it addresses
- Escalated handling: flag for Director review immediately if P1-level risk

**TECHNICAL DEBT REDUCTION**
- Removal or refactor of existing system risk
- Must quantify the ongoing cost of not addressing (engineering hours, incident rate)
- Not eligible for Strategic classification without that quantification

**DEVELOPER EXPERIENCE**
- Tooling, workflow, or process improvement for internal engineering teams
- Has a named set of consuming teams and an adoption metric
- Delivery timeline one quarter or less

**COMPLIANCE AND SECURITY**
- Regulatory, audit, or security mandate
- Has a deadline driven by an external requirement
- Escalated handling: flag for Director review regardless of score

---

## Completeness Check
Mark each field: PRESENT / MISSING / UNCLEAR

Required fields:
1. Technical owner (named individual, not a team)
2. Engineering sponsor (Staff Engineer, Principal, or Engineering Director)
3. Consuming teams (who benefits from this work and has confirmed awareness)
4. Current state problem (what breaks, degrades, or slows without this)
5. Engineering estimate (team-weeks or story points)
6. Target delivery quarter and any compliance or reliability deadlines
7. Known dependencies on other platform components or external services

If 2 or more fields are MISSING:
- Classify as INCOMPLETE
- Generate a clarifying questions document
- Save to [CUSTOMIZE: /PMO/Intake/Platform/Clarification/]

---

## Prioritization Scoring
Score each criterion from 1 (low) to 5 (high).
Document your rationale in one sentence per criterion.

**RELIABILITY AND RISK IMPACT (1-5) — weighted 2x**
This criterion counts double for platform intakes.
5: Active P1 risk or incident pattern with quantified blast radius
4: Known fragility with documented near-misses or degradation events
3: Risk identified but not yet materialized, moderate blast radius
2: Theoretical risk with limited supporting evidence
1: No reliability or risk impact articulated

**DEVELOPER AND TEAM VELOCITY IMPACT (1-5)**
5: Directly unblocks 3+ teams or eliminates a recurring bottleneck
4: Meaningful velocity improvement for 2+ teams with evidence
3: Moderate improvement for one team with plausible spillover
2: Marginal improvement, limited consuming team impact
1: No measurable velocity impact

**PLATFORM STRATEGIC ALIGNMENT (1-5)**
5: Directly required for a named platform or reliability OKR
4: Strong contribution to platform direction, OKR-adjacent
3: Consistent with platform strategy but not tied to a named OKR
2: Tangential to current platform priorities
1: No alignment to current platform strategy

**DELIVERY FEASIBILITY (1-5)**
5: Clearly scoped, dependencies mapped, team capacity available
4: Well-scoped with minor unknowns, team likely available
3: Reasonably scoped but capacity or architecture decisions unclear
2: Scope unclear OR team capacity definitely constrained this quarter
1: Undefined scope AND no team capacity

**COMPLIANCE OR EXTERNAL DEADLINE (1-5)**
5: Hard external deadline (audit, regulatory, security mandate)
4: Strong internal deadline with documented consequence of missing
3: Preferred timing with reasonable business rationale
2: General urgency but no external driver
1: No timing dependency

---

## Platform Score Calculation
Standard score: sum of all five criteria (max 25 before weighting)
Reliability-weighted score: add the Reliability and Risk Impact score
one additional time (this criterion scores twice)
Maximum weighted score: 30

Report both scores in the output.

---

## Escalation Flags
RELIABILITY ESCALATION: If Reliability and Risk Impact score is 5 AND
any active incident is referenced, flag immediately for Director review.

COMPLIANCE ESCALATION: If classification is Compliance and Security,
flag immediately for Director review regardless of score or capacity.

TRADE-OFF FLAG: If weighted score >= [CUSTOMIZE: 20] AND platform team
capacity < [CUSTOMIZE: 20%] in target quarter, flag for Director trade-off
decision with top three active platform initiatives listed.

---

## Output Format
1. Request title and submitter
2. Classification with one-sentence rationale
3. Completeness check (all seven required fields)
4. Standard score (max 25) and weighted score (max 30) with rationale per criterion
5. Escalation flags if applicable
6. Trade-off flag if applicable with comparison list
7. Recommended next action:
   - ADVANCE TO CAPACITY CHECK
   - HOLD FOR CLARIFICATION (list specific missing fields)
   - RELIABILITY ESCALATION (immediate Director review)
   - COMPLIANCE ESCALATION (immediate Director review)
   - ROUTE TO TECH DEBT BACKLOG
8. One-paragraph executive summary written for an Engineering Director or VP audience

---

## Output Tone
Write the executive summary as if presenting to a VP of Engineering or CTO.
Lead with the reliability or velocity problem, then the solution, then the risk
of not addressing it. Be specific about blast radius and affected teams.
Avoid business-outcome-first framing. Lead with system impact.

---

## File Paths [CUSTOMIZE]
Submissions: /PMO/Intake/Platform/Submissions/
Processed: /PMO/Intake/Platform/Processed/
Clarification: /PMO/Intake/Platform/Clarification/
Template: /PMO/Templates/platform-intake-summary.docx
