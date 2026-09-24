---
name: good-ux-skills
description: >-
  Review and design interfaces using established UX psychology: decision time,
  memory limits, Gestalt grouping, familiarity, feedback speed, progress,
  complexity, and how people remember experiences. Use when designing UI,
  reviewing screens, critiquing usability, writing UX copy or flows,
  onboarding, forms, navigation, or when the user mentions UX, usability, or
  good UX.
---

# Good UX Skills

Self-contained rules for designing and reviewing interfaces. Apply them so people can finish the task they came to do. Do not use them to trap attention, disguise ads, fake urgency, manufacture incompleteness, or hide alternatives someone would have chosen if they were visible.

## How to apply

1. Name the user's goal for this moment and the single action that completes it.
2. Walk the checks below. Raise a principle only when it changes a design decision.
3. Prefer the smallest change that removes friction. Do not add decoration to "apply" a principle.
4. If a familiar pattern and a novel one both complete the task, keep the familiar one unless novelty is the point (see Familiarity versus novelty).

Report each issue as:

- **Principle** — name
- **What happens** — the user cost on this screen
- **Change** — one concrete UI change

Lead with what blocks the goal. List principles that are already satisfied only when the user asked for a full audit.

## Checks

- Choices here are few, comparable, and ranked. A recommended path is obvious, and the real alternatives stay visible.
- Hard work is split into steps with visible progress.
- Information is chunked. The product remembers state. Key items sit at the start or end of a list.
- Related items are near, boxed, linked, or styled as one group. The layout reads as one simple figure. Only one thing is visually isolated, and color is not the only signal.
- Nothing important looks like an ad. One change happens at a time.
- Controls and flow match what people already know. They can start immediately; help sits on the control, not in a tour they must finish first.
- Response is under about 400 ms, or the wait is explained. Targets are large, spaced, and close to attention. Difficulty matches skill. The task is as short as people expect.
- Parts that do not serve the goal are gone. Complexity that cannot be removed sits in the product. Input is accepted in the form people actually type. Effort is on the few flows that matter most.
- The most intense moment and the ending are designed on purpose. Visual polish is high, and task success is still tested on its own.

## Aesthetic-usability effect

People rate attractive interfaces as easier to use, and that rating tracks looks more than measured ease. They also tolerate small usability flaws longer when the product looks cared for. Polish is worth doing. It also hides defects in preference tests, so judge task success, errors, and time separately from whether people say it looks good.

## Choice overload

A large set of options makes choosing slower and leaves people less satisfied with the outcome, even when a good option was in the set. This is the same pressure as decision time growing with the number of choices.

- Put a featured or recommended option forward.
- Let people narrow first with search and filters.
- When comparison is the job (plans, prices, specs), show the candidates side by side.
- Do not reveal a fake subset and hide the rest. People treat whatever is on screen as the full set.

## Chunking

Break a pile of items into a few meaningful groups so people can scan for what matches their goal and see what belongs together. Do it with modules, headings, rules, and spacing — not with a lower item count for its own sake. A raw digit string is hard; the same digits grouped as a phone number are easy. A wall of text is hard; the same words with headings, short paragraphs, and a readable line length are easy. Dense screens (dashboards, results, settings) need chunks so relationships are visible.

## Cognitive bias

People decide with shortcuts from past experience. Shortcuts are fast and systematically wrong. Knowing that does not delete the shortcut; it only makes it possible to catch it.

Design for the person who skims, misreads, and confirms what they already believe. Confirmation bias is the common one: we notice evidence that supports the design we already like and ignore the rest. In a review, look for the failure the layout makes easy to miss. Do not treat a confident stakeholder opinion as observed behavior.

## Cognitive load

Load is the mental work of understanding and operating the interface. Intrinsic load is the goal itself: hold the task, absorb what is new, keep track of progress. Extraneous load is work that does not help: ornament, unclear labels, extra decisions, things that must be remembered across screens. When incoming information exceeds working memory, people slow down, miss details, and abandon the task.

Causes to hunt: too many choices, too much thought required, lack of clarity.

Reduce extraneous load:

