# Agent and Harness Compatibility

ADP is vendor-neutral. A compatible agent should be able to read/edit repository files, inspect code/Git state, execute development commands, run verification, and preserve durable repository state.

Canonical routing is `AGENTS.md → ADP.md`.

Vendor adapters must stay thin and MUST NOT become independent protocol copies. If an adapter conflicts with `ADP.md`, `ADP.md` wins.


## Delegation and concurrency

Multi-agent capability is optional. A compatible ADP agent/harness does not need to support delegation to execute ADP correctly.

When a harness does support delegated or concurrent work, it should be able to preserve the execution brief, return worker results/evidence to a coordinating agent, and provide isolated writable workspaces for concurrent mutating lanes or else serialize mutation.

Harness-specific worker/session/process identifiers are runtime state, not canonical project state. Prefer event-driven completion/escalation when available; do not require model-driven polling as part of ADP itself.
