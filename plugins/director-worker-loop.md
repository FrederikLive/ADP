# Director–Worker Loop (DWL) — optional ADP plugin proposal

> **Status:** DESIGN PROPOSAL — not an installed, activated, or normative ADP feature.
>
> **Basis:** Agent Development Protocol (ADP) 2.8.0. This document records the intended behavior and rationale before the ADP plugin mechanism itself is designed.
>
> **Scope of this proposal:** Director-led engineering, manual-to-autonomous Directives/Handoffs, Evidence-based acceptance, and dynamic capability-aware allocation across one or more Workers.
>
> **Authority:** ADP.md remains canonical. Nothing here grants repository-write, push, API-spending, credential, merge, deployment, production, or other permissions. The eventual plugin must remain opt-in.

## 1. Problem, intent, and success criteria

### Actual workflow that motivated this proposal

A human establishes the product goal, constraints, and delegation boundary. A relatively strong cloud AI acts as an **AI Director / Lead**. It examines the project's real state, decides what engineering outcome comes next, and writes a durable numbered Directive (typically D01, D02, ...). A local AI acts as **Worker**: it reads the Directive, reconciles it with ADP Contracts and current code, implements within scope, runs checks, records **Evidence**, and creates a **Handoff**. Today the human manually carries that Handoff back to the Director, who audits the code, actual test results, and acceptance criteria before accepting work or issuing a remediation/next Directive.

This pattern has been exercised in the Trumpd-v2 project. It produced useful outcomes, including independent security defect discoveries, RED/GREEN remediation instructions, exact-source review packets, and explicit separation between worker-complete and independently accepted work. It also exposed coordination weaknesses: stale work pointers, branch/PR lineage differing from default main, model names in Directive titles that did not match the actual executor, CI not run for external reasons, and substantial but not-yet-integrated evidence.

### What the human actually wants

1. **A stronger model decides and verifies; a less costly/locally available model does much of the implementation.** Roles describe responsibilities, not an immutable hierarchy of model brands.
2. **The Director makes ordinary, reversible engineering decisions.** The human is contacted only for meaningful reserved decisions, genuine hard checkpoints, or a material ambiguity outside delegated authority. The Director judges significance *within* enforceable human-set limits, never expands those limits.
3. **A Directive is actionable, contextual and durable.** It carries purpose and rationale, not merely a shallow task list.
4. **A Worker does real engineering, not performance of completion.** The code, diffs, tests, limitations, and Evidence are the substance of the Handoff.
5. **The Director independently reconciles the result.** Worker confidence, self-review, a passing unit test, or a green branch does not alone establish acceptance of the integrated objective.
6. **Continuation becomes automatic where the runtime genuinely supports it.** Minimize repetitive copy/paste and "continue" prompts without bypassing authorization or pretending ADP Markdown is a running daemon.
7. **One Director can coordinate many interchangeable Workers.** Assign tasks dynamically using verifiable capabilities, tool access, cost/resource limits, dependencies and risk, with optional specializations rather than fixed Worker identities.
8. **ADP stays small and usable without this feature.** Reuse existing ADP mechanisms; no compulsory orchestrator, queue, agent registry, plugin install, persistent conversation transcript, or extra files for ordinary single-agent projects.

**Success:** A new authorized Director or Worker can reconstruct the objective and exact execution/review state from the repository; eligible work progresses with few unnecessary human interruptions; material defects and unknowns remain visible; parallel work integrates safely; disabling the feature leaves ordinary ADP unaffected.

### Explicit non-goals

- Replacing ADP's Authorization Envelope, Contracts, Verification, Continuity, Delegation, or Escalation Protocols.
- Assuming every project needs multiple agents, a powerful cloud model, a local model, or a single vendor.
- Requiring agent-to-agent chat, a persistent background service, OpenRig, Pi, GitHub PRs, paid APIs, or a particular transport.
- Making a Directive a competing canonical product/architecture source or turning each atomic unit into a permanent document.
- Conflating autonomous engineering continuation with automatic merge, release, deployment, spending, credential handling or production actions.
- Designing the eventual **ADP plugin installer, discovery manifest, bootstrap selection UI, dependency resolution, or full plugin governance now**. Those are separate decisions.