- Remove elements that do not help the goal. Do not cut so far that the action becomes ambiguous.
- Reuse patterns people already know, so they spend effort on the task instead of on learning the chrome.
- Move chores onto the system: editable defaults, previously entered data, anticipatory values.
- Show the real choices as one group. Options split across hidden panels get treated as if the hidden ones do not exist, which both limits people and makes the visible choice feel harder.
- Set type to be read: size, contrast, line length, and hierarchy. Legible but unpleasant text still costs attention.
- Pair icons with words unless the symbol is truly universal (close, play, search). Most icons depend on prior exposure and add load when they stand alone.

## Doherty threshold

Work feels additive when the computer answers before the person has to wait on it. The practical bar is about 400 ms. The older bar of about 2 seconds is too slow for a back-and-forth tool; under 400 ms, people stay engaged and throughput jumps.

- Return feedback within 400 ms whenever the system can.
- When it cannot, improve perceived speed: show that something is happening, skeleton the next view, animate the transition while work continues.
- Percent-done indicators make waits tolerable even when the estimate is imperfect.
- A short, deliberate pause can raise trust when the user expects careful work (a check, a tailored result). Never add delay to a trivial action to fake effort.

## Fitts's law

Time to hit a target grows with how far it is and shrinks as the target gets larger. Fast movement toward a small target produces errors. That tradeoff is the whole law.

- Make click and touch targets large enough to hit accurately.
- Leave space between targets so a near miss does not activate the neighbor.
- Put the next action close to where attention already is. A primary button at the far corner of a large screen is slow; the same button beside the field the user just finished is fast.
- On touch, finger size sets the minimum, not mouse precision.

## Flow

Flow is full absorption in the activity: focused on the present, feeling in control, enjoying the doing. It appears when challenge and skill match. Too hard becomes frustration. Too easy becomes boredom.

- Tell the user what their action just did and what is now done.
- Remove steps that are not part of the task. Slow response and scavenger hunts for features knock people out of the task.
- Keep the next useful action available to find without leaving the flow to hunt settings.

## Goal-gradient effect

Effort increases as the goal gets closer. People speed up near the end. They also speed up when they can see progress, including progress you surface early.

- Show where they are and what remains (steps, meter, checklist).
- A true head start helps a long task that would otherwise look untouched. "Profile 20% complete" because you already stored their name is motivating. A meter that does not match remaining work is not.
- The closer the finish looks, the more likely they are to complete. Design the last steps to feel short and clear.

## Hick's law

The time to decide rises with the number and complexity of choices. More stimuli, slower response. People do not want that work.

- When response time matters, cut choices.
- Split a complex task into smaller decisions so each screen carries less load.
- Highlight a recommended option.
- For new users, reveal features as they become usable instead of presenting the whole product at once.
- Do not simplify so far that the control becomes an abstraction nobody can decode. A remote with three mystery buttons is not simpler than a remote with labeled essentials.

Patterns: a search home that is only the query, because every extra module is another decision. A simple remote that moves complexity into on-screen menus, where options can be grouped and disclosed in layers. A first session that teaches one action in a safe context, hides everything else, then introduces the next feature after the first one works.

## Jakob's law

People spend most of their time in other products. They want this one to work the way those do. They carry expectations from anything that looks similar, including physical controls (a toggle should look like a switch, a radio like a radio).

- Use conventional placement, labels, and flows so attention stays on the task. Carts, checkout, back, search, and primary buttons should behave the way they do elsewhere.
- When you change a product people already know, let them preview the new version, keep the old one for a while, or switch back. Forcing the new model on day one creates a clash between what they remember and what is on screen.

## Familiarity versus novelty

Familiarity transfers skill. The interface can recede and the task can proceed. Novelty is justified in three cases:

- Differentiation is the goal: a different layout, feature, or interaction is how the product is supposed to stand apart (a browser that uses a sidebar and heavy personalization instead of the usual toolbar).
- The technology changes the task itself: the old pattern no longer matches how the job is done (answers composed from sources instead of a list of links).
- Exploration or surprise is the outcome: storytelling, exhibition, or play, where a scroll-driven or nonstandard interaction is the point. A conventional layout would be clearer and less memorable; pick the one that matches the goal.

Any novel pattern still has to pass a task test with the actual audience. If people cannot finish, drop the novelty. Research which audience you are designing for before you leave the common pattern.

## Law of common region

