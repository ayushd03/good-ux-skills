# Behavior

These rules apply only when their condition does. Read the section that matches the feature. The plan workflow is in [SKILL.md](../SKILL.md). Skip a section that cannot occur.

## Information architecture

- Use the object's name that users say, not the internal table name. The same object has one name across navigation, the page title, and the action.
- Navigation labels name the destination or the task, not a metaphor the team likes.
- Show current location (selected nav, title, breadcrumbs) when the product has more than one level.
- Say where this feature lives and which nearby action it is not. "Export" is not "Download receipt" if those produce different results.
- Categories follow how users look for the thing. If search logs or support show another name, use that name or accept both.

## Choosing a pattern

Pick by the task, then record the reason.

| Use | When |
| --- | --- |
| Same page | The task is short, context on the page still matters, or the user repeats it |
| Modal | A short decision, the page underneath must stay in place, and there is a visible dismiss |
| Drawer | More context than a modal, still without losing the parent, and it must work at the narrow width |
| Inline edit | One field or a small group, with an obvious save or an explicit autosave |
| Wizard | Decisions depend on earlier answers, or one screen would mix unrelated choices. Not because the user is new |
| Direct manipulation | The object is visible and the action is on the object (reorder, resize) |

Every control looks interactive without relying on hover alone. A wizard does not hide the rest of the product unless those other areas are invalid until this setup finishes.

Keyboard: where focus moves when the layer opens, where it returns when it closes, and what Escape and Back do.

## Content

- Plain language. One term per object. Do not copy product language that users already misunderstand; say what was unclear and replace it.
- The action label names the result ("Export CSV"), not "OK" or "Submit", when the result is not obvious.
- Instructions appear before the user can make the mistake, next to the decision.
- Say the consequence before a costly action: object, scope, and what will be true afterward.
- Errors say what happened, what is still safe, and the next useful action. Do not blame the user. Do not use only "Something went wrong" when you know the cause.

## Forms

Specify each field:

- Label and purpose, plus why it is asked if that is not obvious.
- Default, and whether it is required or optional.
- Control type (text, select, date, toggle).
- What a valid value looks like.

Rules for every form:

- Validate when the user leaves the field or tries to submit, not on the first keystroke, unless a character can never be valid.
- The error is attached to the field. It clears when the value becomes valid. A server error maps to the field when the field caused it, and to a form-level message when it did not.
- Values the user entered survive a failed submit, a timeout, and a refresh if the plan says they do. State which.
- Use the input type and autocomplete token that match the data so browsers and password managers can fill them.
- Pasting the whole value works. Formatting (spaces in card numbers, dashes in phones) is tolerated and normalized.
- Do not ask for anything the product already has or does not need for this task. Do not ask twice.

## Undo, confirm, and preview

Use the lightest control that matches how reversible the **effects** are, not whether the field can be edited later.

- **Effects are harmless or fully undone by editing** — no confirm. Editing the value restores the prior situation, including anything it already changed.
- **Edit does not undo the effect** — publishing to a wider audience, starting a recurring charge, or pointing an integration at a new destination can act immediately. Treat that as undo, preview, or confirm, even if the control can be switched back.
- **Undo** — the action applies immediately. Say what was undone and how long undo lasts. Undo restores the previous state, including related records, or the plan lists what it does not restore.
- **Preview** — the user must see the exact object and scope before commit (who receives it, which rows, the amount).
- **Confirm** — only when undo is impossible or the harm is serious. The dialog names the object and the consequence. "Are you sure?" is not enough. The confirm button repeats the verb ("Delete 12 invoices"), not "Yes".

State downstream effects: shared copies, notifications, billing, and what another person already saw.

## Unconfirmed async work

If a timeout, a closed laptop, or a lost connection can happen after the server may have succeeded, and repeating the action would double-charge, double-send, or double-write:

- The UI says the outcome is **unconfirmed**, not that it failed.
- Either check that operation's status, or retry the **same** operation under a verified duplicate-protection contract (the same idempotency key). Do not silently start a new operation while the original outcome is unknown. A missing status endpoint is not required when that contract already exists.
- Disabling the button only shows that this view is waiting. It does not cover refresh, another tab, or a retry from somewhere else.
- Partial success lists what finished and what did not, each with a next step.
- An optimistic update rolls back visibly if the server rejects it, and says what the user is looking at now.

