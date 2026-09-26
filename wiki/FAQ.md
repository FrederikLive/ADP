# FAQ

> This Wiki is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

## Is ADP an AI coding agent?

No.

ADP is a **protocol** for how coding agents should understand, structure, execute, verify, persist, and hand off software-development work.

## Is ADP tied to ChatGPT, Claude, Copilot, Gemini, Cursor, OpenCode, or another vendor?

No.

Vendor-specific files should be thin adapters. Durable project behavior belongs in repository-native instructions and canonical project docs.

## Does ADP require multiple agents?

No.

Direct single-agent execution remains the default when it is the smallest sufficient topology.

ADP 2.5 adds rules for delegation and concurrency **when they are beneficial**.

## Does ADP require Git worktrees?

Not for ordinary single-agent work.

When multiple agents mutate the same repository concurrently, they must not share one writable checkout. Git worktrees are one good solution, but equivalent isolation is allowed.

## Why does ADP use Contracts?

Contracts give substantial work a durable outcome, scope, acceptance criteria, dependencies, validation plan, and handoff state.

They prevent the work from being defined only by a temporary conversation.

## Do all tasks need a Contract file?

No.

Small fixes can use the user's request/conversation as the Contract.

Avoid ceremonial documentation.

## Why HIGH autonomy?

The goal is to reduce repeated “continue?” prompts while keeping human authority over consequential actions.

HIGH autonomy covers normal reversible development. Hard checkpoints still protect destructive, expensive, externally consequential, security-sensitive, or materially ambiguous decisions.

## Can an agent deploy automatically?

Only if deployment is already within the user's Authorization Envelope and project policy.

Otherwise deployment is a hard checkpoint.

## What if tests cannot run?

Report `NOT AVAILABLE` or `NOT RUN` accurately.

Do not substitute “looks correct” for verification.

## What if an agent runs out of context?

ADP's Continuity Protocol requires enough durable repository state for a cold successor to recover the work without the old conversation.

## What if a delegated worker says it is done?

The coordinator treats that as provisional evidence, reconciles the result against the Contract and actual artifacts, and verifies proportionally before accepting it as authoritative project state.

## What if two agents need to edit the same area?

Prefer non-overlapping ownership.

If overlap is unavoidable, define ownership and integration order. Do not allow competing simultaneous writes to one workspace.

## Is `WORK.json` required?

No.

Use it when a substantial multi-Contract project benefits from machine-readable execution state.

## Is the Wiki normative?

No.

The Wiki explains ADP for humans. `ADP.md` is canonical.
