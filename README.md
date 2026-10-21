# ADP — Agent Development Protocol

[![Validate](https://github.com/FrederikLive/ADP/actions/workflows/validate.yml/badge.svg)](https://github.com/FrederikLive/ADP/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Protocol Version](https://img.shields.io/badge/ADP-2.7.1-blue.svg)](VERSION)

**ADP (Agent Development Protocol)** is a vendor-neutral protocol for structuring software projects so capable AI coding agents can bootstrap, understand, build, test, verify, continue, recover, and hand work to another agent with minimal unnecessary human intervention.

The central design principle is:

> **The repository is durable project memory. Agent sessions are replaceable execution capacity.**

## Canonical specification

The normative protocol is:

**[`ADP.md`](ADP.md)** — full canonical specification

**[`ADP.min.md`](ADP.min.md)** — compact machine-consumption distribution

If `ADP.min.md` or any convenience template, example, integration guide, or adapter conflicts with `ADP.md`, **`ADP.md` wins**. See [`docs/MINIFIED.md`](docs/MINIFIED.md) for the compact distribution's compression contract.

## For AI coding agents

If this repository has been attached, cloned, mounted, vendored, or otherwise made available to you as development guidance:

1. Read [`AGENTS.md`](AGENTS.md).
2. Apply ADP.md's reading policy: read REQUIRED material, determine CONDITIONAL applicability, and follow every applicable normative requirement. Use [`ADP.min.md`](ADP.min.md) for context-constrained work, while consulting the full specification for applicable detail and disputes.
3. Treat `ADP.md` as the canonical protocol.
4. Apply ADP to the **target project** the user asked you to work on.
5. Do not modify this ADP repository unless the user is explicitly asking you to develop ADP itself.

A generic user prompt is:

```text
Use the Agent Development Protocol from the ADP repository available in this
workspace/context.

Read its AGENTS.md, then apply ADP.md's reading policy: read REQUIRED material, determine CONDITIONAL applicability, and follow every applicable normative requirement.

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

### Updating ADP in an existing project

Ask your coding agent **"Check ADP for updates"** for a read-only comparison, **"Update ADP"** for a safe authorized integration update, or **"Migrate to ADP version X"** for a compatibility-aware migration. The [ADP Project Update Guide](docs/UPDATING_ADP.md) describes copied-file, submodule, attached and remote-reference adoption without overwriting local project instructions. It is consulted only when requested; ADP never requires routine update checks.

### Example requests you can give an ADP-aware agent

The [ADP user-request catalogue](docs/COMMANDS.md) groups optional natural-language requests such as "Show project status", "Resume the project", "Verify current work", "Review external analysis", "Show Observatory" and "Check ADP for updates". These are **intent examples**, not slash commands, special agent tools or replacements for a project's actual executable commands.

### Optional: visualize an ADP project

[ADP-Observatory](https://github.com/FrederikLive/ADP-Observatory) is a separate, optional human-facing analyzer for ADP projects. Its Rust scanner and offline HTML dashboard run in the development executable. Experimental provenance-attested CI binaries exist, but an official installer and trusted automatic download-and-run launcher are **not yet released**. See [the Observatory usage and planned launcher guide](docs/OBSERVATORY.md). No Observatory installation or additional project metadata is required for ADP conformance.

## What ADP establishes

ADP defines nine core protocols:

1. **Bootstrap Protocol** — how a new or existing repository is initialized.
2. **Autonomy Protocol** — what an agent may do without repeated approval.
3. **Work Protocol** — Project → Milestone → Workstream → Contract → Atomic Unit → Evidence.
4. **Delegated & Concurrent Execution Protocol** — when to delegate, how concurrent mutation is isolated, and how delegated results are reconciled.
5. **Verification Protocol** — how work is proven correct.
6. **Continuity Protocol** — how project state survives context windows and agent replacement.
7. **Transition Transparency Protocol** — how meaningful development boundaries are shown to humans without turning ordinary continuation into approval gates.
8. **External Analysis Intake & Reconciliation Protocol** — how external reports are independently validated, dispositioned, tracked, and verified.
9. **Escalation Protocol** — when human involvement is genuinely required.

## Repository map

```text
ADP.md                         Canonical protocol
ADP.min.md                     Compact machine-consumption distribution
AGENTS.md                      Agent entrypoint for this repository
README.md                      Human entrypoint

docs/
├── USING_ADP.md               How to consume ADP from other projects/agents
├── UPDATING_ADP.md            On-demand existing-project ADP updates
├── COMMANDS.md                Optional user-to-agent request catalogue
├── CONFORMANCE.md             Conformance model
├── COMPATIBILITY.md           Agent/harness integration guidance
├── VERSIONING.md              Protocol versioning rules
├── GLOSSARY.md                ADP terminology
├── RESEARCH.md                Research rationale
└── WIKI.md                    Wiki source/publishing maintenance

wiki/                          Version-controlled source for the GitHub Wiki
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