Elements inside a clearly bounded area are seen as a group. A border around a set, or a shared background behind it, is enough. Use a container when you need the structure to be obvious at a glance: card, panel, tinted section. This is often stronger and faster to read than spacing alone.

## Law of proximity

Items near each other are grouped, and they are assumed to share a function or a meaning. Tighten space inside the group and open space between groups. A results list works when each result is a tight cluster and the gap before the next result is larger than the gap inside it. People organize the page faster when proximity does the grouping for them.

## Law of prägnanz

People resolve ambiguous or complex images into the simplest form they can, because that takes the least effort. They process and remember simple figures better than complex ones. The eye will collapse a noisy arrangement into one shape if it can.

- Align to a small set of edges and a clear figure-ground split.
- Prefer one silhouette over overlapping structures the viewer has to reassemble.
- If the layout can be read two ways, people will pick the simpler reading, which may not be the one you intended. Remove the ambiguity.

## Law of similarity

Similar elements are seen as one group even when they are separated. Color, shape, size, orientation, and motion can all say "these belong together and do the same kind of thing."

- Repeat the same treatment for the same kind of action.
- Make links and navigation visually different from body text so they are not read as prose.

## Law of uniform connectedness

Elements that are visually connected are seen as more related than elements with no connection. Connect with a shared color, a line, a frame, an arrow, or another tangible link. Use it to show context or to lift a related subset out of a larger collection. A border around one result (a video, a featured snippet, a selected row) both ties that content together and separates it from the rows around it.

## Mental model

A mental model is the small working theory a person carries about how a system behaves. They build it from what they think they know, then apply it to anything that seems similar. When the product matches the model, knowledge transfers and they do not pause to learn the interface. When it does not, they do the wrong thing confidently.

- Match familiar structures: product cards, carts, checkout, navigation that stays put.
- The hard part is the gap between the team's model and the user's. Close it with observation, interviews, and journey mapping, not with internal vocabulary on the screen.
- Good experiences feel obvious because the model was already in the user's head.

## Miller's law

Immediate memory holds on the order of 7 ± 2 items. That span changes with what the person already knows and with the situation. The useful idea is not the number seven. It is chunking: people remember meaningful groups, not raw bits. Later evidence puts a practical working limit nearer four chunks. Do not cap menus, nav, or lists at seven to satisfy the law. Do group content so each chunk is one thing the user can process, understand, and remember.

## Occam's razor

When competing designs predict the outcome equally well, pick the one with the fewest assumptions. The best way to reduce complexity is not to add it. Examine each element and remove as many as you can without breaking the function. Stop when removing one more piece would harm the task, not when every idea has been included. A plainer design that still communicates beats a richer one that assumes the user will infer the same things you do.

## Paradox of the active user

People do not read manuals. They start, including into errors. They would often be faster later if they studied the system first, and they still will not. Motivation is the immediate task.

Do not gate the product behind a slideshow tour. Those overlays block the start and almost nobody reads them. Teach inside the product, on whatever path they take:

- Tooltips and hints on the control, at the moment of use. Light, contextual, easy to ignore.
- Progressive onboarding: hide the rest, let them succeed at one core action in a safe context, then reveal the next feature. This matches how people learn, by adding to something they already did.
- An optional getting-started checklist or template they can follow, leave, and return to. It limits the blank-page problem without trapping them.

Build for the person who clicks first, not for a careful reader who does not exist.

## Pareto principle

For many outcomes, a small share of causes produces most of the effect — classically about 80 percent of results from about 20 percent of inputs. Inputs and outputs are uneven. A large feature list often contains a few that matter.

- Find the tasks, screens, and errors that account for most of the real outcome.
- Spend design and fix effort there before polishing rare paths.
- A large group of items can contain only a few meaningful contributors. Prioritize those.

## Parkinson's law

A task expands to fill the time available for it. If the interface allows a slow path, people will take it, and the experience feels worse than the work required.

- Keep completion time near what people expect, and shorter when you can do that without new confusion.
- Autofill, saved details, and defaults collapse forms, booking, and checkout so the task cannot inflate.
- Reducing actual duration below expected duration improves the experience. Adding steps "while we have them here" does the opposite.

## Peak-end rule

People judge an experience by its most intense moment and its ending, not by the average of every moment. A longer uncomfortable episode that ends slightly better is remembered more kindly than a shorter one that ends at the worst point.