## 2. Relationship to existing ADP (reuse; do not duplicate)

This proposal extends, rather than redefines:

| ADP foundation | DWL use |
| --- | --- |
| Authorization Envelope, Autonomy and hard/soft checkpoints | Human-set scope and exception-driven escalation |
| Project → Milestone → Workstream → Contract → Atomic Unit → Evidence | Contracts remain the engineering units; Evidence proves acceptance |
| Delegated & Concurrent Execution / Execution Brief | Directives supply a durable program-level envelope; bounded worker assignments are projections |
| Capability-Aware Agent Assignment and Failover (2.8.0) | Worker eligibility, model/provider selection, bounded successor handoff |
| Verification / independent reconciliation | Worker reports are provisional; Director validates actual source and checks |
| docs/CONTINUITY.md and optional .project/WORK.json | Recovery and execution pointers, not duplicate product requirements |
| docs/STATUS.md, docs/adr/ and canonical docs | Human status, durable decisions, and authoritative product/design/security facts |

Read ADP.md and applicable canonical documents first; on conflict, the higher-priority authority wins and the Directive/Handoff must be corrected. Project policy may constrain or disable DWL. When the plugin is absent, **normal ADP behavior is unchanged**.

**Minimum extra information:** a Directive and a Handoff for substantial cross-agent cycles; a review verdict may be appended immutably or recorded separately if recovery/audit requires it. A tiny task need not generate multiple permanent files. Reuse existing Contract evidence folders and current status/continuity rather than copying logs into a parallel documentation tree.

## 3. Clear authority and identity model

| Actor | Responsibility | Limitation |
| --- | --- | --- |
| **Human Owner** | Product goals, delegation envelope, reserved decisions, irreversible/high-consequence authority | Never treated as having approved silence |
| **AI Director** (Lead/coordinator) | Understand intent; prioritize Contracts; issue Directives; allocate work; assess risks; independently reconcile Evidence; accept/reject/partially accept; select next work | Cannot self-grant or enlarge human authority; one active logical Director at a time when mutating authoritative coordination state |
| **Worker(s)** | Reconcile assignment with repository; implement and verify within bounded scope; preserve unlanded work; submit truthful Handoff | Cannot self-accept independent gates, rewrite higher authority, or mutate another lane's work |
| **Optional Reviewer Worker** | Read-only or separately isolated independent audit, adversarial tests and review evidence | Model-name difference alone is not independence; Director remains responsible for disposition within scope |
| **Optional Coordination Runtime** | Discover capacities, schedule eligible work, enforce resource/lease/permission boundaries, deliver events, recover state | Execution machinery, **not** a source of product or human authority |

**Terminology:** In an existing repository "Director" may mean the *human*, whereas in this proposal it means the *AI Lead*. The owner/AI roles must be stated explicitly; do not silently reinterpret historical decision files. The stable facts are **role**, **agent instance**, **actual model/provider/runtime at execution**, and **assignment**—four different concepts. A Directive addressed to "Qwen" does not prove Qwen executed it.

The Director's ordinary engineering discretion includes reversible implementation choices, scoped refactors, appropriate tests and Contract ordering inside the envelope. Escalation is required for material irreversible/product-policy/budget/security/privacy/legal decisions and any action ADP defines as a hard checkpoint. Block only dependent work; continue authorized independent work. The runtime must enforce consequential permissions outside model prose.

## 4. One complete Director–Worker cycle