If repeating the action is harmless, say that and offer retry. Do not add a status service for a routine download.

## Persistence and navigation

Write the contract for any task with state:

- **Back** — returns to the previous step with entries intact, or warns. Do not silently discard.
- **Refresh and reopen** — what is still there.
- **Close tab** — draft kept or not, and for how long.
- **Session expiry** — reauthenticate and return to the same step with the draft, unless the data must be dropped for security. Say which.
- **Another device** — available or not.
- **Autosave** — the status text ("Saved" / "Saving" / "Couldn't save") and what is included.
- **Filters, sort, and scroll** — restored when the user returns in the same session, or not. Say which.
- **Cancel** — dismisses the surface only, or also cancels the server operation. These are different. Name the one you mean.

## Data, collaboration, and scale

When more than one person can touch the object, or the collection can be large:

- What the user sees if the record changed, was deleted, or changed owner while they were editing. Who wins, and what is kept of their draft.
- Search, filters, and no-results: why it is empty, and how to clear the filter. Distinguish "none exist" from "none match".
- Sort is labeled with the field and direction. Pagination or infinite scroll states what is loaded.
- A selection that crosses pages says whether the action applies to the selected rows or to every row matching the filter. Default to the visible selection unless the user explicitly expands the scope.
- A bulk action reports partial failure per item. It does not say "done" when some failed.
- The layout and the actions still make sense with three records and with thousands. Do not design only the demo set.

## Localization

When the product is translated or takes international input:

- Layout survives longer strings. Do not size a control to the English word.
- Right-to-left mirrors the layout and keeps media and numbers readable.
- Names, addresses, and phone numbers are not forced into one country's shape.
- Currency, units, pluralization, dates, and time zones are explicit. A date that could be either day-first or month-first is clarified, not guessed, when the guess changes the booking or the deadline.
- Show the zone when a time is a deadline or a shared event.

## Privacy

Masking is not the whole job. At the decision point, say why the information is requested, who can see it, and how long it is kept when the user would not already know. Sharing defaults to the narrower audience when the product can do either. Optional consent can be refused and later withdrawn without a dead end. Revoking access tells the user what already-shared copies remain. Do not ask for data the task does not need.

Also say where sensitive values can appear or be copied: the screen someone else can see, notifications, logs, analytics, and exported files. Mask or omit them there unless the task requires the value.

## Access that changes mid-task

Checking the role at the start is not enough.

- If the session expires, reauthenticate and restore the work that is safe to restore.
- Show which account or workspace the action applies to when the user has more than one.
- Check authorization for the specific resource and action, not only the role named at the start.
- If **edit** access is removed but **read** access remains, keep the content they may still see. Stop the forbidden action, and explain what they can still do with their draft.
- If **read** access is removed, do not leave the restricted content or a draft of it on screen. Say what, if anything, can be recovered through a path they are still allowed to use.
- **Hide** the action when this person has no related task and showing it would be noise or a probe (a member on a billing table).
- **Show it disabled with a reason** when they can see the object, expect the action, and need to know why it is blocked or how to request access.
- Provide a request-access path when another role can grant it and the user is allowed to ask.

## Notifications and handoffs

- Interrupt only when the user must act, must learn about harm, or asked to be told.
- Some notices are legitimate even if the page showed the same state a moment ago: a receipt, a confirmation they requested, and a background job that finishes after they left.
- Suppress a second notice when they are already looking at that result. Honor preferences. Keep a durable record when they may need it later.
- Name the channel, the urgency, and what happens if they miss it. Do not duplicate the same alert across every channel by default.
- Preferences exist when the product sends more than transactional mail.
- A handoff names who acts next, by when, where they see it, and what the sender sees while they wait.
- If the recipient never acts, say the timeout and the sender's next step.
- Some failures need a person. Give the route (a reference number, a contact) when retry cannot fix it. Do not invent a support channel the product does not have; mark it as a proposed requirement or an open question.

## AI features

Use this only when the feature generates, ranks, or recommends.

- Say what the system did and what it did not check.
- The user can edit or reject the result before it becomes the record, unless the plan explains why not.
- A wrong result has a recovery that does not depend on generating again blindly.
- Do not present a generated fact as verified data. Cite or label uncertainty when the product has it.
- Empty, slow, and refused generations each have a next step.
