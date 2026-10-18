# Transition Transparency

> Introduced in ADP 2.4.0. This page is explanatory; [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

High autonomy should not mean invisible autonomy.

ADP uses **Transition Briefs** to make meaningful project boundaries visible without forcing the user to repeatedly authorize normal continuation.

## Transition Brief

At a substantial Contract/Milestone boundary, hard checkpoint, or objective completion, a Transition Brief identifies as applicable:

- **Completed** — what just finished;
- **Verification** — VERIFIED / FAILED / NOT RUN / NOT AVAILABLE;
- **Current milestone** — the larger outcome in progress;
- **Blockers / risks** — only material items;
- **Next recommended phase** — the next meaningful outcome;
- **Why this is next** — dependency/value/risk rationale;
- **First action** — the first concrete step;
- **Execution state** — CONTINUE / CHECKPOINT / COMPLETE.

## Execution states

### CONTINUE

The next work is authorized and unblocked.

The brief is informational. The agent should continue automatically.

### CHECKPOINT

Human authority or information is required.

### COMPLETE

The authorized objective is satisfied.

Future ideas may still be suggested, but they are not silently converted into scope.

## Next recommended phase vs exact next action

ADP distinguishes two levels:

- **Next recommended phase** — human-scale direction.
- **Exact next action** — agent-scale cold-resume instruction.

Example:

```text
Next recommended phase:
Production-readiness hardening.

Exact next action:
Run the integration suite against the new auth middleware and inspect the
remaining two failing refresh-token cases.
```

## Persistence

Underlying state is persisted in the existing control plane:

- `STATUS.md` — next recommended phase, rationale, first action;
- `CONTINUITY.md` — directional context + exact next action;
- optional `WORK.json` — machine-readable next Contract/Milestone IDs.

Transition Briefs themselves are not another source of truth.

## Delegated execution

In multi-agent work, workers normally report to the coordinating agent. The coordinator reconciles results and surfaces meaningful transitions to the user, avoiding competing progress narratives.