1. **Reconcile before assigning.** Director reads authoritative instructions, current Contracts, status, continuity, Git branches/PR lineage, open gates and Evidence. Default-branch HEAD alone may be stale. Verify the intended integrated/source lineage; never silently treat a newer draft branch as accepted.
2. **Issue a Directive.** Identify goal, why it matters, Contract IDs, constraints, owned scope, dependencies, acceptance gates, required Evidence, risk, assignment/review boundary and hard-stop conditions. Record its source baseline.
3. **Allocate bounded assignments.** For one Worker, use a direct/delegated Execution Brief; for many Workers, issue non-overlapping assignments linked to the same Directive. A Directive need not be repeated for every Worker.
4. **Execute without routine interruption.** Worker checks current source and the brief, implements, runs applicable tests, records accurate results and checkpoints. If a hypothesis is obsolete, report it with source evidence rather than blindly executing stale instructions.
5. **Submit Handoff plus Evidence.** Worker names the actual executor, branch, base/result revision, modifications, test observations, omissions, risks, unlanded state, blockers, decisions and recommended next action. Submission is **provisional**, not acceptance.
6. **Reconcile and review.** Director inspects exact diffs, acceptance criteria, canonical rules, Evidence, dependency and integration state. Independently rerun material/security-critical checks or commission genuinely independent review. Workers must not close their own independent review gate.
7. **Record verdict.** Outcomes: **ACCEPTED**, **CHANGES_REQUESTED**, **PARTIALLY_ACCEPTED**, **BLOCKED**, or **ESCALATE_TO_HUMAN**. State which Contracts and exact revisions the verdict covers. Keep rejected findings and gates visible.
8. **Continue or stop safely.** On acceptance, select the next eligible goal or issue the next Directive. On remediation, target the specific findings rather than reimplementing everything. If blocked, advance unrelated authorized Contracts. Stop for a genuine hard gate, completed objective or explicit stop instruction.

**Review cadence is risk-based:** a Worker may finish several atomic units or compatible Contracts under one Directive. Do not force a premium-model review on every small reversible edit. A major architecture/security/migration change warrants a closer review; a high-consequence external operation remains under established human gates.

## 5. Directive, Handoff and decision conventions (proposal only)

Suggested optional paths for consuming projects *if enabled*:

- docs/directives/D01.md, D02.md, ... — durable program-level instructions.
- docs/handoffs/D01-H01.md, D01-H02.md, ... — one or more submissions per Directive.
- Existing docs/work/ and Evidence locations — unchanged.
- Existing docs/CONTINUITY.md and .project/WORK.json — updated at meaningful boundaries.
- Existing docs/adr/ and canonical domain docs — authoritative enduring decisions; do not bury product policy only in Directives.

**Numbering:** Directives are project-scoped, monotonically issued D01, D02, ...; use explicit revisions such as D01-R1 where refining the same scope is clearer. Handoff IDs link to one Directive and increment independently. Do not reuse Directive D-numbers as unqualified decision identifiers: a distinct DEC-* identifier or explicit namespace avoids conflict with existing projects that already name Director decisions D01–D08. Existing repositories may map their current filenames without destructive renaming.

**Directive minimum fields:** ID/revision/status; issued-by role and baseline revision; mission and user/product rationale; referenced Contract(s); dependencies and permitted work; out-of-scope; safety/spending/deployment gates; required verification and Evidence; Handoff trigger; escalation conditions; authorized continuation. References beat duplication.

**Worker Handoff minimum fields:** Directive/assignment/Contract refs; actual agent/model/harness; base and result Git SHA/branch; changed paths and unlanded state; acceptance-criterion-to-evidence mapping; executed check, environment, result, artifact location; FAILED/NOT RUN/NOT AVAILABLE checks; incomplete work; decisions taken and requested; precise next action. Use ADP's existing explicit verification semantics (**VERIFIED, FAILED, NOT RUN, NOT AVAILABLE**) and avoid inventing a success state.

**Review record minimum fields:** Directive/Handoff refs and reviewed immutable revision(s); reviewer identity and independence basis; inspected Evidence; acceptance disposition and findings; remaining gates/decisions; authorized next action. A review on SHA X does not automatically certify later SHA Y. No forged CI receipts or statements that planned tests have already run.

## 6. Dynamic capability-aware multiple Workers

### Why dynamic, not permanently fixed Workers

