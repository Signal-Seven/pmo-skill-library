# PMO Skill Library — Starter Kit
### The Agentic PMO by @Signal-Seven

This repository contains twelve Custom Skills for Claude that automate the
core functions of an enterprise PMO and portfolio management organization.

Each Skill is a folder containing a SKILL.md file. Upload to Claude via
Settings > Features > Skills, or place in `.claude/skills/` for Claude Code.

---

## Skill Directory

| Skill | Slash Command | What It Does |
|-------|---------------|--------------|
| intake-triage | `/intake-triage` | Classifies, scores, and triages intake requests |
| portfolio-status | `/portfolio-status` | Classifies epics as On Track / At Risk / Critical |
| goal-alignment | `/goal-alignment` | Scores portfolio contribution against OKRs |
| capacity-planning | `/capacity-planning` | Generates rolling capacity availability view |
| exec-comms | `/exec-comms` | Drafts executive communications and escalation memos |
| demand-loop | `/demand-loop` | Manages the autonomous weekly demand pipeline |
| continuous-planning | `/continuous-planning` | Runs the 7-stage continuous planning pipeline |
| portfolio-health-view | `/portfolio-health-view` | On-demand portfolio health dashboard |
| capacity-view | `/capacity-view` | On-demand capacity utilization view |
| okr-alignment-view | `/okr-alignment-view` | On-demand OKR contribution analysis |
| demand-funnel-view | `/demand-funnel-view` | On-demand intake demand trend view |
| intake-chat | `/intake-chat` | Conversational intake form (replaces MS Forms / Jira intake) |

---

## Quick Start

**Week 1:** Install `intake-triage` and `portfolio-status`. Connect Jira MCP.
Run your first portfolio synthesis task and refine against your own standard.

**Week 2:** Schedule the weekly status report via Cowork using `portfolio-status`.
Run in parallel with your manual process for two weeks.

**Week 3:** Activate `intake-triage`. Run five real intake requests through it.
Add `goal-alignment` and `capacity-planning`.

**Week 4:** Configure `demand-loop` for Monday morning automation.

**Week 5-6:** Add the four on-demand dashboard Skills. Set up `continuous-planning`
for your six-week review cadence.

---

## Required MCP Connectors
- Jira (Atlassian MCP) — portfolio-status, intake-triage, all dashboard views
- Slack — demand-loop, intake-chat
- Google Drive — continuous-planning, exec-comms
- Google Sheets / Excel — capacity-planning, capacity-view

Configure in Claude Settings > Connectors or in `.claude/mcp.json` for Claude Code.

---

## Customization

Each SKILL.md contains sections marked `[CUSTOMIZE]`. Update these for your org:
- Project keys and Jira project names
- OKR definitions (goal-alignment, okr-alignment-view)
- File paths for templates and capacity models
- Scoring thresholds and escalation rules
- Communication style and executive names

---

## Full Implementation Guide
Read the companion guide: *The Agentic PMO: A Practitioner's Guide*
Available at thesignal.substack.com | @thesignal7

---

## License
MIT — use it, fork it, adapt it for your org. If it saves you an afternoon,
let me know. If it breaks something, open an issue.

## Contributing
This is a starter kit, not a finished product. PRs welcome — especially
new dashboard skills, additional MCP connector configurations, and
real-world `[CUSTOMIZE]` examples from PMOs that have run this in production.
