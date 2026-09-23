# Research Rationale for ADP

**Author:** Frederik Smith  
**Email:** w5zk8yjto@mozmail.com  
**License:** MIT

> The normative protocol is `../ADP.md`.

ADP addresses recurring AI coding failure modes: repeated human "continue" prompts, context loss, architectural drift, weak verification, fragmented planning, poor handoff, and opaque autonomous progress.

Its core model treats the repository as durable project memory and the agent session as replaceable execution capacity. Stable canonical knowledge is separated from ephemeral operational state. Work is structured as Project → Milestone → Workstream → Contract → Atomic Unit → Evidence. Soft checkpoints persist progress without demanding acknowledgement; hard checkpoints are reserved for genuine authority/safety boundaries.

Transition Transparency complements autonomy rather than weakening it. At meaningful Contract or Milestone boundaries, a concise Transition Brief exposes the completed outcome, verification state, current milestone, next recommended phase, rationale, first action, and execution state. Human-scale direction is persisted in STATUS.md while agent-scale resume instructions remain in CONTINUITY.md. This avoids both silent autonomous drift and repetitive permission prompts.

ADP remains vendor-, language-, framework-, and harness-neutral. Future empirical work should compare intervention frequency, completion rates, verification quality, bootstrap quality, and cross-agent handoff performance.
