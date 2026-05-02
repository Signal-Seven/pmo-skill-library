# PMO Skill Library — Starter Kit
### The Agentic PMO by @thesignal7

This repository contains fifteen Custom Skills for Claude that automate the
core functions of an enterprise PMO and portfolio management organization.

Each Skill is a folder containing a SKILL.md file. Upload to Claude via
Settings > Features > Skills, or place in `.claude/skills/` for Claude Code.

---

## Skill Directory

### Core PMO Skills (start here)

| Skill | Slash Command | What It Does |
|-------|---------------|--------------|
| intake-triage | `/intake-triage` | Classifies and scores all incoming initiative requests (balanced enterprise scoring) |
| portfolio-status | `/portfolio-status` | Classifies epics as On Track / At Risk / Critical for a single portfolio |
| goal-alignment | `/goal-alignment` | Scores portfolio contribution against organizational OKRs |
| capacity-planning | `/capacity-planning` | Generates rolling six-week capacity availability view by team |
| exec-comms | `/exec-comms` | Drafts executive communications and escalation memos |
| demand-loop | `/demand-loop` | Manages the autonomous weekly demand pipeline |
| continuous-planning | `/continuous-planning` | Runs the seven-stage continuous planning pipeline |
| intake-chat | `/intake-chat` | Conversational intake form replacing MS Forms / Jira intake |

### On-Demand Dashboard Skills

| Skill | Slash Command | What It Does |
|-------|---------------|--------------|
| portfolio-health-view | `/portfolio-health-view` | On-demand portfolio health dashboard |
| capacity-view | `/capacity-view` | On-demand capacity utilization view |
| okr-alignment-view | `/okr-alignment-view` | On-demand OKR contribution analysis |
| demand-funnel-view | `/demand-funnel-view` | On-demand intake demand trend view |

### Business Unit Variant Skills (for enterprise scaling)

| Skill | Slash Command | What It Does |
|-------|---------------|--------------|
| product-intake-triage | `/product-intake-triage` | Intake scoring weighted for product portfolios (revenue and customer impact 2x) |
| platform-intake-triage | `/platform-intake-triage` | Intake scoring weighted for platform portfolios (reliability and risk impact 2x) |
| enterprise-portfolio-status | `/enterprise-portfolio-status` | Consolidated portfolio health across multiple BUs, teams, and Jira instances |

---

## Quick Start Sequence

**Week 1:** `portfolio-status` + `intake-triage`
Connect Jira MCP. Run one portfolio synthesis task. Schedule the weekly report.

**Week 2-3:** `intake-triage` + `intake-chat`
Process five real intake requests. Deploy intake-chat as a shared Claude Project.

**Week 4:** `capacity-planning` + `goal-alignment`
Connect your Excel capacity model. Run your first trade-off analysis.

**Week 5:** `demand-loop`
Launch the Monday morning automation.

**Week 6:** All four dashboard Skills + `continuous-planning`

**Enterprise scaling:** Add `product-intake-triage`, `platform-intake-triage`,
and `enterprise-portfolio-status` once the core Skills are running.

---

## Enterprise Scaling

Skills are shared organization-wide on Claude Team and Enterprise plans.
Upload once as an admin and every TPM gets the same Skill immediately.
Update one SKILL.md and re-upload — the change propagates everywhere.

For multiple Jira instances, add each as a separate connector entry in your
MCP config. Portfolio queries reach all instances in a single pass.
See the MCP Connector Setup section below.

---

## Customizing Your Skills

Every SKILL.md contains `[CUSTOMIZE]` sections. Update these for your org:
- Project keys and Jira project names
- OKR definitions (goal-alignment, okr-alignment-view)
- File paths for templates and capacity models
- Scoring thresholds and trade-off flag levels
- Communication style and executive audience names
- Business unit names (enterprise-portfolio-status)

---

## MCP Connector Setup

Single Jira instance:
```json
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://mcp.atlassian.com/v1/mcp"]
    }
  }
}
```

Multiple Jira instances (enterprise multi-BU):
```json
{
  "mcpServers": {
    "jira-product": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://your-product-org.atlassian.com/v1/mcp"]
    },
    "jira-platform": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://your-platform-org.atlassian.com/v1/mcp"]
    },
    "slack": { "type": "http", "url": "https://mcp.slack.com/mcp" },
    "google-drive": { "type": "http", "url": "https://drivemcp.googleapis.com/mcp/v1" }
  }
}
```

Enterprise note: MCP connectors may require security review. The MCP
architecture supports private network configurations and IP allowlisting.
Engage your security team in Week 1.

---

## Full Implementation Guide

LinkedIn article and guide: @thesignal7 | thesignal.substack.com
Consultation hours: reach out via LinkedIn or The Signal

*Built by Trisha Townsend | @thesignal7 | May 2026*
