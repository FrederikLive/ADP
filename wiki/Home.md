# ADP — Agent Development Protocol

**ADP** is a vendor-neutral protocol for structuring software projects so capable AI coding agents can understand what the user wants, build it with high autonomy, verify the result, preserve project knowledge, recover across sessions, and hand work to another agent without losing state.

> **Core principle:** The repository is durable project memory. Agent sessions are replaceable execution capacity.

This Wiki is a human-friendly guide to ADP. It is **non-normative**. The canonical protocol is [ADP.md](https://github.com/FrederikLive/ADP/blob/main/ADP.md); if this Wiki and the protocol differ, **ADP.md wins**.

## What ADP is for

ADP addresses common failure modes in AI-assisted development:

- repeated “continue” prompts;
- agents stopping after partial work;
- product intent being lost during implementation;
- weak or unverified completion claims;
- context-window exhaustion;
- poor handoff between agents;
- documentation drift;
- unsafe destructive actions;
- concurrent agents overwriting one another;
- delegated workers returning technically correct work that misses the user's actual goal.

ADP creates a small repository-native control system around the code so agents can work autonomously without making the project dependent on a particular vendor, model, IDE, or orchestration framework.

## The ADP model

```text
USER INTENT
    │
    ▼
PROJECT
    │
    └── MILESTONE / OUTCOME
           │
           └── WORKSTREAM
                  │
                  └── CONTRACT
                         │
                         ├── ATOMIC UNIT
                         └── EVIDENCE
```

Execution can be direct or delegated:

```text
Contract
   │
   ├── Direct execution
   │
   └── Delegated execution
          ├── Execution Brief
          ├── isolated mutation when concurrent
          ├── worker evidence
          └── reconciliation
```

## Start here

- [Getting Started](Getting-Started.md)
- [Core Model](Core-Model.md)
- [Autonomy and Checkpoints](Autonomy-and-Checkpoints.md)
- [Delegated and Concurrent Execution](Delegated-and-Concurrent-Execution.md)
- [Verification and Evidence](Verification-and-Evidence.md)
- [Continuity and Handoffs](Continuity-and-Handoffs.md)
- [Transition Transparency](Transition-Transparency.md)
- [Repository Control Plane](Repository-Control-Plane.md)
- [WORK.json](WORK-json.md)
- [Conformance and Versioning](Conformance-and-Versioning.md)
- [FAQ](FAQ.md)

## Current protocol

**ADP 2.5.0** adds Delegated & Concurrent Execution while keeping direct single-agent execution as the default when it is the smallest sufficient execution topology.

**Author:** Frederik Smith  
**License:** MIT
