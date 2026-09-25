---
name: good-ux-skills
description: >-
  Turn a feature or product request into an implementable UX plan, and review
  an experience when asked to evaluate it. It asks for evidence of the user
  need, circumstances of use, validation of risky assumptions, and a way to
  measure the outcome. Covers flows, states, recovery, accessibility, and
  psychology used only when it changes a decision. Use when designing UI,
  planning a feature, reviewing screens, writing flows, forms, navigation, or
  when the user mentions UX, usability, or good UX.
license: MIT
---

# Good UX Skills

Turn a request to create or change an experience into a UX plan a developer can build. When the user asks to evaluate an existing experience, review it. Do not use these rules to trap attention, disguise ads, fake urgency, manufacture incompleteness, or hide alternatives someone would have chosen if they were visible.

Pick the job from what the requester asks for. How complete the request is, and whether screens already exist, do not decide it.

- **Plan**: they want something created or changed, including a redesign. Follow "From request to plan".
- **Review**: they want an evaluation and no build. Follow "Review an existing screen".

Open a reference only when the feature needs it. Do not paste a principle onto every decision.

- [principles.md](references/principles.md): psychology, response time, onboarding, prioritization boundaries
- [behavior.md](references/behavior.md): forms, findability, patterns, undo, unconfirmed async work, persistence, scale, localization, privacy, permissions, notifications, AI

## From request to plan

Do not jump to screens. If the solution is still open, understand the need before picking a feature. If the feature is already settled, keep it and specify it.

1. **Check the problem.** Name the unmet need, the current workaround, and what makes the task hard. If the solution is still open, ask whether a change to an existing flow, the content, or a default would remove the need for a new feature.
2. **Gather evidence.** Implementation and users. Label material decisions as a requester requirement, a reported need, observed behavior, or an assumption. A small change inside an established pattern reuses that context; do not relabel routine choices.
3. **Learn the circumstances of use.** How the work is actually done, not only who the persona is.
4. **Ask about unknowns that matter.** Ask only what would change the design. Assume the rest and say so.
5. **Compare alternatives** when the approach is uncertain or consequential. Then commit, with a reason.
6. **Map the path and specify behavior.** Flows, surfaces, states. Use [behavior.md](references/behavior.md) for the topics that apply.
7. **Plan the measurement and the test.** Say how you will measure success after release, and how you will test risky assumptions before it.
8. **Write the plan** in the "Plan format" section. Drop sections the feature does not need. Do not write "N/A" under every heading.
9. **Check** "Is this worth building this way?" then "Is this implementable?".

Keep three statuses separate: **specified** (this plan), **implemented** (the build matches the spec), **validated** (evidence supported a named claim for a named audience under named conditions). A completed test records the outcome as **supported, contradicted, or inconclusive**. Only **supported** is validated, and only within those limits. An accessible component is not an accessible flow. A written scenario is not a completed test.

## Problem before solution

State:

- The unmet need, in the user's words if you have them.
- How they get the outcome today, including workarounds.
- What causes the difficulty (missing information, too many steps, the wrong object, a default, fear of a mistake).

If the solution is still open, record the need and prefer a smaller change to an existing flow, the content, or a default when that would meet it. If the requester already settled the feature, keep that choice in scope. Flag a concern, and compare alternatives only inside the authorized scope. Do not silently replace the request. State what is in scope and what is out.

## Evidence, not only the codebase

Look at the product before asking the developer to explain it: docs, pages, components, tokens, routes, similar features. Reuse a pattern unless it is the usability problem; if you replace it, say what was wrong.

Also look for evidence about users, when it exists: research notes, support complaints, search logs, analytics, session notes, and workarounds visible in the product. For each material decision, say which kind it is:

- **Requester requirement** — what the person asking for the work decided. They may not be an end user, and they may not be reporting research.
- **Reported need** — someone described what users do or want. Secondhand unless the source is named.
- **Observed behavior** — research, logs, analytics, or a session you can point at.
- **Assumption** — none of the above. Mandatory constraints (security, law, platform) are constraints, not hypotheses.

Never invent research, quotes, baselines, business rules, or metrics. If none of those sources are in the repo or the brief, say so.

When nothing exists yet, do not invent a component library. Establish audience, what they must understand before they act, content, page structure, actions, brand constraints, and the first conventions this product will repeat. For a content site, say what a visitor must grasp on each page before the action.

## Circumstances of use

"Who uses this?" is not enough. When it would change the design, establish:

- How often they do the task, and how well they already know the domain.
- Urgency, interruption, and whether they will return mid-task.
- Device, connectivity, and language proficiency.
- Whether they act for themselves or for someone else.

A hurried occasional user and an expert repeating the task may need different density, help, and confirmation. Say which circumstance the plan is for.

## Missing information

- **Changes the design** — the need, who may act, whether an action destroys or discloses data, which flow it joins. One focused question per gap.
- **Does not** — copy tone that can match clear existing language, field order that matches a sibling form. Assume it and label the assumption.
- **Capabilities.** Label each one the design depends on:
  - **Verified**: it exists. Rely on it.
  - **Proposed requirement**: it does not exist, nothing shows it is forbidden, and the experience needs it. Specify the user-facing behavior and name what engineering must build. Needing new work does not, by itself, make the UX provisional.
  - **Unknown feasibility**: a constraint might make the approach impossible, and you cannot tell.
- **Provisional sections.** An open question can change the UX materially: permissions, data loss, the core task, or unknown feasibility. It leaves the affected sections **provisional**. Other sections stay **ready to build**.

## Compare alternatives

For an uncertain or consequential choice, briefly compare the plausible approaches on discoverability, effort, error risk, accessibility, and implementation constraints. Record why the chosen one fits this task. Do not cite a principle on every label.

Defaults to test, not rules:

- Frequent work often keeps its controls on the task surface. Stages help when one screen mixes unrelated decisions.
- Experts often want density and stable placement. They also benefit when rare options are quiet.
- An irreversible or costly action explains the object, the scope, and the consequence. A generic "Are you sure?" does not.
- Match this product first, then common patterns, unless the pattern is the problem.

Pattern choice (page, modal, drawer, inline edit, wizard, direct manipulation), findability, forms, and undo depth: [behavior.md](references/behavior.md).

## Prioritize by harm and frequency

Frequency is one input. Also score:

- **Severity** — lockout, data loss, accidental disclosure, money, inaccessible recovery.
- **Reach** — how many people, and which segment.
- **Recoverability** — undo, support, or none.
- **Evidence confidence** — observed, inferred, or guessed.

A rare failure can outrank a common annoyance. Do not use an 80/20 split to defer those. Details and the boundary on Pareto-style reasoning: [principles.md](references/principles.md).

## Map the path

For anything larger than one control, specify discovery and entry, prerequisites, role, the main task, alternatives, leave and return, and handoffs. One completing action is enough only when the feature is one control on an existing screen.

Where relevant, the plan must also say what survives Back, refresh, closing the tab, session expiry, and another device. Draft lifetime, autosave, and whether cancel dismisses the UI or cancels the operation are in [behavior.md](references/behavior.md). So are notifications, handoffs, collaboration, and large collections.

## Specify each surface

For every page, section, or dialog in scope, specify:

- Purpose and entry conditions.
- Information, in hierarchy order.
- Primary and secondary actions.
- Fields: label, purpose, default, required, validation, and error text.
- Copy, where the wording changes the decision.
- What each action does and where it leads.

Controls must look interactive. Names of objects, navigation labels, and current location must match what users call them. If existing product language is unclear, do not copy it. Plain language, action labels, and errors that state what happened, what is safe, and the next step: [behavior.md](references/behavior.md).

## Layout and input

Specify the behaviors that apply, not a generic "make it responsive":

- What stacks, what scrolls, and what stays fixed.
- How a wide table behaves at a narrow width: stacked rows, horizontal scroll with a pinned column, or fewer columns.
- Pointer targets: at least **24 × 24 CSS pixels**, or a documented exception under [WCAG 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).
- **2.1.1 Keyboard:** the task can be completed from the keyboard, not only reached. **2.1.2** is a separate requirement: focus can leave the component. Being able to leave a component is not the same as being able to operate it.

## States and recovery

Check which of these can occur, and specify each one that can: initial, loading, empty, success, validation failure, system failure, unavailable or offline, partial data, and permission restrictions. Then, for each, state trigger, feedback, remaining actions (including a second click), data kept or frozen, and the next state.

Separate three timescales. Immediate input feedback is on the order of a tenth of a second. An operation can take around a second before it interrupts thought. Longer work needs honest status and a way to wait or leave. Show real progress when it is measurable. Do not add delay to make work look careful. Thresholds: [principles.md](references/principles.md).

Add transaction safeguards only when repeating the action can double-charge, double-send, or double-write. A routine download that returns the same file again does not need them. If a request can time out after the server may have succeeded, the UI says the outcome is unconfirmed, not failed. Disabling the button is feedback, not protection. Full rules: [behavior.md](references/behavior.md).