- Design the peak on purpose: the moment the product is most helpful, most valuable, or most stressful (pay, submit, wait, first success).
- Design the end: what finished, what happens next, and a clear sense that it worked. A bare confirmation wastes the moment people will actually remember.
- Negative peaks are remembered more vividly than positive ones. Waiting, errors, and uncertainty need more care than decorative delight.
- Perceived waiting is part of the peak. Shorten it or make the wait feel fair and informed so it does not become the memory of the product.

## Postel's law

Be liberal in what you accept and conservative in what you send. Systems that receive input should tolerate variation when the meaning is clear. Systems that emit output should stick to a strict, predictable contract.

- Expect odd input, partial data, different devices, and different abilities.
- Accept the input people actually give, translate it into what you need, define the bounds, and say what you accepted or what is still wrong.
- The more variation you planned for, the less brittle the design.
- What you show back should be reliable and accessible, not a mirror of whatever mess came in.

## Selective attention

People focus on a subset of what is on screen, usually the part tied to their goal, and filter the rest. Guide that focus. Do not compete with it.

- Banner blindness: people skip anything that looks like an ad, sits next to an ad, or occupies a slot historically used for ads. They do this on purpose and automatically. Do not style real content or actions that way, and do not place them in those slots.
- Change blindness: a meaningful change goes unseen when attention is limited and the cue is weak, especially if several changes happen together. Review the screen for competing updates and separate them so one cue can land.
- Tunnel vision is normal during a task. Put the next step on that tunnel, not in the periphery.

## Serial position effect

Items at the beginning and the end of a series are remembered better than items in the middle. The start is the primacy effect; the end is the recency effect.

- Put the actions and labels people must remember at the two ends of navigation, menus, and lists.
- Put the least important items in the middle. They are the ones that fail to stick in both working memory and long-term memory.

## Tesler's law

Also called the law of conservation of complexity. Every process has a core of complexity that cannot be designed away. Someone has to carry it: the product or the user. Put as much of that burden in design and engineering as possible. An extra week of implementation is cheaper than an extra minute paid by every user.

- Do not design for an idealized rational user. People skip, mis-tap, and refuse to prepare.
- When complexity remains, teach it in context (hints on the path they are already on), not in a preface.
- Simplifying a tool often makes people attempt harder tasks. Plan for the next task they will try once the first one feels easy.
- Controls are where complexity becomes visible. Every control you remove must reappear as behavior the system handles, or you have only hidden the complexity until it fails.

## Von Restorff effect

Also called the isolation effect. Among similar objects, the one that differs is the one people remember.

- Make the important fact or the primary action the different item.
- Use emphasis rarely. If several elements compete, none of them is isolated, and the loud ones get read as ads.
- Do not communicate that difference with color alone. People with color-vision deficiency or low vision will miss it. Pair color with shape, weight, label, or position.
- Motion can create isolation. Also give a static way to see the same emphasis for people who are sensitive to motion.

## Working memory

Working memory holds and manipulates the information needed to finish a task. Capacity is a few chunks, about 4 to 7, and a new chunk fades in roughly 20 to 30 seconds. People are good at recognizing something they have seen and poor at keeping new information ready to reuse.

- Show only what this step needs, and make sure it is relevant.
- Prefer recognition over recall. Mark visited links, show breadcrumbs, keep the path visible.
- Put the memory burden on the system. Carry values from screen to screen. If the user must compare items, show the comparison together instead of asking them to remember the previous page.

## Zeigarnik effect

Unfinished or interrupted tasks are remembered better than finished ones. An open loop stays active; a closed one drops away.

- Signal that there is more content, clearly, so discovery has a pull.
- Show progress so the open loop draws people toward finishing rather than toward anxiety.
- A visible head start makes the unfinished task feel worth continuing.
- Do not invent fake incompleteness to nag people back. Use the effect for tasks they already intend to finish.

## Gestalt grouping, together

Proximity, similarity, common region, uniform connectedness, and prägnanz are one perceptual system. People see organized patterns by default. Use them in this order of strength when a relationship must be unmistakable: connect or enclose first, then align by similarity, then tighten proximity, and keep the overall figure simple. If two groupings disagree (close together but styled differently, or boxed together but far apart), people hesitate. Make the cues agree.
