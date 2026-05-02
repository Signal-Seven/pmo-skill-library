---
name: intake-triage
description: Process incoming PMO initiative requests. Classifies into Strategic
  Initiative, Platform Investment, Change Request, or Operational Ask. Checks
  completeness of six required fields, scores five prioritization criteria (1-5
  each, max 25), and flags trade-off decisions when score is high but capacity
  is constrained. Use when evaluating any new initiative submission or triaging
  the intake queue.
---

# PMO Intake Triage Skill

## Classification Framework

**STRATEGIC INITIATIVE**
- Net-new investment not currently in any portfolio
- Requires cross-team coordination (2+ teams)
- Has confirmed executive sponsor (VP or above)
- Ties to one or more annual OKRs
- Estimated delivery greater than one quarter

**PLATFORM INVESTMENT**
- Technical infrastructure, tooling, or enablement work
- No direct revenue attribution but delivery-critical
- May be single-team but with broad organizational impact

**CHANGE REQUEST**
- Modification to scope, timeline, or resources of existing approved in-flight work
- Must reference an active epic or initiative by name or key

**OPERATIONAL ASK**
- Support, maintenance, or operational request
- Route directly to team-level backlog without PMO review

---

## Completeness Check
Mark each field: PRESENT / MISSING / UNCLEAR

1. Business owner (named individual, not a team)
2. Executive sponsor (VP or above, confirmed awareness)
3. Primary success metric with target value and measurement date
4. Engineering estimate (team-weeks or story points)
5. Target delivery quarter
6. Known dependencies with named owning teams (or "none identified")

If 2+ fields are MISSING: classify as INCOMPLETE and generate clarifying questions doc.
Save to [CUSTOMIZE: /PMO/Intake/Clarification/]

---

## Prioritization Scoring (1-5 each, document rationale per score)

**STRATEGIC ALIGNMENT**
5=directly required for named OKR | 4=strong OKR contribution | 3=supports direction
2=tangential | 1=no alignment

**REVENUE OR COST IMPACT**
5=quantified >$1M high confidence | 4=$250K-$1M | 3=moderate estimated
2=claimed unsubstantiated | 1=none articulated

**DELIVERY FEASIBILITY**
5=clearly scoped team available | 4=well-scoped minor unknowns | 3=reasonable scope capacity unclear
2=scope unclear OR capacity constrained | 1=undefined

**DEPENDENCY RISK (higher = lower risk)**
5=no dependencies or all confirmed | 4=minor confirmed | 3=some unconfirmed
2=significant unclear | 1=complex unresolved blockers

**TIME SENSITIVITY**
5=hard deadline (regulatory/contractual) | 4=strong market timing | 3=general urgency
2=preferred timing | 1=no dependency

---

## Trade-Off Flag
If score >= [CUSTOMIZE: 16] AND capacity < [CUSTOMIZE: 20%] in target quarter:
Flag TRADE-OFF REQUIRED. List top 3 active initiatives by score for comparison.

---

## Output Format
1. Request title and submitter
2. Classification with rationale
3. Completeness check (all six fields)
4. Scores with one-sentence rationale each
5. Total score out of 25
6. Trade-off flag (if applicable)
7. Recommended next action: ADVANCE / HOLD FOR CLARIFICATION / ROUTE TO TEAM
8. One-paragraph executive summary

---

## File Paths [CUSTOMIZE]
Submissions: /PMO/Intake/Submissions/
Processed: /PMO/Intake/Processed/
Clarification: /PMO/Intake/Clarification/
Template: /PMO/Templates/intake-review.docx
