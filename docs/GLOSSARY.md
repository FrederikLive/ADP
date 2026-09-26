# ADP Glossary

**ADP:** Agent Development Protocol.  
**Authorization Envelope:** actions/work authorized by user objective and project context.  
**Atomic Unit:** small coherent implementation step.  
**Contract:** durable substantial-work unit with outcome, scope, acceptance, dependencies, validation, handoff.  
**Coordinating Agent:** delegating agent responsible for briefs, collision control, reconciliation, authoritative state, and human-facing reporting for delegated work.  
**Delegated Execution:** execution of bounded authorized work by another agent/worker under a coordinating agent.  
**Execution Brief:** compact generated projection of user intent, Contract scope, boundaries, acceptance, mutation posture, and verification for delegated execution; not a canonical requirements source.  
**Mutation Posture:** delegated authority mode: `READ_ONLY` or `MUTATING`.  
**Concurrent Mutation Isolation:** requirement that concurrent mutating lanes use separate writable workspaces/change lineages or be serialized.  
**Continuity:** ability to survive context/session/agent replacement.  
**Hard Checkpoint:** pause requiring consequential human authority/information.  
**Soft Checkpoint:** persistence/verification point not normally requiring acknowledgement.  
**Evidence:** executable/inspectable proof supporting completion.  
**Reconciliation:** coordinator review/integration of delegated output against intent, Contract, canonical state, actual artifacts, and required verification before authoritative acceptance.  
**Unlanded Work:** delegated or local changes not yet deliberately integrated/committed/otherwise preserved in the project's accepted delivery path.  
**Next Recommended Phase:** human-scale description of the next meaningful Contract, Workstream, or Milestone outcome and why it should happen next.  
**Exact Next Action:** agent-scale cold-resume instruction concrete enough to continue without reconstructing the plan.  
**Transition Brief:** concise user-facing report at a meaningful development boundary showing completion, verification, next phase, rationale, first action, and execution state.  
**Transition Transparency:** property that makes meaningful development transitions legible to the human operator without creating routine approval gates.  
**Cold Start:** successor session without previous conversation.
