# Agent and Harness Compatibility

ADP is vendor-neutral. A compatible agent should be able to read/edit repository files, inspect code/Git state, execute development commands, run verification, and preserve durable repository state.

Canonical routing is `AGENTS.md → ADP.md`.

Vendor adapters must stay thin and MUST NOT become independent protocol copies. If an adapter conflicts with `ADP.md`, `ADP.md` wins.
