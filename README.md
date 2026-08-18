# CS Standard Skills for Dust

A public-ready library of anonymized Customer Success skill templates for Dust. Each template is designed to be copied into a Dust workspace, connected to that workspace’s own Tools and Knowledge, tested with sanitized data, and adapted to local processes.

## Included templates

| Lifecycle stage | Skill |
|---|---|
| Account handover | [`[CS STANDARD] Customer Success Handoff`](skills/customer-success-handoff/SKILL.md) |
| Account handover | [`[CS STANDARD] Stakeholder Power Map`](skills/stakeholder-power-map/SKILL.md) |
| Kickoff | [`[CS STANDARD] Kickoff Package and Recap`](skills/kickoff-package-and-recap/SKILL.md) |
| Steady state | [`[CS STANDARD] Customer Portfolio Prioritization`](skills/customer-portfolio-prioritization/SKILL.md) |
| Steady state | [`[CS STANDARD] Customer Adoption Report`](skills/customer-adoption-report/SKILL.md) |
| Steady state and renewal | [`[CS STANDARD] Customer Roadmap Update`](skills/customer-roadmap-update/SKILL.md) |
| Renewal and expansion | [`[CS STANDARD] Customer Business Review`](skills/customer-business-review/SKILL.md) |

## Install a template in Dust

1. Open the chosen `SKILL.md`.
2. Copy the **Skill name**, **Skill description**, and **Skill instructions** into the Dust Skill editor.
3. Replace the documented `[UPPER_SNAKE_CASE]` placeholders or attach the corresponding Tools and Knowledge.
4. Add only the capabilities needed for your implementation.
5. Configure access through the appropriate Spaces.
6. Test with synthetic or sanitized data in preview.
7. Publish the skill only after privacy, source, and output QA.
8. Configure any Trigger, Schedule, Agent, Pod, or Frame wrapper separately.

Dust Skills package reusable instructions, knowledge, and tools. Clear descriptions help agents decide when a skill should be enabled, while narrowly scoped sources improve reliability.

## Anonymization rules

This repository must not contain:

- Real customer, employee, stakeholder, or account-owner names
- Email addresses, profile links, stable user IDs, CRM IDs, workspace IDs, file IDs, or private URLs
- Raw call transcripts, emails, chat messages, support tickets, or CRM notes
- Pricing, discounts, contract terms, renewal strategy, or confidential roadmap details
- Named-user product activity or small cohorts that could identify individuals
- Secrets, tokens, credentials, or copied tool configuration

Use synthetic examples and `[UPPER_SNAKE_CASE]` placeholders. Treat combinations of role, reporting line, exact date, use case, and activity as potentially identifying even when names are removed.

## Repository conventions

- Every Dust display name starts exactly with `[CS STANDARD]`.
- Folder names use lowercase kebab-case.
- Core templates remain vendor-neutral where possible. Configure specific CRM, analytics, support, and meeting tools in your workspace.
- Unknown facts use `[TO_CONFIRM]`.
- Customer-facing and internal-only outputs remain separate.
- Any external sharing or write action requires explicit authorization.

## License

The templates in this repository are licensed under the [Creative Commons Attribution 4.0 International License](LICENSE). You may copy, adapt, and redistribute them, including commercially, provided appropriate attribution is given.

## Disclaimer

These templates are starting points, not legal, privacy, security, financial, or contractual advice. Each workspace owner is responsible for configuring permissions, validating data handling, testing outputs, and approving customer-facing use.
