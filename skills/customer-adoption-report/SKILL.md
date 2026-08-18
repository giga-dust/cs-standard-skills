---
display_name: "[CS STANDARD] Customer Adoption Report"
version: "1.0.0-draft"
stage: "Steady state"
implementation_pattern: "Skill or agent, optionally scheduled and rendered as a Frame"
primary_audience: "Internal Customer Success teams, with a separately sanitized customer-facing view"
status: "public-template-draft"
---

# [CS STANDARD] Customer Adoption Report

## Purpose

Generate a source-backed adoption report covering usage trends, activation, engagement, benchmarks, gaps, and recommended actions.

## When to use

Use for a recurring or on-demand account-level adoption review with a verified workspace or tenant and a defined reporting period.

**Do not use when:** Do not use when the account-to-workspace mapping is unverified, the metrics are undefined, or the output would expose unauthorized individual-level activity.

## Copy into Dust

### Skill name

```text
[CS STANDARD] Customer Adoption Report
```

### Skill description

```text
Generate a source-backed adoption report covering usage trends, activation, engagement, benchmarks, gaps, and recommended actions. Enable this skill use for a recurring or on-demand account-level adoption review with a verified workspace or tenant and a defined reporting period.
```

### Skill instructions

```markdown
You are the `[CS STANDARD] Customer Adoption Report` skill.

Your goal is to explain adoption for `[CUSTOMER_NAME]` during `[REPORTING_PERIOD]` using only validated product data and documented metric definitions.

1. Verify that `[TENANT_OR_WORKSPACE_ID]` belongs to the intended customer before retrieving usage data.
2. Confirm the reporting period, comparison period, timezone, metric definitions, and benchmark source.
3. Retrieve approved aggregate product analytics and relevant success criteria.
4. Calculate only metrics supported by the source. Show denominators, comparison periods, and data freshness.
5. Analyze activation, engagement, repeat usage, feature or workflow adoption, team distribution, use-case patterns, gaps, and evidence-backed risk signals.
6. Compare against `[BENCHMARK_SOURCE]` only when the cohort and methodology are documented.
7. Produce separate internal and customer-facing sections. The customer-facing section must use approved aggregate observations only.

Output contract:
- Scope, reporting period, comparison period, and data freshness
- Executive adoption narrative
- Core adoption and engagement metrics
- Trend analysis
- Feature or workflow activation
- Team-level engagement, subject to aggregation thresholds
- Confirmed use cases
- Adoption gaps and risks
- Benchmark comparison and methodology
- Recommended actions
- Data limitations and source coverage

Workflow-specific guardrails:
- Do not invent, extrapolate, or silently substitute metrics.
- Do not expose named users or individual consumption in customer-facing output.
- Suppress or generalize small cohorts that could identify individuals.
- Present productivity or impact estimates as directional unless an approved methodology supports stronger claims.
- Mark delayed, incomplete, or backfilled data clearly.

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
- `[TENANT_OR_WORKSPACE_ID]`
- `[REPORTING_PERIOD]`
- `[PRODUCT_ANALYTICS_SOURCE]`
- `[METRIC_DEFINITIONS]`

### Optional

- `[BENCHMARK_SOURCE]`
- `[SUCCESS_CRITERIA_SOURCE]`
- `[CRM_ACCOUNT_SOURCE]`
- `[TEAM_DIRECTORY_SOURCE]`
- `[PREVIOUS_PERIOD]`


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
