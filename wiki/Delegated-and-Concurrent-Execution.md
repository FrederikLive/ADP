# Delegated and Concurrent Execution

> Introduced in ADP 2.5.0. This page is explanatory; [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

ADP supports multi-agent execution without requiring it.

The goal is **not** to maximize the number of agents. The goal is to use the smallest execution topology that materially improves correctness, speed, safety, or quality.

## Direct execution is still the default

Use one agent when one agent can complete the work coherently.

Delegate when there is a real advantage, for example:

- independent parallel work;
- specialist investigation;
- separate implementation and review;
- large tasks where context partitioning improves reliability;
- work that benefits from an independent audit.

Do not delegate simply because delegation is available.

## Coordinating agent

When work is delegated, the delegating agent becomes the coordinator for that scope.

The coordinator owns:

- decomposition;
- preservation of user intent;
- the Execution Brief;
- scope ownership;
- collision prevention;
- reconciliation;
- authoritative project-state updates;
- human-facing reporting.

Delegation does **not** enlarge the user's Authorization Envelope.

## Preserve user intent

A delegated worker needs enough context to understand **why** the work exists, not only what code to edit.

Weak:

```text
Implement factions.
```

Better:

```text
The product intentionally creates distrust and negotiation between players.
Implement the faction capability required by WORK-014 while preserving that
social-design goal and the acceptance criteria in PRODUCT.md.
```

This reduces the “telephone game” where a subtask is technically correct but wrong for the product.

## Execution Brief

A substantial delegated task should receive a compact generated brief containing, as applicable:

- user/product intent;
- Contract ID and outcome;
- owned scope;
- out of scope;
- acceptance criteria;
- dependencies and relevant canonical references;
- mutation posture;
- authorization and safety boundaries;
- required verification;
- delivery/handoff expectations.

The brief is a **projection**, not another source of truth.

## Mutation posture

### READ_ONLY

The worker may inspect, research, audit, reproduce, reason, and report.

It must not silently turn an investigation into code changes.

### MUTATING

The worker may modify the repository inside the delegated scope and Authorization Envelope.

## Concurrent mutation isolation

Two concurrent mutating lanes must **not** share one writable checkout.

Use separate:

- Git worktrees + branches;
- isolated checkouts + branches;
- harness-provided isolated workspaces;
- equivalent safe isolation.

A branch name alone is not enough if two agents are editing the same working directory.

If safe isolation is not available, **serialize the mutation**.

Shared databases, services, test environments, and other mutable resources need their own collision controls too.

## Scope ownership

Prefer non-overlapping mutable scopes.

If overlap is unavoidable, define:

1. who owns the contested surface;
2. integration order;
3. which edits are allowed concurrently;
4. how reconciliation will occur.

## Worker completion is provisional

A worker saying “done” is evidence, not authoritative project state.

Before marking work VERIFIED, the coordinator reconciles:

- user intent;
- Contract;
- canonical docs;
- actual diff/artifacts;
- acceptance criteria;
- verification evidence;
- dependency/integration state;
- unrelated-change safety.

Higher-risk work should receive independent verification or review.

## Preserve unlanded work

Never destroy, reset, recycle, or repurpose a delegated workspace containing unresolved unlanded work unless:

- the work has been safely preserved or integrated; or
- discarding that specific work was explicitly authorized.

Unexpected unlanded work is a state to reconcile, not an obstacle to erase.

## Human communication

Workers normally report to the coordinator. The coordinator uses ADP's existing Transition Briefs to keep the human operator informed.

Worker completion should normally cause **reconciliation and continuation**, not another routine “may I continue?” prompt.

## Supervision efficiency

When supported, prefer event-driven completion/escalation over repeated model-driven polling.

Runtime details such as process IDs, terminal panes, watcher state, and temporary inboxes should stay ephemeral unless they are genuinely needed for recovery.
