# Capability-aware agent assignment and failover (optional)

> Non-normative implementation guide for the [canonical ADP protocol](../ADP.md). This is a policy **extension** to delegated execution, not a required orchestrator or another authority hierarchy.

## Why this exists

Contracts may need different coding capabilities, tools, privacy guarantees or review independence. A preferred Lead Programmer may hit a context limit or provider quota. ADP's repository state and cold-start checks already enable safe successor work; this extension specifies **how to select**, **whether to switch**, and **how not to exceed authorization**.

## The three execution modes

| Mode | Mechanism | Guarantee |
| --- | --- | --- |
| `advisory` | Agent recommends a suitable authorized role/model and a handoff | Works without extra runtime; never claims a model switch |
| `harness_native` | Existing harness selection/delegation support | Only what the installed harness actually supports |
| `external` | Separate, explicitly authorized orchestrator/runtime | Implementation-dependent; not installed by ADP |

A chat application cannot necessarily change its own model or wake up a new process. A router that selects LLM API calls is not equivalent to a safe coding-session handoff. No mode bypasses credentials, runtime uptime, hard checkpoints, or authorized API charges.

## Optional policy

Copy [the sample policy](../examples/AGENT_POLICY.json) to `.project/AGENT_POLICY.json` in a target project, **only if useful**. Validate using [the JSON Schema](../schema/agent-policy.schema.json). The example deliberately has `max_api_spend_usd: 0` and `advisory` mode: it never turns on paid APIs or external services.

Policies specify preferences, not permissions. Director/owner rules, existing authorization, and Contract/security constraints have precedence. The lead programmer may make ordinary technical decisions; reserved/product/budget/irreversible decisions remain with the human. An acting lead must already be authorized. An optional policy cannot self-authorize privileged actions.

Resource profiles:
- `maximum_quality`: maximize verified suitability among eligible available candidates, not unlimited paid spending.
- `balanced`: quality/latency/resource balance without skipping required checks.
- `subscription_quota_aware`: conserve limited premium interactions; subscription quotas are not cross-provider API funds.
- `cost_capped`: stay under explicitly authorized API usage; zero budget forbids new paid fallback calls.
- `privacy_first`: restrict to eligible providers and environments satisfying data-handling rules.

An approved provider is **eligible for consideration**, not guaranteed available, billed, or authorized to receive every class of data. If provider capability, remaining quota, price, context window, or billing rights cannot be verified, treat it as UNKNOWN.

## Suggested evaluation record

For a substantial Contract, keep any needed rationale in that Contract, without creating an obligatory report per task:

- Required language/stack, tools, context, privacy and risk/review conditions
- Eligible candidates and why any candidates were excluded
- Preferred coordinator/worker role and resource policy used
- Selected execution approach, evidence/uncertainty, and fallback
- Whether any decision is reserved for the human; other unblocked work to continue

Do not hardcode universal "best models" or award performance scores based only on marketing. Measure task outcomes using verification evidence, revisions, tests and defect follow-up when practical.

## Safe quota or outage handoff

1. Classify failure: exhausted quota, retryable rate limit, context pressure, provider outage, missing credentials/tools or unknown.
2. Safely preserve unlanded changes; update the Contract and `docs/CONTINUITY.md` with last good state, Git reference, actual verification, blocker and exact next action.
3. Check the successor's eligibility, policy, access, spending, and mutation isolation. Do not invent cross-platform subscription entitlements.
4. Successor follows ADP's cold-start procedure and inspects actual changes and evidence; it must not blindly replay partially completed non-idempotent actions.
5. Coordinator reconciles output. If the original task requires human authority, leave it blocked and continue independent ready work instead of silently deciding.

A separate actor may act as coordinator only within the same previously authorized role scope. Preserve review independence for high-risk work; a second model name is not enough without independent inspection.

## Contract and ledger conventions

A substantial Contract MAY include a **Capability / assignment** section. `.project/WORK.json` MAY carry recovery-useful `execution.assignment` metadata; model IDs are snapshots, not permanent role identity or product truth. Keep per-request tokens, current quota, rate-limit reset times, process IDs and credentials outside canonical project metadata.

## Reference integration boundary

A real orchestrator would need adapters for model discovery, auth/billing policy, process supervision, workspace isolation, retry classification, runtime events, and cold-resume validation. It should expose capabilities truthfully and fail closed on authorization or paid-access uncertainty. This release defines no such running service and does not require one.

