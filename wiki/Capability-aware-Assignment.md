# Capability-aware Assignment and Failover

> Explanatory guide only. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative. Available since ADP 2.8.0.

ADP can recommend an appropriate coding agent/harness/model for a Contract and define safe handoffs when quotas, context windows or provider failures interrupt work. It does **not** require multi-model tooling and cannot change models without an authorized runtime that supports it.

## Authority ≠ model

- **Director:** human retains final responsibility for reserved scope/product/budget and consequential decisions.
- **Lead Programmer:** coordinating role allowed to resolve ordinary technical questions and reconcile delegated work within existing authorization.
- **Assistant/Specialist/Reviewer:** limited to the Execution Brief and its authorization.
- An acting coordinator may recover a stalled lead's work only if the substitution is already authorized; different provider/model identities confer no extra rights.

When the lead cannot decide a reserved question, record options, recommendation and affected work. Continue independent ready work; do not treat silence as approval.

## Contract selection

1. Evaluate actual Contract requirements, risks, tools, context, sensitive data, review and dependencies.
2. Exclude candidates that fail authorization, data/privacy, capability, review or spending constraints.
3. Among remaining eligible models and harnesses, prefer evidence of actual suitability, tool compatibility, reliability, availability and appropriate resource use. Mark unsupported/unobserved data UNKNOWN.
4. Choose direct execution if delegation adds more overhead/risk than value.
5. Reassess when the Contract or evidence materially changes.

No model is permanently declared the "best" for a category. Different providers may be assigned to the same project role across sessions.

## Modes and preferences

| Mode | Meaning |
| --- | --- |
| advisory | Recommendation only; available without a special harness |
| harness_native | Use native selection/delegation only where documented and supported |
| external | Separately approved orchestrator supervising agents and cross-provider handoff |

Optional [sample policy](https://github.com/FrederikLive/ADP/blob/main/examples/AGENT_POLICY.json) and [schema](https://github.com/FrederikLive/ADP/blob/main/schema/agent-policy.schema.json) define optimization preference without granting credentials, elevated permissions, or paid API access.

Profiles: `maximum_quality`, `balanced`, `subscription_quota_aware`, `cost_capped`, and `privacy_first`. These are preferences after hard constraints. A subscription quota is not automatically an API billing entitlement.

## Safe failover

When a worker hits context or usage limits, the coordinator classifies the issue, preserves unlanded changes, records Git and verification state, updates `CONTINUITY.md` with the exact next action and checks a successor's eligibility. The successor must inspect the actual repo before retrying potentially non-idempotent work. Its changes remain provisional until reconciled and verified.

If no suitable and authorized successor exists, mark dependent work blocked and continue other ready work, or stop safely. ADP cannot promise overnight execution without a running authorized supervisor.

## Further reading

- [Implementation and compatibility guide](https://github.com/FrederikLive/ADP/blob/main/docs/AGENT_ORCHESTRATION.md)
- [Delegated & Concurrent Execution](Delegated-and-Concurrent-Execution.md)
- [Continuity & Handoffs](Continuity-and-Handoffs.md)
