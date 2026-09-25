<div align="center">

# Good UX Skills

**Your coding agent builds the button. This skill makes it design the experience.**

An agent skill that turns a feature request into a UX plan a developer can build, and reviews existing screens when you ask for an evaluation.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ayushd03/good-ux-skills?style=social)](https://github.com/ayushd03/good-ux-skills/stargazers)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-8A2BE2)](https://agentskills.io)
[![WCAG 2.2 AA](https://img.shields.io/badge/WCAG-2.2_AA-green)](https://www.w3.org/TR/WCAG22/)

Works with **Claude Code** · **Cursor** · **Codex** · **Gemini CLI** · **GitHub Copilot** · **OpenCode** · and any agent that reads `SKILL.md`

</div>

---

## Why

Ask a coding agent to "add export" and you get an Export button and a success toast. Nobody asked what the export is for. Nothing says what happens on a double click, a timeout, or a permission change. The empty state, the error copy, and keyboard access are left to chance.

Good UX Skills changes how the agent works before it writes code:

- **Need before screens.** It checks the problem, the current workaround, and whether a smaller change would do.
- **No fake research.** Every material decision is labeled as a requester requirement, a reported need, observed behavior, or an assumption.
- **Every state, not just the happy path.** Loading, empty, partial, failure, offline, permission loss, and timeouts where the server may have succeeded.
- **Accessibility that is easy to miss.** WCAG 2.2 AA criteria for what the UI actually contains, such as target size, reflow, focus, and status messages.
- **A way to know it worked.** An outcome metric with a baseline, and a usability test for risky assumptions, clearly marked as proposed or completed.

## Before and after

**Request:** *"Add a way to export invoices."*

| Without the skill | With the skill |
| --- | --- |
| Adds an Export button | Asks what the export is for (reconciling rows in a spreadsheet) and labels the answer a requester requirement, not research |
| Picks a format at random | Picks CSV of the filtered rows, because that serves the stated need |
| Shows a success toast | Specifies the second click, a timeout, a filter change mid-export, and losing permission mid-task |
| Stops at "done" | Measures CSV responses, export errors, and related support tickets against a baseline |
| Calls it validated | Proposes a usability test, and says what that test would not prove |

The full worked example is at the end of [`SKILL.md`](skills/good-ux-skills/SKILL.md#worked-example).

## Install

### Any agent, with the skills CLI

```bash
npx skills add ayushd03/good-ux-skills
```

The [skills CLI](https://skills.sh) installs into Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, OpenCode, and other supported agents.

### Claude Code plugin

```text
/plugin marketplace add ayushd03/good-ux-skills
/plugin install good-ux-skills@good-ux-skills
```

### Manual

Clone the repository, then copy the skill folder into your agent's skills directory:

```bash
git clone https://github.com/ayushd03/good-ux-skills.git
cp -r good-ux-skills/skills/good-ux-skills ~/.claude/skills/    # Claude Code
cp -r good-ux-skills/skills/good-ux-skills ~/.cursor/skills/    # Cursor
cp -r good-ux-skills/skills/good-ux-skills ~/.agents/skills/    # Codex
```

Use a project's `.claude/skills/` (or the equivalent) to install it for one project only.

### Other agents

Point your rules file (`AGENTS.md`, `.cursorrules`, `GEMINI.md`, and so on) at [`skills/good-ux-skills/SKILL.md`](skills/good-ux-skills/SKILL.md). Tell the agent to open the files in `references/` only when a feature needs them.

## Use it

The skill triggers on UX work. You can also call it directly, for example with `/good-ux-skills` in Claude Code.

- *"Plan the UX for exporting invoices."*
- *"Design the flow for inviting a teammate to a workspace."*
- *"Review this checkout screen for usability."*
- *"What happens in this form when the session expires?"*

## What you get

**A plan** for a request to build or change something. It includes the sections the feature needs and drops the rest:

1. Problem, and what is in and out of scope
2. Evidence and assumptions, each labeled by source
3. Context and constraints
4. Alternatives, when the choice is uncertain
5. Flows
6. Surfaces
7. States
8. Layout, accessibility, privacy, and locale
9. Reuse
10. Measurement
11. Validation
12. Build order and acceptance checks

**A review** for a request to evaluate. Each issue names the user and task, the finding, the evidence, the severity, one concrete change, and how to verify it. Issues that block the task come first.

## What's inside

```text
good-ux-skills/
├── skills/
│   └── good-ux-skills/
│       ├── SKILL.md              # Workflow: plan or review, evidence rules, plan format, worked example
│       └── references/
│           ├── principles.md     # Psychology and response time, with the limits of each principle
│           └── behavior.md       # Forms, patterns, undo, async work, persistence, permissions, privacy, AI
└── .claude-plugin/               # Claude Code plugin and marketplace manifests
```

The agent reads `SKILL.md` first. It opens a reference file only when the feature needs that topic, so the skill stays light on context.

## Principles behind the skill

- **Psychology only when it changes a decision.** No Hick's law pasted onto every label.
- **Rare harm beats common annoyance.** Data loss, lockout, and accidental disclosure are not deferred by an 80/20 split.
- **Specified, implemented, and validated are different claims.** An accessible component is not an accessible flow. A written test plan is not a completed test.
- **No dark patterns.** The skill will not help trap attention, fake urgency, or hide alternatives.

## Contributing

Contributions are welcome, especially:

- Before-and-after transcripts that show the skill helping, or failing
- Rules that are wrong, too vague, or missing a source
- Install instructions for agents not listed here

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Star history

If the skill improved something you shipped, a star helps other developers find it.

[![Star History Chart](https://api.star-history.com/svg?repos=ayushd03/good-ux-skills&type=Date)](https://star-history.com/#ayushd03/good-ux-skills&Date)

## License

MIT. See [LICENSE](LICENSE).
