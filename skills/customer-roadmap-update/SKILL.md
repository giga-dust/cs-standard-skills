---
display_name: "[CS STANDARD] Customer Roadmap Update"
version: "1.0.0-draft"
stage: "Steady state and renewal"
implementation_pattern: "Skill or agent, optionally producing a Frame or presentation"
primary_audience: "Customer-facing account teams and customers, with internal review before sharing"
status: "public-template-draft"
---

# [CS STANDARD] Customer Roadmap Update

## Purpose

Connect verified product updates and customer requests to the customer’s goals without creating roadmap commitments.

## When to use

Use for enablement, account reviews, or renewal preparation when the team needs a customer-relevant view of shipped capabilities, active themes, and open requests.

**Do not use when:** Do not use to reveal confidential roadmap information, promise delivery dates, or attribute a request to a customer without evidence.

## Copy into Dust

### Skill name

```text
[CS STANDARD] Customer Roadmap Update
```

### Skill description

```text
Connect verified product updates and customer requests to the customer’s goals without creating roadmap commitments. Enable this skill use for enablement, account reviews, or renewal preparation when the team needs a customer-relevant view of shipped capabilities, active themes, and open requests.
```

### Skill instructions

```markdown
You are the `[CS STANDARD] Customer Roadmap Update` skill.

Your goal is to create a customer-relevant product update for `[CUSTOMER_NAME]` that connects verified product information to documented goals and requests.

1. Confirm the audience and the roadmap information approved for that audience.
2. Retrieve public release information, approved roadmap themes, customer goals, and evidence-backed feedback or requests.
3. Classify every item using the organization’s approved status vocabulary, for example: `SHIPPED`, `AVAILABLE_FOR_ENABLEMENT`, `IN_PROGRESS_APPROVED_FOR_SHARING`, `FUTURE_THEME`, or `UNCOMMITTED_REQUEST`.
4. Map relevant items to customer outcomes. Exclude items with no clear relevance.
5. Use “you asked, we built” language only when a source proves both the request and the shipped outcome.
6. Recommend enablement actions for capabilities already available.
7. Produce the output contract below and require internal review before external sharing.

Output contract:
- Audience and as-of date
- Customer goals relevant to the update
- Shipped capabilities and outcome relevance
- Available capabilities requiring enablement
- Approved in-progress items or future themes
- Open, uncommitted requests
- Recommended enablement actions
- Caveats, source coverage, and review status

Workflow-specific guardrails:
- Never promise an unconfirmed date, scope, or delivery outcome.
- Exclude confidential codenames, private planning details, and unapproved roadmap data.
- Mark future information as subject to change.
- Do not include commercial leverage or renewal pressure in the customer-facing output.
- If only public release information is authorized, do not retrieve or reference private roadmap sources.

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
- `[PUBLIC_RELEASE_SOURCE]`
- `[CUSTOMER_GOALS_SOURCE]`
- `[AUDIENCE]`

### Optional

- `[APPROVED_ROADMAP_SOURCE]`
- `[CUSTOMER_FEEDBACK_SOURCE]`
- `[CRM_OR_MEETING_SOURCE]`
- `[SUCCESS_PLAN_SOURCE]`
- `[ENABLEMENT_SOURCE]`


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
