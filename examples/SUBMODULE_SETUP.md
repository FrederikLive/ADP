# ADP as a Git submodule

```bash
git submodule add https://github.com/FrederikLive/ADP.git .adp/protocol
git add .gitmodules .adp/protocol
git commit -m "chore: add ADP development protocol"
```

Point the agent to `.adp/protocol/AGENTS.md` and `.adp/protocol/ADP.md`. Pin a release tag for reproducibility.