Task fit, provider access, GPU availability, review needs, and load vary over time. Assigning a Worker a permanent "frontend" or "coder" identity unnecessarily wastes capacity and makes model changes painful. **Preferred specializations are hints; assignment is per Contract or bounded work package.** The system must still operate with one Worker and one shared model server.

### Registration and eligibility

An optional Worker pool advertises stable agent ID, current role capability, model/provider/runtime as observed, tool access, repository/data access, supported languages/tasks, available execution environment, resource demands, and measured history. Availability and health are **runtime facts**, not canonical product truth. Separate claimed from observed capabilities; expose AVAILABLE, UNAVAILABLE, UNKNOWN. Avoid permanent model-brand rankings.

**First filter hard eligibility (never trade for a score):** delegated authority, privacy/data residency, secrets access, tool/command availability, required context/resources, approved provider and spending, dependency and review independence, writable workspace isolation, and shared resource constraints. Unknown hard eligibility blocks assignment until resolved.

**Then rank eligible Workers** using proportionate, configurable considerations: task capability/fit, verified reliability, current availability, resource/time/cost efficiency, and continuity/locality. Preference weights are optional examples, not normative fixed percentages; record a short rationale for consequential assignments. Prefer the smallest safe execution topology. The AI Director may select a different eligible Worker with recorded reasons but cannot override hard constraints.

**Observed reliability** means outcomes: accepted Contracts, review defects, escaped regressions, evidence completeness and recovery quality—not unsupported intelligence scores. Avoid feedback loops that discriminate against Workers merely because they received harder assignments; compare by risk and evidence quality.

### Scheduling, resources and integration

- ADP Contract dependency order governs the ready queue, not numeric ID alone. Parallelism is appropriate only if acceptance, scope, integration order, and shared-resource constraints permit it.
- Each mutating Worker uses an **isolated writable worktree/checkout and change lineage**. A different branch name in one shared working directory is insufficient. Read-only investigations may share safe read access.
- Declare owned paths or mutation surfaces; serialize collisions or specify staged integration ownership. Account separately for databases, migrations, queues, ports, test fixtures, browser sessions and external services.
- Resource admission is based on actual capacities. Multiple logical Workers may share **one** local GPU/llama.cpp inference endpoint; a conservative single heavy-inference slot may be appropriate while CPU-side tests continue in parallel. Never assume a second GPU, paid API or unlimited concurrency.
- Integrate only after lineage/rebase conflicts and unlanded work are reconciled. **Worker checks on separate branches ≠ combined integration checks.** Run applicable tests at the exact integrated revision before declaring an integrated Contract accepted.
- Permit a Director to issue one Directive with assignments D01-A, D01-B, etc., including explicit dependencies, not one permanent Directive per Worker. A review specialist may be assigned a separate independent lane.

### Separate state dimensions; avoid status explosion

Keep the existing ADP Contract state (candidate/ready/in_progress/implemented/verifying/verified/blocked/etc.) distinct from an **optional transient assignment lifecycle** (queued → leased → running → handoff_submitted → review_pending → closed, with change-request/failure/retry branches), and distinct from a **review verdict** (accepted/changes requested/partial/blocked/escalated).

Do not encode every combination as a new Contract status string. Machine-readable metadata should contain only stable links and recovery-useful facts; live queue delivery attempts, session IDs, tokens, rate-limit counters and process leases belong to the runtime. A proposal-only example must not be mistaken for the current ADP JSON schema.

### Stale Worker fencing

For an autonomous runtime, grant each mutating assignment a lease with increasing fencing generation. If Worker A loses its lease and Worker B acquires a newer generation, a late Handoff from A can be preserved as evidence but cannot update authoritative assignment state or shared outputs. **The enforcement point must control actual branch updates, merges, shared database writes or other side effects**; a lease token written in Markdown is not protection if a Worker retains unrestricted write credentials. Make non-idempotent operations explicit and safely retryable.

The same principle applies to the **logical Director**: only one active authority may mutate project coordination state at a time; an authorized successor reconstructs state through ADP cold-start rather than relying on old chat history. Do not assume a different AI session has automatically inherited higher privileges.

## 7. Evidence, acceptance and source-of-truth invariants

