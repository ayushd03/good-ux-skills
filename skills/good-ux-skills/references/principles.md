# Principles

Read a section only when it changes a design decision. These are tendencies with boundaries, not laws that override task evidence. The workflow, evidence rules, and plan shape are in [SKILL.md](../SKILL.md).

## Response time

Do not use one threshold for every wait.

- **Input feedback** (click, key, hover, toggle) should feel immediate, on the order of a tenth of a second. If it is slower, show that the control received the action.
- **Completing an operation** can take around a second before it breaks the person's train of thought. Past that, say what is happening.
- **Long work** needs honest status. Use a percent only when the percent is real. Otherwise say what is happening ("Checking with the bank") and whether they can leave. Give them a way to cancel when cancel is safe.
- About **400 ms** is a conversational-productivity target for back-and-forth tools, not the definition of a good tap, and not a reason to block the UI at 399 ms.
- Do not insert delay to make a result feel more careful or more valuable.

## Aesthetic and usability

People often rate a polished interface as easier, and that rating can track looks more than measured success. Polish is worth doing. Still judge task completion, errors, and time separately. Beauty hides defects in preference tests.

## Choice and memory

A large option set can slow the decision and leave people less satisfied, even when a good option was present. That is a risk, not a command to hide options the task requires. When comparison is the job, show the candidates together. Do not show a subset and hide the rest if people will treat the subset as complete.

Working memory is small and brief, on the order of a handful of chunks, and it varies with expertise and context. Chunk so each unit is one meaningful thing. Do not cap menus at seven. Prefer recognition (visited links, breadcrumbs, values carried forward) when the user would otherwise have to recall.

People remember the start and end of a list better than the middle in memory tests. That does not set navigation order. Order navigation and labels by the task and the information structure. Use the memory effect only as a reason to check that a critical action is not buried, not as a reason to put it at both ends.

Unfinished tasks are often remembered more than finished ones. A visible next step can help a task the user already intends to finish. Do not invent incompleteness to pull them back.

## Load

Intrinsic load comes from the task. Extraneous load comes from ornament, unclear labels, and decisions that do not help. Cut the second. Do not cut so far that the action becomes ambiguous. Pair icons with words unless the symbol is truly common in this product. Show the real choices as one group when splitting them would look like the full set.

## Grouping

People treat items as related when they are near, inside one boundary, visually connected, or similar in color, shape, size, or motion. Make those cues agree. There is no fixed order of strength to apply on every screen. If two cues disagree, people hesitate. Isolate one element when a single fact must stand out. Do not isolate one peer in a set that must be compared. Do not rely on color alone. Do not require motion to see the emphasis.

Simple, aligned layouts are easier to parse than layouts that can be read two ways. If a layout has two readings, people may take the simpler one.

## Familiarity

People carry expectations from other products and from physical controls. Match those when the task is the same. Leave them when the task is different, when the old pattern is the problem, or when novelty is the point. Novelty is the point for a different product shape, a changed task, or an experience whose goal is exploration. A novel pattern still has to pass a task test. When you change a product people know, let them preview or keep the old way for a while if the cost of a clash is high.

The team's model of the system is not the user's. Close the gap with observation, not with internal vocabulary on the screen.

## Attention

People attend to what serves the current goal. Do not style a real action like an ad or place it in a slot used for ads. People can miss a change when several things move at once. A monitoring screen may still need many updates. Give the update that matters a durable cue instead of banning simultaneous change.

## Flow, progress, and endings

Flow is more likely when difficulty matches skill and the next action is obvious. That is a description, not a requirement to remove every step.

People often speed up when the end is visible. Show progress that matches remaining work. A head start is fine when it reflects real stored data. Do not fake the meter.

People weigh the most intense moment and the ending more than the average of every step. Design the stressful moment and the ending on purpose. Negative peaks stick. This is a reason to care about errors and waiting, not a reason to add decoration.

## Complexity

When two designs serve the task equally well, prefer the one with fewer assumptions and fewer parts. Stop removing when the next removal hides the action or the consequence.

Some complexity cannot be removed, only moved. Put it in the product when the user would otherwise pay it on every use. People will not read a manual first. Teach on the path they are already on.

## Onboarding

Do not gate the product behind a tour. People start.

Contextual hints on the control are appropriate when they are easy to ignore. An optional checklist or template can orient a first session without blocking other tasks.

Do not hide the rest of the product as the default lesson plan. That blocks returning users, experts, and anyone who arrived for a different task. Distinguish:

- **Onboarding** — optional guidance while the product stays usable.
- **Required setup** — the task cannot proceed without a missing fact (a workspace). Ask for that fact and nothing else.
- **No data yet** — an empty state that explains how the object gets there, not a tour of unrelated features.

## Prioritization boundary

A small share of causes often accounts for a large share of volume. Use that to find high-volume tasks. Do not use it to ignore rare, severe harm: lockout, data loss, accidental disclosure, or a recovery path that some people cannot operate. Score severity, reach, recoverability, and how confident the evidence is. The rule in [SKILL.md](../SKILL.md) is the one to apply.

## Time on task

A task can expand when the interface offers needless steps. That is not evidence that people always choose the slow path on purpose. Remove steps that do not serve the need. Do not claim a slow path will be taken merely because it exists.

## Bias

People, including the team, notice what confirms the design they already like. A stakeholder's confidence is not observed behavior. In a review, look for the failure the layout makes easy to miss, and label it as a hypothesis until something demonstrates it.

## Input tolerance

Accept the input people actually give when the meaning is clear, normalize it, and say what you accepted or what is still wrong. What you show back should be strict and predictable. Ambiguous input is clarified, not silently guessed, when the guess could change money, identity, or the object of the action.
