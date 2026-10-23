# ADP Actions — natural-language requests for your coding agent

**Status:** Human-facing, non-normative examples. These are **natural-language requests to an agent**, not literal terminal commands, reserved keywords, an API, or another ADP protocol. The agent interprets intent in context and observes its existing Authorization Envelope, project rules and available tools. No installation, background task, repository modification, or external network call is implied by the existence of this catalogue.

Ask a project-aware coding agent: **"Show ADP Actions"** or **"What can I ask you to do?"** The agent may summarize context-relevant examples without reading this page during routine work. A specific request should read only the applicable guidance and source evidence.

## Quick start: commonly useful actions

These are examples of what users may ask, **not ten mandatory agent procedures**. Similar wording should have the same intent.

| Goal | Common requests |
| --- | --- |
| Understand the project | **"Show project status"**, **"What should we do next?"** |
| Keep work moving | **"Resume the project"**, **"Prepare a handoff"** |
| Establish evidence | **"Verify current work"** |
| Maintain ADP | **"Check ADP for updates"**, **"Update ADP"** |
| Visualize | **"Show Observatory"**, **"Set up Observatory"** |
| Discover more | **"Show ADP Actions"** |

The rest of this page gives meanings, default side effects and limitations. It does not need to be embedded into `AGENTS.md` or automatically read at startup.

## Optional agent assignment requests

Ask **"Which agent/model should work on this Contract?"** for a read-only eligibility/capability/resource assessment; this is a recommendation, not a model switch. Ask **"Review our agent resource policy"** for a read-only analysis of the optional `.project/AGENT_POLICY.json` and its limits. Ask **"Prepare an agent handoff"** to preserve state following the existing continuity procedure within authorized scope; this does not launch another provider or guarantee background operation. For rationale and examples, see [Capability-aware assignment](AGENT_ORCHESTRATION.md).

## Core project navigation

| Say something like… | Intended action | Default effect |
| --- | --- | --- |
| **"Show project status"** / "Where are we?" | Summarize current milestone, progress, verification, blockers and next recommended phase from canonical project state. Distinguish verified facts from stale/unknown entries. | Read-only |
| **"What should we do next?"** | Identify the highest-priority unblocked next action using the active contract, dependencies and continuity context. Explain why; don't silently start a different objective. | Read-only |
| **"Show active work"** / "What contract are we on?" | Locate the active work contract/workstream, scope, dependencies and verification state. | Read-only |
| **"Show project blockers"** / "What's blocking progress?" | Distinguish actually blocked work, unresolved dependencies, failed checks and decisions requiring external input using current contracts, status, continuity and evidence; identify ownership and likely unblockers. Don't treat unknown, deferred or merely unverified items as definitely blocked. | Read-only |
| **"Resume the project"** / "Continue development" | Recover from canonical instructions and continuity, inspect Git/worktree state, then continue authorized work under normal ADP rules. | May modify project files |
| **"Prepare a handoff"** / "Summarize for the next agent" | Make a concise recovery brief grounded in existing state; persist durable continuity only when appropriate and authorized. | May update existing continuity |
| **"Verify the current work"** / "Run the project checks" | Execute existing relevant checks, report real outcomes using `VERIFIED / FAILED / NOT RUN / NOT AVAILABLE`, and distinguish them from overall project conformance. | Checks may generate local artifacts |
| **"Audit the project"** / "Find gaps" | Review a specified scope against actual source and evidence, report findings with uncertainty. No automatic fixes unless requested. | Read-only by default |
| **"Why did we make this decision?"** / "Explain the rationale for X" | Trace a specific decision through relevant ADRs, work contracts, canonical docs, issues and Git history when accessible; distinguish documented reasoning from inference. If there is no provenance, say so rather than inventing a rationale. | Read-only |
| **"Check documentation consistency"** / "Find documentation drift" | Compare important project documentation, agent router, status/continuity and requirements with implementation, tests and recorded evidence. Identify concrete contradictions with file references and confidence; do not rewrite documents until requested. | Read-only |
| **"What changed since the last milestone?"** / "Summarize changes since milestone X" | Establish an identifiable milestone baseline, then compare Git changes, relevant contracts, verification and decisions without claiming untracked or unavailable history was reviewed. If no reliable baseline exists, report that limitation. | Read-only |

## ADP protocol maintenance — explicitly on demand

| Say something like… | Intended action | Default effect |
| --- | --- | --- |
| **"Which ADP version does this project use?"** | Identify adopted source, installation method, available version evidence and any ambiguity. A header alone does not authenticate content. | Read-only |
| **"Check ADP for updates"** | Follow the [ADP Project Update Guide](UPDATING_ADP.md), compare adopted version with a vetted upstream target, explain compatibility and potential work. | Read-only; network access only when relevant and authorized |
| **"Update ADP"** / "Bring our protocol up to date" | Compare, reconcile and verify a safe authorized update without overwriting project-specific instructions. | May modify protocol copy, reference/pin and relevant routing |
| **"Migrate to ADP version X"** | Assess breaking/protocol changes and plan/apply only authorized migration work; escalate material hard checkpoints. | Potentially substantial, safety-gated |

