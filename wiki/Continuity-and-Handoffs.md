# Continuity and Handoffs

> This page is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

ADP assumes agent sessions can disappear, models can change, and context windows can end.

The project must remain recoverable anyway.

## Repository as durable memory

Critical project knowledge should not exist only in chat.

ADP separates:

- canonical product and architecture facts;
- durable operational state;
- generated resume state;
- ephemeral local agent/runtime state.

## CONTINUITY.md

A substantial ADP project maintains `docs/CONTINUITY.md` as a concise resume packet.

It should identify:

- active objective;
- active Milestone;
- active Workstream;
- active Contract;
- current position;
- last known-good state;
- verification state;
- work in progress;
- blocker/investigation;
- next recommended phase;
- exact next action;
- decisions since the last checkpoint;
- workspace/Git state.

It is a current snapshot, not a chronological diary.

## Cold-start protocol

A fresh agent should:

1. read root `AGENTS.md`;
2. read `docs/CONTINUITY.md`;
3. read `docs/STATUS.md`;
4. read the active Contract;
5. inspect Git status and relevant diff;
6. inspect recent history when useful;
7. read relevant canonical docs;
8. run the cheapest useful health check;
9. compare repository reality with the handoff;
10. repair stale continuity metadata;
11. resume the exact next unblocked action.

A successor should verify predecessor claims against code, Git, tests, and other evidence.

## Context pressure

Do not intentionally run a context window to zero.

When context pressure becomes meaningful:

1. finish the current Atomic Unit if safe;
2. avoid starting broad new work;
3. run narrow relevant verification;
4. update Contract/status/continuity;
5. record known-good state;
6. preserve the exact next action;
7. checkpoint with Git if permitted;
8. compact/reset/handoff;
9. continue automatically when supported.

## Delegated work

When delegated/concurrent work is active, continuity should record only durable recovery information, such as:

- Contract and delegated scope;
- mutation posture;
- stable branch/workspace reference when useful;
- integrated versus unlanded state;
- verification state;
- blocker;
- exact next reconciliation/resume action.

Transient process/session/pane/watch state normally remains ephemeral.

## Related pages

- [Repository Control Plane](Repository-Control-Plane.md)
- [WORK.json](WORK-json.md)
- [Transition Transparency](Transition-Transparency.md)
