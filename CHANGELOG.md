# Changelog

## [Unreleased]

### Documentation
- Rebranded the optional human request catalogue as **ADP Actions** while retaining `docs/COMMANDS.md` as its stable link; added evidence-based, read-only examples for project blockers, decision rationale, documentation consistency and changes since a milestone. Kept the full guide on demand, not in normal agent context.
- Added [docs/UPDATING_ADP.md](docs/UPDATING_ADP.md), a non-normative, user-requested guide for checking/updating/migrating ADP integrations in copied-file, pinned-submodule, mounted and remotely referenced projects while preserving local instructions.
- Added [docs/COMMANDS.md](docs/COMMANDS.md), a non-binding human-to-agent request catalogue covering project status, verification, handoff, ADP maintenance, external analysis and optional Observatory.
- Added tiny conditional update/command-discovery pointers to full/compact ADP and the generated AGENTS template; aligned human usage/versioning docs and repository validation. No new core protocol, mandatory manifest or routine background update checking.
- Added an optional, user-triggered Observatory Agent Skill discovery hint in the portable/compact ADP descriptions and generated AGENTS.md template. Full launch and installation logic stays in the Observatory repository; no normative requirement or new project file was added.
- Added an optional, non-normative ADP-Observatory human usage guide and linked it from the README and ADP usage documentation. The tool is not a required part of ADP, and proposed launch commands are explicitly marked as not yet released.

## [2.7.1] - 2026-10-18
### Fixed
- Unified Git authorization across greenfield bootstrap and checkpoint commits, separating local from remote permissions.
- Prohibited self-authored authority and introduced stable authorization decisions.
- Added Git continuity guidance and eight static policy-conformance scenarios.


## [2.7.0] - 2026-10-17
### Added
- External-analysis intake naming and storage convention for reports with descriptive, generic, generated, or obscure filenames and multiple text formats.
- Separate normalized reconciliation records, exact original-filename/path metadata, collision-safe identifiers, and archive-copy integrity checks.
- Default adaptable external-analysis directory layout, subject to repository conventions, authorization, privacy, and retention policy.

## [2.6.0] - 2026-10-17
### Added
- Reading and conformance policy distinguishing REQUIRED, CONDITIONAL, and REFERENCE material while preserving all applicable normative requirements.
- External Analysis Intake & Reconciliation Protocol for independent validation, finding dispositions, traceability, canonical integration, authorization boundaries, and verification.
- Reusable external-analysis reconciliation record template and explicit completion criteria.

### Changed
- Consolidated repeated ADP identity/scope prose into one authoritative section.
- Updated bootstrap prompts and directives to follow the reading policy.
- Synchronized compact distribution and repository metadata for ADP 2.6.0.

## [2.5.0] - 2026-09-27
### Added
- Delegated & Concurrent Execution protocol for safe, proportional multi-agent execution without making delegation mandatory.
- Direct-vs-delegated execution-topology guidance: use the smallest topology that materially improves delivery.
- User/product-intent preservation across delegation and compact generated Execution Briefs.
- Delegated mutation postures: `READ_ONLY` and `MUTATING`.
- Concurrent mutation isolation, scope ownership/collision control, and serialization fallback when isolation is unavailable.
- Delegated-result reconciliation: worker completion is provisional evidence until checked against the Contract, canonical state, diff/artifacts, and required verification.
- Explicit preservation rule for unresolved unlanded delegated work.
- Optional durable per-contract execution metadata in `.project/WORK.json` and its schema.
- Delegation-safe conformance, compatibility, glossary, research, compact-distribution, and validation guidance.
- Version-controlled GitHub Wiki source covering usage, core concepts, autonomy, delegated execution, verification, continuity, transition transparency, control-plane ownership, WORK.json, conformance/versioning, and FAQ.

### Changed
- Generated `AGENTS.md` guidance now includes concise delegation/concurrency invariants.
- Continuity guidance now records recoverable delegated/concurrent state without persisting transient orchestration noise.
- Human-facing reporting for delegated execution is routed through the existing Transition Transparency model.
- Harness guidance prefers event-driven completion/escalation over model-driven polling when available.

## [2.4.0] - 2026-09-23
### Added
- Transition Transparency protocol with concise user-facing Transition Briefs at meaningful Contract/Milestone boundaries.
- Explicit distinction between the human-scale Next recommended phase and agent-scale Exact next action.
- Transition execution states: `CONTINUE`, `CHECKPOINT`, and `COMPLETE`.
- Optional `next_milestone` and `next_contract` fields in `.project/WORK.json` and its schema.
- Transition-transparent conformance definition.
- `ADP.min.md`: semantically compressed machine-consumption distribution.
- `docs/MINIFIED.md`: compression contract and maintenance guidance.
- Validation for compact/full version alignment, semantic anchors, and size ceiling.

### Changed
- `STATUS.md` now owns the next recommended phase, rationale, and first action.
- `CONTINUITY.md` now distinguishes directional next-phase context from the exact cold-resume action.
- Generated `AGENTS.md` guidance reports meaningful transitions without creating routine approval gates.
- Next-work selection prioritizes dependency-ready milestone progress, important unblockers, and material risk reduction before optional polish.

## [2.3.0] - 2026-09-21
### Added
- Public open-source ADP repository.
- Universal `AGENTS.md` entrypoint.
- Repository/submodule/single-file consumption.
- Templates, schema, examples, conformance docs, validation, and CI.
### Changed
- ADP consistently expands to **Agent Development Protocol**.

## [2.2.0] - 2026-09-21
- Authorization Envelope, HIGH-autonomy continuation, work hierarchy, checkpoints, retry budgets, continuity protocol, optional WORK.json, cold-start procedure.
