# Research Rationale for ADP

**Author:** Frederik Smith  
**Email:** w5zk8yjto@mozmail.com  
**License:** MIT

> The normative protocol is `../ADP.md`.

ADP addresses recurring AI coding failure modes: repeated human "continue" prompts, context loss, architectural drift, weak verification, fragmented planning, poor handoff, and opaque autonomous progress.

Its core model treats the repository as durable project memory and the agent session as replaceable execution capacity. Stable canonical knowledge is separated from ephemeral operational state. Work is structured as Project → Milestone → Workstream → Contract → Atomic Unit → Evidence. Soft checkpoints persist progress without demanding acknowledgement; hard checkpoints are reserved for genuine authority/safety boundaries.

Transition Transparency complements autonomy rather than weakening it. At meaningful Contract or Milestone boundaries, a concise Transition Brief exposes the completed outcome, verification state, current milestone, next recommended phase, rationale, first action, and execution state. Human-scale direction is persisted in STATUS.md while agent-scale resume instructions remain in CONTINUITY.md. This avoids both silent autonomous drift and repetitive permission prompts.

ADP remains vendor-, language-, framework-, and harness-neutral. Future empirical work should compare intervention frequency, completion rates, verification quality, bootstrap quality, and cross-agent handoff performance.


## Delegated and concurrent execution rationale

ADP 2.5.0 adds a deliberately small execution layer for environments that can run more than one coding agent. The change was motivated by a gap between ADP's existing ability to describe parallel Workstreams and its previous lack of normative rules for safely executing parallel mutation.

Review of orchestration-oriented systems, including [FirstMate](https://github.com/kunchenguid/firstmate), highlighted several generalizable behaviors: isolate concurrent writers, give delegated workers explicit bounded briefs, distinguish investigation from mutation authority, reconcile worker claims before accepting them, and preserve unlanded work during cleanup/recovery. ADP adopts those protocol-level principles without adopting FirstMate's runtime architecture, terminology, terminal backends, watchers, queues, or harness-specific machinery.

The optimization target remains the same: maximize correct completion of the user's intended product with low unnecessary intervention and low context overhead. Therefore direct single-agent execution remains the default when it is sufficient. Delegation is recommended only when independence, parallelism, specialization, review separation, or context partitioning provides a material advantage.

Execution Briefs are projections rather than new sources of truth. This preserves ADP's one-owner-per-fact discipline while giving a worker enough product rationale to avoid the delegation “telephone game,” where a technically correct subtask can drift from the user's actual goal.

Concurrent mutation isolation and reconciliation address two distinct failure modes: workspace collision while work is in flight, and false confidence after a worker reports completion. Isolation prevents agents from overwriting or testing against one another's partial changes; reconciliation prevents a worker's self-report from becoming authoritative without comparison to the Contract, canonical documents, actual artifacts, and evidence.

Future empirical work should compare direct versus delegated execution on completion quality, elapsed time, token/context cost, conflict rate, intervention rate, verification defects, and recovery after worker/session failure.
