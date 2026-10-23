# Agent and Harness Compatibility

ADP is vendor-neutral. A compatible agent should be able to read/edit repository files, inspect code/Git state, execute development commands, run verification, and preserve durable repository state.

Canonical routing is `AGENTS.md → ADP.md`.

Vendor adapters must stay thin and MUST NOT become independent protocol copies. If an adapter conflicts with `ADP.md`, `ADP.md` wins.


## Delegation and concurrency

Multi-agent capability is optional. A compatible ADP agent/harness does not need to support delegation to execute ADP correctly.

When a harness does support delegated or concurrent work, it should be able to preserve the execution brief, return worker results/evidence to a coordinating agent, and provide isolated writable workspaces for concurrent mutating lanes or else serialize mutation.

Harness-specific worker/session/process identifiers are runtime state, not canonical project state. Prefer event-driven completion/escalation when available; do not require model-driven polling as part of ADP itself.


## Optional capability-aware routing and model failover

The capability-aware assignment section of `ADP.md` is conditional, not a new requirement to use multi-model tooling. Supported modes:

- `advisory`: assess and recommend eligible assignment; a conforming agent must not claim it automatically switched a model.
- `harness_native`: invoke only actually available and authorized native features; such switching may be limited to a provider/model family.
- `external`: a separately deployed, authorized orchestrator may route workers across providers and manage processes. ADP does not implement this runtime.

An adapter SHOULD distinguish supported/unsupported/unknown model and harness capabilities; provider authorization, data restrictions, actual price/quota visibility, workspace isolation, process management, context recovery, retries and failure types. Lack of an API, subscription quota, or observable budget is not evidence of availability. A request-level LLM router is not an entire coding-session handoff.

Optional policy: [`schema/agent-policy.schema.json`](../schema/agent-policy.schema.json) and [sample](../examples/AGENT_POLICY.json); explanation in [`docs/AGENT_ORCHESTRATION.md`](AGENT_ORCHESTRATION.md). No adapter, vendor credentials, or policy file is required for basic ADP conformance. Providers must be checked against the applicable Authorization Envelope, spending ceiling, security requirements and Contract needs before selection. A generator's policy cannot grant permission.
