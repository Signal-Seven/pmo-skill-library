---
name: product-intake-triage
description: Process incoming initiative requests specifically for a product portfolio.
  Weighted toward revenue impact, customer outcomes, market timing, and product OKR
  contribution. Use when evaluating new feature requests, product investments, or
  go-to-market initiatives submitted to the product PMO or portfolio team. Different
  from intake-triage which uses a balanced enterprise score. This Skill weights
  revenue and customer impact more heavily for product decisions.
---

# Product Portfolio Intake Triage Skill

## When to Use This Skill
Use this Skill when the intake request is:
- A new product feature or capability
- A go-to-market initiative tied to a product release
- A customer-facing integration or partnership
- A product experience or UX improvement
- A monetization or pricing change

For platform or infrastructure requests, use platform-intake-triage.
For enterprise-wide strategic initiatives, use intake-triage.

---

## Classification Framework

**PRODUCT INITIATIVE (STRATEGIC)**
- Net-new capability that directly drives revenue, retention, or acquisition
- Tied to a product OKR or a committed customer promise
- Requires cross-functional coordination (Product, Engineering, Design, GTM)
- Delivery timeline greater than one quarter

**PRODUCT INITIATIVE (ENHANCEMENT)**
- Improvement to an existing product capability
- Customer-requested or NPS-driven
- Primarily single-team delivery
- Delivery timeline one quarter or less

**GO-TO-MARKET REQUEST**
- Launch enablement, pricing change, packaging, or positioning work
- Requires product readiness but driven by Sales, Marketing, or Partnerships
- Must reference a product initiative it supports

**CUSTOMER COMMITMENT**
- Explicitly promised to a named customer or customer segment
- Has a contractual or renewal implication
- Escalated handling: flag immediately regardless of score

---

## Completeness Check
Mark each field: PRESENT / MISSING / UNCLEAR

Required fields:
1. Product owner (named individual, not a team)
2. Executive sponsor or product leader sign-off (Director or above)
3. Customer or market problem being solved (one sentence, specific)
4. Primary success metric with target value and measurement date
5. Engineering estimate (team-weeks or story points)
6. Target delivery quarter and any hard market or launch deadlines
7. Known dependencies (design, data, platform, GTM)

If 2 or more fields are MISSING:
- Classify as INCOMPLETE
- Generate a clarifying questions document
- Save to [CUSTOMIZE: /PMO/Intake/Product/Clarification/]

---

## Prioritization Scoring
Score each criterion from 1 (low) to 5 (high).
Document your rationale in one sentence per criterion.

**REVENUE AND CUSTOMER IMPACT (1-5) — weighted 2x**
This criterion counts double in the total score for product intakes.
5: Quantified revenue impact >$1M or direct retention of >100 accounts
4: Quantified impact $250K-$1M or material churn risk reduction
3: Moderate impact estimated with reasonable methodology
2: Impact claimed but methodology unclear or unsubstantiated
1: No financial or customer impact articulated

**PRODUCT STRATEGIC ALIGNMENT (1-5)**
5: Directly required for a named product OKR this quarter
4: Strong contribution to product direction, OKR-adjacent
3: Consistent with product strategy but not tied to a named OKR
2: Tangential to current product priorities
1: No discernible alignment to current product strategy

**DELIVERY FEASIBILITY (1-5)**
5: Clearly scoped, design ready, engineering team available
4: Well-scoped with minor unknowns, team likely available
3: Reasonably scoped but design or capacity unclear
2: Scope unclear OR team capacity definitely constrained this quarter
1: Undefined scope AND no team capacity

**MARKET AND TIMING (1-5)**
5: Hard market deadline (competitor launch, regulatory, renewal date)
4: Strong market window with evidence (competitive pressure, seasonal)
3: Timing preference with reasonable business rationale
2: Preferred timing but no external driver
1: No timing dependency

**DEPENDENCY RISK (1-5, higher = lower risk)**
5: No cross-team dependencies or all confirmed
4: Minor dependencies, owning teams confirmed
3: Some dependencies identified, not yet confirmed
2: Significant dependencies with unclear ownership
1: Complex unresolved dependencies across multiple teams

---

## Product Score Calculation
Standard score: sum of all five criteria (max 25 before weighting)
Revenue-weighted score: add the Revenue and Customer Impact score
one additional time (this criterion scores twice)
Maximum weighted score: 30

Report both scores in the output.

---

## Trade-Off Flag
If weighted score >= [CUSTOMIZE: 20] AND capacity model shows
< [CUSTOMIZE: 20%] product team availability in target quarter:
Flag as TRADE-OFF REQUIRED
List top three currently active product initiatives for comparison.

If classification is CUSTOMER COMMITMENT:
Flag immediately for Director review regardless of score or capacity.

---

## Output Format
1. Request title and submitter
2. Classification with one-sentence rationale
3. Completeness check (all seven required fields)
4. Standard score (max 25) and weighted score (max 30) with rationale per criterion
5. Trade-off flag if applicable, with top three active initiatives listed
6. Customer commitment flag if applicable
7. Recommended next action:
   - ADVANCE TO CAPACITY CHECK
   - HOLD FOR CLARIFICATION (list specific missing fields)
   - CUSTOMER COMMITMENT ESCALATION (immediate Director review)
   - ROUTE TO ENHANCEMENT BACKLOG (for low-scoring enhancements)
8. One-paragraph executive summary written for a product leader audience

---

## Output Tone
Write the executive summary as if presenting to a CPO or VP of Product.
Lead with the customer or market problem, then the solution, then the business case.
Avoid engineering-first framing. Lead with outcomes, not implementation.

---

## File Paths [CUSTOMIZE]
Submissions: /PMO/Intake/Product/Submissions/
Processed: /PMO/Intake/Product/Processed/
Clarification: /PMO/Intake/Product/Clarification/
Template: /PMO/Templates/product-intake-summary.docx