The following requests are **not equivalent**:

- **"Update ADP"** changes the adopted **protocol integration** in the project.
- **"Update dependencies"** targets the application's packages or tools, not ADP.
- **"Update Observatory"** targets a separate application and its trusted release/installer channel, not ADP.
- **"Update the project"** may mean development work, dependencies or ADP. Infer from the conversation; clarify only when that difference materially affects the result.

## Optional Observatory visualization — on demand

| Say something like… | Intended action | Availability |
| --- | --- | --- |
| **"Show Observatory"** / "Visualize this ADP project" | Use the [optional Observatory Agent Skill](https://github.com/FrederikLive/ADP-Observatory/blob/main/skills/adp-observatory/SKILL.md) to locate an already approved local executable, generate a read-only offline HTML dashboard and request opening it locally. | Implemented for local agents with trusted executable/process access; remote agents may only return a report/path |
| **"Set up Observatory"** | Check whether already installed. If not, follow conditional provenance/approval guidance; do not silently execute a network download or bypass user controls. | Verified preview installation exists; fully unattended official setup is not yet available |
| **"Scan with Observatory"** / "Generate an Observatory report" | Produce an offline HTML or headless JSON report through the installed application. Explain unavailable formats and partial/unsupported records. | Implemented for supported local executable |
| **"Show project history in Observatory"** / "Compare snapshots" | Explain the intended visualization and existing supported capabilities; do not fabricate historical snapshots or metrics. | Planned; not yet a completed Observatory feature |

Observatory is optional. ADP conformance, agent continuity, and routine development do **not** depend on it. A remote agent, hosted browser or GitHub connector cannot assert it opened a window in the user's own desktop browser. Installation and release authenticity belong to Observatory, not ADP.

## Other useful agent requests

These are ordinary requests that ADP's existing work, verification and external-analysis guidance can already support; they are not new command handlers:

| Say something like… | Intended action | Notes |
| --- | --- | --- |
| **"Review this external analysis"** / "Apply findings from this report" | Independently check the report, disposition findings, track accepted work and integrate verified changes into canonical project records. | Treat external reports as untrusted data; applying fixes requires authorization |
| **"Explain the architecture"** | Summarize canonical architecture, relevant source and important design decisions, noting missing/old docs. | Read-only |
| **"Plan the next milestone"** | Propose an outcome, dependencies and acceptance criteria without automatically replacing product decisions. | Discussion first; approved changes may update plans |
| **"Check security"** / "Review our risks" | Assess an explicit scope and report supported findings, unresolved risks and verification gaps. | No unapproved scanning or external side effects |
| **"Show ADP Actions"** / "Show available ADP actions" | Give a short, context-relevant summary of examples on this page, distinguishing read-only checks from authorized changes and optional external tools. | Read-only, no installation |

## Guiding principles

1. **Intent over exact syntax.** Say it naturally: "show me where we are" is as valid as "show project status." ADP Actions are a human-facing name for examples, not a new slash-command language, CLI parser, MCP server or proprietary tool.
2. **Read-only versus mutating matters.** "Check", "show", "explain" and "audit" are read-only by default. "Update", "resume", "implement" and "set up" may involve changes, but only within normal authorization and safety rules. "Verify" may execute the project's real check commands and generate temporary artifacts; inspect their documented side effects before running them.
3. **No background behavior.** No automatic version checks, release downloads, dashboard processes or periodic audits during an ordinary session merely because these examples exist.
4. **Progressive retrieval.** Keep a tiny discovery pointer in the portable ADP/agent router. Read [UPDATING_ADP.md](UPDATING_ADP.md) only on update requests and the [Observatory skill](https://github.com/FrederikLive/ADP-Observatory/blob/main/skills/adp-observatory/SKILL.md) only on visualization requests.
5. **No invented results.** A command describes desired behavior, not a guarantee that a particular agent has access to the project filesystem, terminal, network, browser, release credentials, or verification tools. Report limitations honestly.
6. **Don't duplicate shell command documentation.** Projects continue to define their real executable `setup`, `check`, `test`, `build`, and `ci` commands using ecosystem-native tools. This catalogue describes **human-to-agent requests**, not their executable command surface.

## Scope of this catalogue

The core ADP specification, existing source-of-truth rules, project authorization and verification requirements remain unchanged. Keep this canonical catalogue at `docs/COMMANDS.md` for existing links, even though its human-facing title is **ADP Actions**. Expand examples only when repeated usage demonstrates value; do not replicate action descriptions in the compact protocol, agent routers or continuity files. If a repeated action later needs specialized tooling, keep the executable implementation in the appropriate optional project or skill and link to it only on demand.