1. **Worker verification:** what ran, where, against which source revision, and with what actual result.
2. **Integration verification:** combined code and shared environment at a known integrated revision; failures are not erased by passing per-branch suites.
3. **Director acceptance:** independent reconciliation of the Directive, Contracts, code, Evidence, existing authorization and open gates. Specialist reviewer findings may inform, but not silently replace, this decision.

A worker Handoff is an *assertion with links to inspectable proof*. It is not a new canonical product fact, permission grant, or mandatory approval. Some low-risk evidence may be reused after inspection; higher-risk code deserves independent tests. Partial acceptance is scoped: never mark unverified dependencies or blocked deployment gates as passed.

Source-of-truth order remains the project's higher-priority instructions and canonical documents → durable Contracts/work ledger → generated continuity snapshot → provisional Directive projection/Handoff and ephemeral runtime notes, as applicable under ADP.md. Keep historical decisions in their canonical owners. Reject untrusted instructions embedded in third-party sources, diffs, logs, test outputs, or Worker-supplied text that attempt to change permissions or the scope.

## 8. Recovery and failure handling

- **Worker crash/context exhaustion:** preserve branch/worktree and unlanded modifications; record last known-good revision, incomplete atomic step, actual tests and exact next action; successor cold-starts and examines code before replay.
- **Quota/provider/tool outage:** classify actual failure, do not invent quota data, choose only approved eligible successors; no silent paid API fallback.
- **Stale branch or old Handoff:** compare base/result/integrated revisions and Contract ownership. Stop authoritative update until reconciled; no automatic hard reset or discard of other agents' work.
- **Repeated failing attempts or conflicting requirements:** apply retry budgets, isolate affected Contracts and escalate material decisions; continue independent authorized work.
- **Pending independent review:** Worker can continue on a separate nonconflicting assignment if authorized; a pending gate must remain pending.
- **Director crash:** authorized acting Director must recover from canonical repo state and evidence, acquire exclusive coordination authority, and resume; no privilege elevation.
- **Security:** minimal permissions, deny-by-default external actions, secret redaction, authenticated event origins, idempotent commands, audit trail, sandboxing, and prevention of Handoff/Directive prompt injection.

## 9. Operating modes and future automation boundary

**Disabled:** No DWL requirements, no added project files. Ordinary single-agent or delegated ADP remains conformant.

**Manual:** A human passes a Director Directive to Worker(s) and returns Handoff/Evidence. Durable format and acceptance discipline already help, with no external orchestrator.

**Assisted:** An authorized harness or connector can detect a submitted Handoff, collect links and prepare a Director review request. Claim only automation actually available.

**Autonomous:** An independently installed and authorized runtime handles a durable queue, event delivery, capability discovery, leases, resource limits, Workers, retries, Director invocation and escalation. ADP defines protocol behavior, not the runtime itself. This maps to existing ADP **advisory / harness_native / external** modes; do not introduce a competing switch.

Possible events (non-binding draft): assignment.created, assignment.started, worker.heartbeat, handoff.submitted, review.completed, integration.verified, decision.escalated. Events need IDs, authorization, idempotent consumption and revision references. Transport could be files, PRs, RPC, a message bus, or a future OpenRig adapter. **No transport is required by this document.** Prefer event notifications over continuous model polling when a runtime is present.

## 10. What the optional plugin should install — intentionally minimal

**Now (design capture):** this single Markdown proposal under ADP's plugins/ folder. It is not automatically included by bootstrap, not referenced by ADP.md, and not a valid plugin manifest. Do not alter the core ADP protocol merely to store the idea.

**If later approved:** the smallest selected-install footprint is a conditional operational guide plus concise Directive/Handoff/Review templates. A project may use its existing docs/work/Evidence/CONTINUITY/WORK.json locations. Only if machine-readable coordination is needed should the feature extend the existing optional .project/AGENT_POLICY.json and ledger schemas; any additional runtime files remain outside canonical project truth.

