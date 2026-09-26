# Changelog

## [Unreleased]

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
