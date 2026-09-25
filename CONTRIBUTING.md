# Contributing

Thanks for helping make coding agents better at UX.

## What helps most

- **Transcripts.** A request, the agent's answer with the skill, and what was right or wrong about it. Failures are as useful as wins.
- **Corrections.** A rule that is wrong, too broad, or missing a source. Link the source (WCAG, research, platform guidelines).
- **Gaps.** A situation the skill handles badly, such as a pattern, a state, or a type of product it does not cover.
- **Install notes** for agents the README does not list.

## Before you change the skill

- Keep `SKILL.md` short. Detailed rules go in `references/`, which the agent opens only when a feature needs them.
- Write rules an agent can act on. "Specify what survives a refresh" is actionable. "Make it intuitive" is not.
- State the condition a rule applies under. Rules without limits get applied everywhere.
- Do not add a principle unless it changes a decision.
- Cite WCAG criteria by number and link to the W3C page.
- Never add rules that manipulate users: fake urgency, hidden alternatives, attention traps.

## Pull requests

1. Open an issue first for large changes, so we can agree on the direction.
2. Keep one topic per pull request.
3. Show the effect: include a before-and-after answer for the same request when you change behavior.
4. Run the checks locally:

   ```bash
   python3 scripts/validate.py
   ```

5. Add a line to [CHANGELOG.md](CHANGELOG.md) under "Unreleased".

## Repository layout

```text
skills/<skill-name>/SKILL.md      # One folder per skill; `name` in frontmatter matches the folder
skills/<skill-name>/references/   # Loaded on demand
.claude-plugin/                   # Claude Code plugin and marketplace manifests
scripts/validate.py               # Frontmatter and link checks, run in CI
```

By contributing, you agree that your contribution is licensed under the MIT License.
