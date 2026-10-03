# Capability Explorer

**Understand what technology can do — and what you might do with it.**

Capability Explorer v0.1 is an AI skill that explains GitHub repositories,
plugins, skills, MCP servers, models, SDKs, CLIs, and frameworks in plain
English. It connects real capabilities with practical uses, creative ideas,
and ambitious possibilities while separating evidence from speculation.

## Choose your depth

| View | What you get |
| --- | --- |
| Quick View | A short introduction, difficulty and payoff, three uses, and a meaningful unexpected possibility. |
| Explorer View | Capabilities, requirements, useful meters, examples, combinations, and limitations. Default for a repository URL. |
| Deep Dive | Architecture, interfaces, dependencies, evidence, and integration details tailored to your question. |

Resource usage is information, not a constraint. An ambitious idea should
not disappear because it might use more tokens or computing power.

## Use it

The skill lives in [`skills/capability-explorer/SKILL.md`](skills/capability-explorer/SKILL.md).
Add the complete `capability-explorer` folder to a skill-capable assistant
using that host's supported installation workflow. This repository does
not automatically install itself into your account.

For an assistant without skill installation, attach `SKILL.md` and ask it
to follow the instructions while explaining your target. Browsing or
repository access is needed for current, evidence-backed inspection; if
unavailable, supply the relevant source files and documentation yourself.

Example requests:

```text
Use Capability Explorer: https://github.com/owner/project

Quick View: What is this tool, and why might I care?

Explorer View: What could I build with this beyond the obvious uses?

Deep Dive: Explain its architecture, actual interfaces, and setup requirements.
```

No bundled service, API key, GPU, or Python runtime is required to read the
skill. The assistant and the technology being explored may have their own
requirements and costs. This version is a portable instruction package,
not a standalone website, model, or MCP server.

## Evidence you can understand

- **Verified:** supported by inspected implementation/configuration, with
  the scope stated. Reading code does not prove it runs successfully.
- **Reported:** the project or its documentation claims it.
- **Inferred:** a plausible possibility that needs additional work or tools.

Meters explain difficulty, resource intensity, payoff, and ecosystem
leverage where useful. They are judgments with definitions, not benchmarks.
Unknowns stay unknown. The skill uses read-only inspection for explanation.

## Validate v0.1

Run `python3 scripts/validate.py` from the repository root. It uses only
Python's standard library and checks package structure and document links.
The behavioral scenarios in [`tests/acceptance.md`](tests/acceptance.md)
cover depth selection, source honesty, creative possibilities, unavailable
access, and hostile repository instructions. Structural validation does
not establish that every model will follow the instructions consistently.

## Scope

v0.1 packages the agreed core behavior. There is no automatic installation,
background execution, agent orchestration, or model integration layer.
Future changes should be driven by actual use rather than extra machinery.

Released under the [MIT license](LICENSE).
