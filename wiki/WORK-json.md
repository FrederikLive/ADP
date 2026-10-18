# WORK.json

> This page is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) and the repository schema are normative.

For substantial, long-running projects with multiple Contracts, ADP may use:

```text
.project/WORK.json
```

It is a **machine-readable execution ledger**, not a requirements database.

## Purpose

`WORK.json` helps agents deterministically answer:

- which Contract is active;
- which Contracts are ready, blocked, or verified;
- what dependencies exist;
- which Milestone is active;
- what should happen next;
- when useful, how an active Contract is being executed.

## Typical shape

```json
{
  "schema_version": 1,
  "project": "example",
  "active_milestone": "M1",
  "active_contract": "WORK-002",
  "next_milestone": "M1",
  "next_contract": "WORK-003",
  "contracts": [
    {
      "id": "WORK-002",
      "title": "Authentication",
      "workstream": "Platform",
      "status": "in_progress",
      "depends_on": ["WORK-001"],
      "contract_file": "docs/work/WORK-002.md",
      "execution": {
        "mode": "delegated",
        "mutation": "mutating",
        "branch": "adp/WORK-002"
      }
    }
  ]
}
```

## Contract statuses

ADP currently recognizes:

- `candidate`
- `ready`
- `in_progress`
- `blocked`
- `implemented`
- `verifying`
- `verified`
- `deferred`
- `cancelled`

A Contract must not be marked `verified` without evidence.

## Execution metadata

ADP 2.5.0 optionally allows:

```json
"execution": {
  "mode": "direct | delegated",
  "mutation": "read_only | mutating",
  "branch": "stable branch reference or null"
}
```

Use this only when it improves durable recovery.

Do **not** turn `WORK.json` into a runtime process registry.

Avoid persisting:

- process IDs;
- terminal pane IDs;
- temporary session IDs;
- watcher internals;
- transient queues/inboxes;
- harness-specific noise with no cold-recovery value.

## Authority

`WORK.json` owns execution state only.

It does not replace:

- `PRODUCT.md` for product requirements;
- Contract Markdown for rich rationale/acceptance;
- `ARCHITECTURE.md` for system design;
- `CONTINUITY.md` for the current resume packet.

## Schema

The repository provides:

```text
schema/work.schema.json
```

Tools may validate ledgers against it.
