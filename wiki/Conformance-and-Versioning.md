# Conformance and Versioning

> This page is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

## Conformance is behavioral

A project is not ADP-conformant merely because it contains files named `AGENTS.md`, `STATUS.md`, or `CONTINUITY.md`.

ADP conformance is about behavior.

### ADP-aware

The agent can reliably locate and read the applicable protocol.

### ADP-bootstrapped

The repository has an appropriate control plane, executable command surface, verification expectations, safe Git/file handling, and continuity behavior.

### Continuity-ready

A cold successor can recover:

- active objective;
- current state;
- active Contract;
- worktree state;
- verification state;
- next recommended phase;
- exact next action.

### Transition-transparent

The user can determine:

- what meaningful outcome completed;
- what was verified;
- the current Milestone;
- the recommended next phase;
- why it is next;
- whether execution will CONTINUE, CHECKPOINT, or COMPLETE.

### Delegation-safe

When delegation/concurrent mutation is used:

- relevant user intent survives delegation;
- concurrent writers are isolated;
- mutable ownership is controlled;
- worker completion is reconciled before authoritative acceptance;
- unresolved unlanded work is preserved.

**Delegation itself is optional.** A single-agent project can be fully ADP-conformant.

### Reading-efficient

Agents distinguish REQUIRED, CONDITIONAL, and REFERENCE material, establish applicability before skipping specialized sections, and never make normative requirements optional merely by deferring explanatory text.

### Analysis-reconciled

External reports are untrusted evidence, not implementation authority. Each finding is independently validated and dispositioned with rationale; accepted work is tracked and verified, and the original source and reconciliation remain traceable. Deferred and unresolved findings remain visible.

## Semantic versioning

ADP uses:

```text
MAJOR.MINOR.PATCH
```

- **MAJOR** — incompatible normative protocol change.
- **MINOR** — backwards-compatible normative addition.
- **PATCH** — non-breaking clarification/correction.

Long-running projects should record/pin the ADP version they adopted.

## Current release

**2.7.1 — 2026-10-17**

Additions:

- Standardized external-analysis intake identifiers, filename conventions, separate reconciliation records, and archive traceability.

**2.6.0 — 2026-10-17**

Additions:

- Reading and conformance policy for efficient loading without weakening normative requirements.
- External Analysis Intake & Reconciliation Protocol.

**2.5.0 — 2026-09-27** introduced Delegated & Concurrent Execution.

## Canonical and derived artifacts

The canonical specification is `ADP.md`.

Derived artifacts such as:

- `ADP.min.md`;
- templates;
- examples;
- this Wiki;

must remain aligned with the canonical protocol.

If a derived artifact conflicts with `ADP.md`, **ADP.md wins**.

## Validation

The ADP repository includes:

```bash
python scripts/validate.py
```

The validator checks repository structure, protocol/version alignment, compact-distribution semantic anchors, JSON validity, and local Markdown links.