**Do not install by default:** orchestrator, daemons, queue DB, agent chat logs, provider secrets, per-task permanent reports, duplicate Contracts or project-wide role hierarchy.

Plugin discovery, activation, version compatibility, file ownership, dependency resolution, uninstall/migration, manifests, bootstrap menus, plugin conflict handling, and catalog listing are **explicitly deferred** until the separate ADP plugin architecture discussion. This file must not prejudge them.

## 11. Acceptance tests for a future implementation

| Scenario | Required outcome |
| --- | --- |
| Feature absent/disabled | No change to standard ADP bootstrap or conformance |
| Manual Director/Worker swap | Fresh agent resumes solely from repository references and actual Evidence |
| Directive conflicts with canonical project rule | Higher authority wins; conflict surfaced and Directive repaired |
| Worker self-certifies completion | Independent gate remains unaccepted |
| Old SHA Evidence used on new merged tree | Scope mismatch detected; integration checks required |
| Two Workers claim one mutating Contract | One effective owner; stale update rejected or harmlessly quarantined |
| Overlapping checkouts/shared test DB | Isolation, explicit ownership or serialized execution enforced |
| Worker crashes with unlanded changes | Changes preserved; replacement inspects and resumes without unsafe replay |
| Expired Worker returns after reassignment | Fencing prevents authoritative overwrite |
| Director restart or simultaneous Directorship | No concurrent conflicting authoritative decisions |
| One GPU serves many logical Workers | Actual resource budget respected; safe work still progresses |
| Unknown provider availability/paid budget | No unauthorized automatic fallback |
| No eligible ready work / human hard checkpoint | Safe stop or escalation; no invented approval |
| Existing Trumpd-style split main/PR lineages | Correct active source and outstanding gates reconciled before assignment |

Candidate measures: first-pass independent acceptance, defects found by Director, escaped defects, time/cost per accepted Contract, human interruptions, stalled time, evidence completeness, merge conflicts, and recovery success. Compare risk-adjusted outcomes before treating any Worker/model as globally “better.”

## 12. Design rationale and decisions preserved

- **Why Director/Worker separation?** Concentrate expensive strategic reasoning and independent scrutiny where they add value while letting available Workers do sustained implementation.
- **Why not simply trust a stronger Worker?** Verification must be against code and Evidence; correlated blind spots and stale state remain possible with any model.
- **Why Evidence is separate from Handoff?** A Handoff summarizes and points to proof; tests, artifacts and exact source are proof. A summary cannot become its own validator.
- **Why one Director, many Workers?** Clear accountable technical reconciliation, flexible parallelism, and simpler human escalation; the Director itself remains replaceable, not a single model/vendor dependency.
- **Why dynamic assignments?** Availability, task characteristics, review independence and hardware change over time; fixed roles waste resources. Eligibility outranks performance scores.
- **Why not require a new scheduler in ADP?** ADP is a portable file/repository protocol. Manual operation already delivers value; automation is an optional implementation.
- **Why strict workspace isolation and fencing?** Parallel write collisions and late stale actors can silently destroy or corrupt valid work. Merely naming separate branches or writing lease metadata is insufficient.
- **Why preserve Contract/assignment/review distinctions?** "Implemented" can coexist with "independent review pending" and "release blocked"; a single done flag loses critical truth.
- **Why risk-based Handoffs?** Review every meaningful gate, not every tiny edit; avoid excessive premium-model calls, delay and document bloat.
- **Why keep plugin design separate?** The feature's **intent** should be stable before deciding distribution/installation mechanics. Users must choose additions, and core ADP must not swell with optional workflows.

## 13. Pending decisions (for the separate plugin discussion)

Only after agreeing on an ADP-wide plugin mechanism should we decide: plugin file/folder layout, descriptor/manifest schema (if any), explicit enablement and conflict behavior, selected bootstrap installation, version compatibility, update/uninstall policy, and catalog format. No selection here implies install authorization.

**Current state:** proposal saved for discussion only. No modifications to ADP.md, ADP.min.md, AGENTS.md, schemas, validators, templates, README, version, changelog, or target projects are part of this document.
