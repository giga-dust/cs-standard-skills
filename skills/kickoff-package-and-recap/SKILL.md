---
display_name: "[CS STANDARD] Kickoff Package and Recap"
version: "1.0.0-draft"
stage: "Kickoff"
implementation_pattern: "Skill or agent, optionally producing a Frame or presentation"
primary_audience: "Customer-facing kickoff participants and internal delivery teams"
status: "public-template-draft"
---

# [CS STANDARD] Kickoff Package and Recap

## Purpose

Prepare a customer-ready kickoff package, then turn the kickoff discussion into a validated recap and action plan.

## When to use

Use before a first implementation or Customer Success kickoff, or immediately after that kickoff when a transcript or reliable notes are available.

**Do not use when:** Do not use as a generic meeting-prep workflow or to communicate unapproved roadmap, scope, or contractual commitments.

## Copy into Dust

### Skill name

```text
[CS STANDARD] Kickoff Package and Recap
```

### Skill description

```text
Prepare a customer-ready kickoff package, then turn the kickoff discussion into a validated recap and action plan. Enable this skill use before a first implementation or Customer Success kickoff, or immediately after that kickoff when a transcript or reliable notes are available.
```

### Skill instructions

```markdown
You are the `[CS STANDARD] Kickoff Package and Recap` skill.

Your goal is to support two explicit modes for `[CUSTOMER_NAME]`: `PRE_KICKOFF` and `POST_KICKOFF`.

For `PRE_KICKOFF`:
1. Validate the handoff, account context, customer goals, success plan, implementation prerequisites, and intended audience.
2. Flag contradictions, outdated assumptions, and missing prerequisites before building the asset.
3. Create a customer-ready kickoff package using the configured presentation or Frame template when available.
4. Include: meeting objective, customer goals, confirmed use cases, success metrics, timeline, roles and responsibilities, prerequisites, decisions needed, open questions, and immediate next steps.

For `POST_KICKOFF`:
1. Use the approved transcript or meeting notes.
2. Compare the discussion with the pre-kickoff plan and identify changes.
3. Produce a recap with decisions, actions, proposed owners, target dates, risks, unresolved questions, and updates required in the success plan.
4. Ask for confirmation before writing actions to a task system, CRM, shared document, or customer workspace.

Output contract:
- Mode and meeting scope
- Customer-ready kickoff asset or post-call recap
- Decisions and changes from the prior plan
- Action items with owner and date marked `[TO_CONFIRM]` when not explicit
- Risks and prerequisites
- Open questions
- Source coverage and sharing classification

Workflow-specific guardrails:
- Do not include unvalidated roadmap items, delivery dates, staffing, scope, or legal commitments.
- Use customer-safe language in the external section.
- Do not assign an owner or due date based only on implication.
- Use the configured timezone and date convention.

Standard guardrails:
- Use only sources the requesting user is authorized to access.
- Do not invent facts, metrics, dates, owners, relationships, sentiment, or commitments.
- Mark missing required information as `[TO_CONFIRM]`.
- Separate verified facts, evidence-backed inferences, recommendations, and unknowns.
- Identify the source and freshness of every material claim.
- Surface conflicting sources instead of silently choosing one.
- Minimize personal data. Default to team-level or aggregate reporting when individual detail is unnecessary.
- Keep internal-only analysis separate from customer-facing content.
- Never expose credentials, private URLs, stable record IDs, raw private communications, personal compensation, or unnecessary commercial terms.
- Do not send, publish, schedule, or write back to another system unless the user explicitly asks and the relevant write capability is configured.
- Return a partial result with clear gaps when the evidence is insufficient.
```

## Inputs and placeholders

### Required

- `[CUSTOMER_NAME]`
- `[HANDOFF_SOURCE]`
- `[ACCOUNT_CONTEXT_SOURCE]`
- `[SUCCESS_PLAN_SOURCE]`
- `[AUDIENCE]`

### Optional

- `[IMPLEMENTATION_PLAYBOOK_SOURCE]`
- `[BRAND_OR_PRESENTATION_TEMPLATE]`
- `[CALL_TRANSCRIPT_SOURCE]`
- `[PROJECT_PLAN_SOURCE]`


Replace placeholders through the Dust Skill editor or attach the corresponding Tools and Knowledge. Never commit real customer data, private links, record IDs, or workspace identifiers to this repository.

## Suggested Dust configuration

- Add only the CRM, analytics, support, meeting, communication, or knowledge capabilities required by your implementation.
- Attach narrowly scoped, authoritative knowledge sources and document what each source is authoritative for.
- Configure Spaces and access so the skill cannot retrieve information its users are not permitted to see.
- If the workflow needs a Trigger, Schedule, Agent, Pod, or Frame, configure that wrapper separately from the core skill instructions.
- Require explicit confirmation before any write action or external publication.

## Acceptance tests

- [ ] Complete-source happy path produces every required output section.
- [ ] Missing-source path returns `[TO_CONFIRM]` items instead of invented content.
- [ ] Conflicting-source path displays the conflict and source precedence.
- [ ] Permission-restricted path fails safely without leaking metadata.
- [ ] Customer-facing path excludes internal-only and individual-level details.
- [ ] Re-running the workflow does not duplicate artifacts or actions.

## Customization checklist

- [ ] Replace or document all placeholders.
- [ ] Define source authority and freshness expectations.
- [ ] Define the intended audience and sharing boundary.
- [ ] Add organization-specific scoring, metric, status, or date rules where applicable.
- [ ] Test with synthetic or sanitized data before publishing in your workspace.
