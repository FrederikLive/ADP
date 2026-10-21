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

## How it works today (prototype)

As of October 2026, Observatory has a tested **Rust command-line scanner**. It can inspect supported work-index structures and references, report limited protocol compatibility, and produce human-readable or JSON output. **It does not yet provide a downloadable installation, automatic launcher, graphical dashboard, or full ADP conformance assessment.**

For developers with Rust installed and the Observatory repository cloned separately, from the root of an ADP project run:

```sh
cargo run --manifest-path /absolute/path/to/ADP-Observatory/Cargo.toml -- . --json
```

Replace the manifest path with the actual location of your Observatory checkout. The `.` refers to the **current ADP project**. Omit `--json` for the current text output. See [the Observatory README](https://github.com/FrederikLive/ADP-Observatory#current-prototype) for its implementation status.

## Intended user experience (not released yet)

Once the application has a verified, platform-specific installer or launcher, a user should be able to open a terminal in their project and run:

```sh
adp-observatory .
```

That command is a **future target**, not a working installation instruction today. The intended behavior is to find the target project, analyze it without modifying files, start a local-only dashboard, and open the dashboard in the user's browser.

For terminal, CI, and agent workflows, a separate explicit scan mode should emit machine-readable results without opening a browser:

```sh
adp-observatory scan . --json
```

The planned subcommand is not implemented yet; the prototype currently takes the project path directly.

### Installation and first-run concept

Users should not need to copy executables into each ADP project or install a compiler. Observatory will provide verified releases for supported platforms and a safe, documented installation or one-shot launch mechanism. The downloaded application and caches belong in user-controlled system locations, **outside the target project**. No login, telemetry, administrator/root privileges, or automatic upload should be required.

A true zero-install, single-command bootstrap should be offered only after it can **verify the downloaded executable and its trusted release metadata before execution**. Never suggest blindly piping remote scripts into a shell. Installation and self-update behavior belong to the Observatory project; the official launch instructions will be published there when those features ship.

## Supported ADP versions

Observatory's parser and display compatibility are independent of normative ADP conformance. A project with an old or unknown ADP version may still be partly readable, with unsupported assessments clearly labeled. A missing optional `WORK.json` is not automatically a violation.

## Documentation and support

For up-to-date installation, supported platforms, analyzer coverage, and releases, refer to the [ADP-Observatory repository](https://github.com/FrederikLive/ADP-Observatory) and its [launcher and distribution design](https://github.com/FrederikLive/ADP-Observatory/blob/main/docs/LAUNCHER.md).

**The normative specification remains [ADP.md](../ADP.md).** No Observatory-specific tool is mandatory for implementing ADP.