## Accessibility: easy-to-miss criteria

Target **WCAG 2.2 Level AA** unless the product names a stricter target. The items below are easy to miss in a plan. They are not a complete conformance checklist. For anything this list does not cover, use the criterion that matches the UI in the [WCAG 2.2 specification](https://www.w3.org/TR/WCAG22/).

Specify the behavior, or name the existing component whose behavior you rely on, for the criteria that apply:

- **1.1.1** text alternatives. **1.3.1** semantic relationships, not only visual grouping. **1.3.2** reading order. **4.1.3** status messages.
- **1.4.3** text contrast 4.5:1, large text 3:1. **1.4.11** non-text contrast 3:1. **1.4.4** resize text. **1.4.12** text spacing.
- **1.4.10 Reflow.** Vertical content at a width of **320 CSS pixels**. Horizontal content at a height of **256 CSS pixels**. Two-dimensional exceptions (maps, diagrams, video, games, data tables) may scroll on two axes; the rest of the page reflows.
- **2.1.2** no keyboard trap. **2.4.7** visible focus. **2.4.11** focus not obscured. **2.5.7** a single-pointer alternative to dragging.
- **4.1.2 Name, Role, Value** — name, role, and state, not the name alone.
- **3.3.1** errors identify the field and what is wrong. **3.3.8** accessible authentication when signing in.
- **Motion.** Honor `prefers-reduced-motion` at every target, so nobody needs interaction animation to understand or operate the UI. **2.2.2** covers content that moves on its own. **2.3.3** is AAA, so AA does not require it. Still honor reduced motion at AA. It being a W3C technique for an AAA criterion is not a reason to skip it.

After implementation, test in proportion to the risk:

- Keyboard through the whole flow.
- At least one assistive-technology pass on custom widgets.
- Zoom and reflow.
- Realistic text.
- A relevant device.

Record **specified**, **implemented**, and the test outcome, as defined in "From request to plan". A screenshot does not show keyboard behavior, latency, or screen-reader output.

## Measure the outcome

For anything beyond a trivial fix, define what will show the need was met. Prefer task completion, errors, abandonment, effort (time or steps), or support demand. Include a baseline when one exists, the segment, the event or research method that captures it, and when to look. Do not treat clicks or engagement as success unless that is the actual goal. Pair the number with what you will investigate if it moves the wrong way.

## Validation loop

Use this when the design is uncertain or the cost of being wrong is high (data loss, money, access, a new pattern). Skip it for a label that matches an established control.

- **Riskiest assumption** — one sentence.
- **Prototype** — the cheapest artifact that can falsify it (copy, paper, coded slice).
- **Participants** — people who match the circumstance, not the team.
- **Tasks** — neutral. Do not walk them through the control you hope they find.
- **Observe** — what they do, where they hesitate, what they think the result is.
- **Revise when** — a stated observation, not "if they dislike it".

Label the block **proposed** or **completed**. For a completed test, name the claim, the audience, the conditions, and the outcome. The status rules in "From request to plan" decide whether it counts as validated. Do not describe a test you did not run. Feed a completed test back into the problem statement before locking the plan.

## Plan format

1. **Problem** — unmet need, workaround, and cause of difficulty. In scope and out of scope. If the solution was open, why this approach rather than a smaller change. If the feature was already settled, the concern you flagged, without replacing the request.
2. **Evidence and assumptions** — source for each material decision only: requester requirement, reported need, observed behavior, or assumption. Circumstances of use when they change the design.
3. **Context** — existing UI and constraints, or from-scratch conventions. Verified capabilities, proposed requirements, unknown feasibility. Provisional sections named.
4. **Alternatives** — only if the choice was uncertain or consequential.
5. **Flows** — entry, main path, alternatives, persistence, roles, handoffs.
6. **Surfaces** — one block per page, section, or dialog.
7. **States** — including unconfirmed async outcomes when the operation can succeed after a timeout.
8. **Layout, accessibility, privacy, locale** — stacking, scrolling, fixed regions, narrow tables, and target size when they apply. WCAG criteria for what the UI actually contains, not a claim of full conformance. Where sensitive data can appear or be copied.
9. **Reuse** — components to use, and what is new.
10. **Measurement** — outcome, baseline, segment, instrumentation, review point.
11. **Validation** — proposed or completed, in the loop above.
12. **Build order and acceptance** — observable checks. Required versus optional. No "intuitive" or "seamless".

## Is this worth building this way?

- The need is stated separately from the requested feature.
- Evidence and assumptions are labeled. Nothing is dressed up as research.
- A smaller change was considered only when the solution was open. A settled feature stayed in scope.
- Harmful rare cases are not dropped because they are rare.

## Is this implementable?

- A developer can build each ready section without guessing a significant branch.
- Every action has an outcome. Failures have recovery. A consequential action does not offer a blind retry after an unconfirmed success. A harmless repeat says so.
- Leave, return, and cancel have a defined effect when the task has state.
- The plan fits verified constraints. Unbuilt capabilities are proposed requirements.

## Review an existing screen

1. Name the user, the task, and the paths, not only one button.
2. Inspect flows, states, recovery, practical requirements, and WCAG criteria that apply. Use [principles.md](references/principles.md) only when a principle changes a decision.
3. Prefer the smallest change that removes the observed friction.

Report each issue as:

- **Who and task**
- **Finding** — demonstrated or hypothesis. A screenshot cannot establish keyboard behavior, latency, or screen-reader support.
- **Evidence** — what you observed, and what you could not check
- **Severity** — harm, reach, recoverability
- **Change** — one concrete UI change
- **How to verify** — the check that would show the change worked

Lead with what blocks the task or causes serious harm.

## Worked example

**Request:** "Add a way to export invoices."

**Problem check.** The feature is a settled request: export stays in scope. Out of scope: scheduling, PDF, email. Asked what the export is for. The requester answered: reconcile the rows on screen in a spreadsheet. That is a **requester requirement**, not observed user behavior, because nothing says they are an end user or reporting research. No research, support export, or analytics were in the repo. Copying the table by hand is an **assumption**. Concern flagged, without replacing the request: an on-screen total would not meet the stated need for rows outside the product.

**Found in the product.** Billing table: date, number, amount, status. Owners and billing admins see it; members do not. Row action downloads one receipt PDF. Filters exist. No export API. The receipt PDF is a different task and does not choose the format.

**Decision.** CSV of those columns for the filtered set, because the requester's purpose is a spreadsheet of the rows on screen. **Proposed requirement:** an endpoint that returns that CSV. The UX is ready to build. Not provisional. Repeating the export is harmless: it returns another copy of the same rows. No status-query capability is required.

**Preparing.** Export shows "Exporting 12 invoices…". Filters stay editable. A second click is ignored. The file is the snapshot from the click. If filters changed, still deliver the file and say "Exported the 12 invoices from when you clicked Export". Do not cancel silently.

**Timeout.** Show "Export didn't finish. Try again." Retry requests the same snapshot again. A second file of the same rows is acceptable. Do not invent a status endpoint for a routine download. Disabling Export while the request is in flight is feedback only.

**No permission.** Action absent for members. Hiding is correct here because members have no related task on this table. If an admin loses **export** but can still read, keep the table, explain why Export stopped, and keep the filters. If they lose **read** access to invoices, remove the rows and the draft of those rows; do not leave restricted data on screen. Say whether a file already generated can still be downloaded. Rule: [behavior.md](references/behavior.md).

**Measurement.** This is a proxy, not a confirmed save. Among billing admins, count:

- HTTP responses that returned the CSV body for a non-empty filter.
- Export errors.
- Support tickets about getting invoice data out.

A link `download` attribute does not mean the file was saved. Baseline: tickets of that type in the last month, if support can supply them. Review after two weeks. Response count alone is not success.

**Validation (proposed, not run).** Claim under test: billing admins reconciling a filtered month will understand what Export produces. It is a CSV of the rows on screen, not a receipt PDF and not every invoice. Participants: billing admins. Prototype: the billing table with the button. Task: "Prepare last month's paid invoices for your spreadsheet." Conditions: filters already in the product, desktop. Revise if they look on each row, expect a PDF, or expect rows the filter hid. This test would not validate mobile. It would not show that CSV is the right reconciliation format.

## Design questions

These are prompts, not rules. When task evidence points the other way, follow the evidence. That includes comparison, expert, and monitoring work.

- Is the need served by this UI, or only the requested feature?
- Are choices few because the task is narrow, or must peers stay visible to compare?
- Should this be steps with progress, or one surface because the user compares, monitors, or repeats it?
- Is the next action recognizable without a tour, while the rest of the product stays available?
- Is input feedback immediate, and is longer work honestly indicated?
- Is the severe failure recoverable even if it is rare?
