# Repository Control Plane

> This page is explanatory. [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md) is normative.

ADP uses a small set of repository files to keep project knowledge durable without turning Markdown into a second implementation layer.

The principle is:

> **One source of truth per concern.**

## Typical control plane

```text
AGENTS.md
README.md

docs/
├── PRODUCT.md
├── ARCHITECTURE.md
├── QUALITY.md
├── STATUS.md
├── CONTINUITY.md
├── IDEAS.md
├── DESIGN.md        # when applicable
├── SECURITY.md      # when applicable
├── DELIVERY.md      # when applicable
├── adr/             # significant historical decisions
└── work/            # substantial work contracts

.project/
└── WORK.json        # optional machine-readable execution ledger
```

Equivalent existing documents may be preserved instead of forcing these exact filenames.

## Ownership

### AGENTS.md

The concise operational entry point for coding agents.

It owns:

- repository navigation;
- standard commands;
- important engineering invariants;
- autonomy/safety rules;
- documentation routing;
- definition of done.

It should be a router, not an encyclopedia.

### PRODUCT.md

Owns the **what and why**:

- users;
- problem;
- goals/non-goals;
- workflows;
- requirements;
- acceptance criteria;
- domain terms;
- product assumptions.

### ARCHITECTURE.md

Owns the current technical system:

- components;
- boundaries;
- data flow;
- persistence;
- APIs;
- integrations;
- runtime/deployment topology;
- failure behavior;
- observability;
- architectural invariants.

### QUALITY.md

Answers:

> What evidence is enough to consider a change correct?

It owns testing strategy, required checks, CI gates, security/accessibility/performance validation where relevant.

### STATUS.md

A short snapshot of current project state:

- current Milestone/phase;
- recently completed;
- in progress;
- blocked;
- next recommended phase;
- known issues;
- last verified state.

Not a diary.

### CONTINUITY.md

The current cold-resume packet for a successor agent.

See [Continuity and Handoffs](Continuity-and-Handoffs.md).

### IDEAS.md

Unapproved future opportunities.

An idea is **not** committed scope.

### DESIGN.md

Created when the project has meaningful UI/UX.

### SECURITY.md

Created when the project meaningfully involves auth, sensitive data, secrets, public services, multi-tenancy, payment, or other security-sensitive behavior.

### DELIVERY.md

Created when software is packaged, deployed, published, released, or installed operationally.

### ADRs

Historical records for architecture decisions that are significant, expensive to reverse, or likely to be questioned later.

### Work Contracts

Use `docs/work/<contract>.md` only for work substantial enough to benefit from durable acceptance criteria and handoff state.

### WORK.json

Optional machine-readable operational state for long-running/multi-Contract work.

See [WORK.json](WORK-json.md).

## Markdown vs executable enforcement

ADP prefers executable enforcement when a machine can reliably enforce a rule:

```text
formatting       → formatter
style            → linter
types            → compiler/type checker
behavior         → tests
schemas          → schema validation
dependency state → manifest + lockfile
merge gates      → CI
```

Markdown should hold intent, architecture, constraints, tradeoffs, safety rules, and information requiring judgment.

## Avoid duplicate truth

Do not keep competing versions of the same fact in:

- README;
- AGENTS.md;
- SYSTEM.md;
- RULES.md;
- task files;
- generated worker briefs.

Link to the canonical owner instead.
