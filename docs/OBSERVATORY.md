# Visualizing an ADP project with ADP-Observatory

**Status:** Optional companion integration. This is a human-facing user guide, **not** part of the normative Agent Development Protocol (ADP).

**[ADP-Observatory](https://github.com/FrederikLive/ADP-Observatory)** is a separate, local-first open-source project intended to help people understand the current state, progress, verification evidence, continuity, and history of repositories that use ADP.

## Design boundary

ADP exists to help agents work efficiently with minimal unnecessary token usage and durable project memory. Observatory is a **consumer** of that project information, not a prerequisite for it.

- An ADP project does **not** need Observatory to conform to ADP.
- Agents should not read this guide during ordinary project work unless asked about Observatory.
- No new ADP metadata, event logs, mandatory project files, or agent documentation steps are required for visualization.
- Observatory must tolerate missing, inconsistent, older, newer, and unsupported project records and distinguish known findings from unknown or not-assessed information.
- Observatory is read-only by default: analysis does not alter canonical project state.
- Observatory findings and dashboards are derived views, not authoritative substitutes for project records or verification evidence.

## Ask an agent to show Observatory (optional)

In an ADP project, users can ask their coding agent:

> Show Observatory for this project.

Equivalent requests such as "Open the ADP Observatory dashboard" or "Visualize this ADP project" should activate the optional [ADP-Observatory Agent Skill](https://github.com/FrederikLive/ADP-Observatory/blob/main/skills/adp-observatory/SKILL.md) **only on demand**. The skill belongs to the Observatory repository; ADP carries only a compact discovery hint. It does not introduce a mandatory protocol, extra work-index fields, routine agent context, or generated project records.

With trusted local terminal access and a previously approved Observatory installation, the agent can use the bundled [local launch helper](https://github.com/FrederikLive/ADP-Observatory/blob/main/skills/adp-observatory/scripts/launch.py) to generate a report outside the project and request opening in the local browser. The helper never downloads executables or packages. If Observatory is absent, the agent follows the skill's **conditional installation guidance** rather than silently executing downloaded code. Preview installation still requires a reviewed local checkout, an exact source commit and CI run, an independently installed GitHub CLI, and appropriate user authorization.

A remote-only coding agent **cannot guarantee opening a window on the user's actual computer**. If the available tools lack local desktop access, it should return the report path or an appropriate generated artifact, or explain how to open Observatory locally. Browser opener success means an open was requested, not proof the user saw it.

**For existing ADP projects:** previously generated `AGENTS.md` files do not update automatically. Install the skill in the agent's supported user-level skills directory or add the same small discovery hint to that project's router. Projects using a copy of an older `ADP.md` can continue working normally without this optional companion.

## How it works today (prototype)

As of October 2026, Observatory has a tested **Rust command-line scanner and local offline HTML viewer**. It can inspect supported work-index structures and references, report limited protocol compatibility, and produce human-readable or JSON output. **It now provides a self-contained offline HTML dashboard in the development executable, but not an official installer, trusted automatic download launcher, historical dashboard, or full ADP conformance assessment.**

For developers with Rust installed and the Observatory repository cloned separately, from the root of an ADP project run:

```sh
cargo run --manifest-path /absolute/path/to/ADP-Observatory/Cargo.toml -- .
cargo run --manifest-path /absolute/path/to/ADP-Observatory/Cargo.toml -- scan . --json
```

Replace the manifest path with the actual location of your Observatory checkout. The `.` refers to the **current ADP project**. The first command generates and attempts to open a local HTML report, stored outside the target project. The second provides headless JSON without opening a browser. The report may contain sensitive project paths and should be handled accordingly. Experimental Windows/Linux/macOS CI binaries with signed build-provenance attestations exist, but are not official OS-code-signed releases; follow the [manual verification guidance](https://github.com/FrederikLive/ADP-Observatory/blob/main/docs/LAUNCHER.md) before testing them. See [the Observatory README](https://github.com/FrederikLive/ADP-Observatory#current-prototype) for its implementation status.

## Intended user experience (not released yet)

Once the application has a verified, platform-specific installer or launcher, a user should be able to open a terminal in their project and run:

```sh
adp-observatory .
```

That command **works in the development executable**, but a user must first obtain or build the binary. It is **not** an available system-wide command until Observatory is installed. The current dashboard is a self-contained offline HTML report, not a listening web server.

For terminal, CI, and agent workflows, a separate explicit scan mode should emit machine-readable results without opening a browser:

```sh
adp-observatory scan . --json
```

The subcommand is implemented in the development executable. An installed, signed official application is not yet available.

### Experimental preview installation (developers only)

The experimental Bash and PowerShell installers have now passed CI download, signed-provenance verification, installation, and scanning tests on Linux x64, macOS ARM64, and Windows x64. They are **not official OS-code-signed installers** and require a trusted local Observatory checkout, GitHub CLI and a pinned successful Actions run plus full commit SHA. See the [preview installation instructions](https://github.com/FrederikLive/ADP-Observatory/blob/main/docs/RELEASING.md). Once installed and on PATH, users can run `adp-observatory .` from an ADP project. The signed and streamlined public installer remains a future release milestone.

### Installation and first-run concept

Users should not need to copy executables into each ADP project or install a compiler. Observatory will provide verified releases for supported platforms and a safe, documented installation or one-shot launch mechanism. The downloaded application and caches belong in user-controlled system locations, **outside the target project**. No login, telemetry, administrator/root privileges, or automatic upload should be required.

A true zero-install, single-command bootstrap should be offered only after it can **verify the downloaded executable and its trusted release metadata before execution**. Never suggest blindly piping remote scripts into a shell. Installation and self-update behavior belong to the Observatory project; the official launch instructions will be published there when those features ship.

## Supported ADP versions

Observatory's parser and display compatibility are independent of normative ADP conformance. A project with an old or unknown ADP version may still be partly readable, with unsupported assessments clearly labeled. A missing optional `WORK.json` is not automatically a violation.

## Documentation and support

For up-to-date installation, supported platforms, analyzer coverage, and releases, refer to the [ADP-Observatory repository](https://github.com/FrederikLive/ADP-Observatory) and its [launcher and distribution design](https://github.com/FrederikLive/ADP-Observatory/blob/main/docs/LAUNCHER.md).

**The normative specification remains [ADP.md](../ADP.md).** No Observatory-specific tool is mandatory for implementing ADP.
