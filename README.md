# ADP — Agent Development Protocol

[![Validate](https://github.com/FrederikLive/ADP/actions/workflows/validate.yml/badge.svg)](https://github.com/FrederikLive/ADP/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Protocol Version](https://img.shields.io/badge/ADP-2.3.0-blue.svg)](VERSION)

**ADP (Agent Development Protocol)** is a vendor-neutral protocol for structuring software projects so capable AI coding agents can bootstrap, understand, build, test, verify, continue, recover, and hand work to another agent with minimal unnecessary human intervention.

The central design principle is:

> **The repository is durable project memory. Agent sessions are replaceable execution capacity.**

## Canonical specification

The normative protocol is:

**[`ADP.md`](ADP.md)**

If any convenience template, example, integration guide, or adapter conflicts with `ADP.md`, **`ADP.md` wins**.

## For AI coding agents

If this repository has been attached, cloned, mounted, vendored, or otherwise made available to you as development guidance:

1. Read [`AGENTS.md`](AGENTS.md).
2. Read [`ADP.md`](ADP.md) completely before bootstrapping a target project.
3. Treat `ADP.md` as the canonical protocol.
4. Apply ADP to the **target project** the user asked you to work on.
5. Do not modify this ADP repository unless the user is explicitly asking you to develop ADP itself.

A generic user prompt is:

```text
Use the Agent Development Protocol from the ADP repository available in this
workspace/context.

Read its AGENTS.md and then ADP.md completely.

We are building:
<describe the project, users, constraints, and desired outcome>

Bootstrap and develop the target project according to ADP. Work with HIGH
autonomy inside the authorization envelope. Do not stop for routine
"continue" acknowledgements. Persist continuity state so another agent can
resume if your context ends.
```

## Ways to use ADP

### 1. Give the entire ADP repository to an agent

This is the preferred method when your coding harness can attach or mount another repository.

The root `AGENTS.md` deliberately routes the agent to `ADP.md`.

### 2. Add ADP as a Git submodule

Example:

```bash
git submodule add https://github.com/FrederikLive/ADP.git .adp/protocol
```

Then tell the target project's agent:

```text
Read .adp/protocol/AGENTS.md and .adp/protocol/ADP.md before bootstrapping
this project.
```

### 3. Copy the single portable file

Copy `ADP.md` into a new project root and point the agent directly to it.

This preserves ADP's original single-file bootstrap model.

### 4. Reference the GitHub repository

If the agent has GitHub/web access, point it to:

```text
https://github.com/FrederikLive/ADP
```

and instruct it to read `AGENTS.md` followed by `ADP.md`.

See [`docs/USING_ADP.md`](docs/USING_ADP.md) for detailed integration patterns.

## What ADP establishes

ADP defines six core protocols:

1. **Bootstrap Protocol** — how a new or existing repository is initialized.
2. **Autonomy Protocol** — what an agent may do without repeated approval.
3. **Work Protocol** — Project → Milestone → Workstream → Contract → Atomic Unit → Evidence.
4. **Verification Protocol** — how work is proven correct.
5. **Continuity Protocol** — how project state survives context windows and agent replacement.
6. **Escalation Protocol** — when human involvement is genuinely required.

## Repository map

```text
ADP.md                         Canonical protocol
AGENTS.md                      Agent entrypoint for this repository
README.md                      Human entrypoint

docs/
├── USING_ADP.md               How to consume ADP from other projects/agents
├── CONFORMANCE.md             Conformance model
├── COMPATIBILITY.md           Agent/harness integration guidance
├── VERSIONING.md              Protocol versioning rules
├── GLOSSARY.md                ADP terminology
└── RESEARCH.md                Research rationale

templates/                     Convenience templates derived from ADP.md
schema/work.schema.json        Optional WORK.json schema
examples/                      Example prompts and integration snippets
scripts/validate.py            Dependency-free repository validator

.github/
├── copilot-instructions.md    GitHub Copilot adapter
├── workflows/validate.yml     CI validation
└── ...                        Contribution templates
```

## Open source

ADP is released under the **MIT License**.

**Author:** Frederik Smith  
**Email:** w5zk8yjto@mozmail.com

See [`LICENSE`](LICENSE).

## Contributing

Protocol improvements are welcome.

Before proposing a normative protocol change, read:

- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`docs/VERSIONING.md`](docs/VERSIONING.md)

## Name

In this repository, **ADP always means Agent Development Protocol**. Because the acronym is not globally unique, use the full name on first reference in external writing.
