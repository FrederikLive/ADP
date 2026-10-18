# Core Model

> This page summarizes the work model. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

ADP separates **what the user wants** from **how an agent session happens to execute it**.

## Work hierarchy

```text
PROJECT
   │
   └── MILESTONE / OUTCOME
          │
          ├── WORKSTREAM
          │      │
          │      └── CONTRACT
          │             │
          │             ├── ATOMIC UNIT
          │             └── ATOMIC UNIT
          │
          └── VERIFICATION EVIDENCE
```

### Project

The durable product or system being built.

### Milestone / Outcome

A meaningful product or engineering state such as:

- functional MVP;
- production readiness;
- public release.

Milestones are outcomes, not arbitrary percentages or chat boundaries.

### Workstream

A logical area of related or parallel work, such as frontend, API, core engine, security, migration, or quality.

A Workstream normally does **not** need its own file.

### Contract

The primary durable unit of substantial engineering work.

A Contract normally defines:

- outcome;
- scope;
- out of scope;
- acceptance criteria;
- dependencies;
- plan;
- validation;
- risks and decisions;
- handoff state.

Small fixes do not need ceremonial Contract files when the user request itself is sufficient.

### Atomic Unit

The smallest coherent implementation step worth completing and validating before moving on.

Atomic Units are normally ephemeral execution steps, not permanent project documents.

### Evidence

Inspectable proof that work satisfies its acceptance criteria:

- tests;
- builds;
- static checks;
- integration validation;
- screenshots or UI automation;
- benchmark results;
- schema validation;
- migration checks.

## Why this matters

ADP deliberately does **not** make a conversation or model session the unit of work.

A Contract may span several sessions, and one session may complete several Contracts. The durable work belongs to the repository.

## Next

- [Autonomy and Checkpoints](Autonomy-and-Checkpoints.md)
- [Verification and Evidence](Verification-and-Evidence.md)
