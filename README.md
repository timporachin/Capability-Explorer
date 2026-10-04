# Capability Explorer

**Show it a tool, agent, skill, or GitHub repo. Discover what it can add to what you're already building — including useful possibilities you haven't thought of.**

GitHub tells you what a project is. Capability Explorer asks what it could become inside yours.

An **AI skill**: instructions your assistant follows, not an app, hosted service, or bundled model. Works with repositories, plugins, agents, MCP servers, models, SDKs, CLIs, and frameworks.

### Video demo

**From separate repositories to an Autonomous R&D Laboratory**

https://github.com/user-attachments/assets/942cb972-245d-470b-88f1-7f4354b90627

Capability Explorer connected five capabilities into an **INFERRED SYSTEM ARCHITECTURE**. This is a proposed architecture, not a finished integrated product.

https://github.com/user-attachments/assets/a3af4d1d-6ab5-4f80-9323-c04f565d2b81

https://github.com/user-attachments/assets/5830ea9c-4a7b-4648-9a7f-0696715eb71a

Animated example with music and on-screen explanations. Proposed integrations are labeled.

### Before / after

**Normal repository explanation**

> “This library lets AI agents interact with desktop applications.”

**Capability Explorer**

> “Your project already has automated builds. This could become a visual acceptance-test worker: launch each build, navigate affected screens, and report failures to your coding agent. Because your app also launches third-party programs, it could test the handoff between them — even without an API.”

*Illustrative project context; proposed integrations are **INFERRED POSSIBILITY**, not existing features or completed tests. [Full Agent-S example](examples/agent-s.md).*

**[Try it in two minutes](INSTALL.md)** · **[See examples](examples/README.md)** · **[Read the skill](skills/capability-explorer/SKILL.md)**

## The idea

**New capability × your existing project × your existing workflow = new implementation possibility.**

Capability Explorer identifies what a technology provides, connects it to your project's components or problems, and explains 2–4 useful implementations and what they require. It can suggest what to enhance, complement, or replace, with reasons for the connection.

## Project-aware by design

If the AI assistant already has relevant context about your project, Capability Explorer should use it instead of making you explain your project again.

Relevant context may come from:

- the current conversation
- project/repository access
- attached files
- available project context or memory
- connected sources
- tools, plugins, models, and workflows already established in context

If sufficient project context genuinely isn't available, Capability Explorer still explains the technology and can ask for a repository or short project description when project-specific recommendations would materially improve the result.

It should never invent project details that aren't actually available.

## Three levels of detail

### Quick View
For **"What is this?"**

A short plain-English explanation, why it might matter to you, a couple of relevant uses, Difficulty, Capability Payoff, and one strong unexpected possibility when appropriate.

### Explorer View
For **"What could I do with this?"** or a repository URL.

The default experience:

- what it is
- what it gives you
- how it fits your project
- things you could build with it
- things you probably haven't considered
- dependencies and setup
- useful capability meters
- important limitations

### Deep Dive
For **"How does this work and how would I integrate it?"**

Adds architecture, interfaces, APIs/MCP tools, source details, exact dependencies, benchmarks, security, licensing, and implementation design as needed.

Complex technology should not require a complex first explanation.

## Capability meters

Meters are supporting information, not the main attraction.

Common dimensions include:

| Meter | What ⓘ means |
| --- | --- |
| **Difficulty ⓘ** | How much technical knowledge, setup, configuration, and infrastructure are needed. |
| **Capability Payoff ⓘ** | How much useful functionality, leverage, automation, or creative possibility it provides. |
| **Token Intensity ⓘ** | How much LLM context, reasoning, and tool usage a representative workflow may consume. |
| **Compute Intensity ⓘ** | CPU, GPU, VRAM, RAM, storage, and processing burden. |
| **Ecosystem Leverage ⓘ** | How strongly it enhances or connects other tools, models, agents, or systems. |

Capability Explorer only shows dimensions that actually help explain the technology. High token or compute use is **information, not a reason to suppress an ambitious idea**.

## Evidence vs. imagination

Capability Explorer deliberately explores possibilities, but it keeps evidence and inference separate.

**Verified** — directly supported by inspected implementation or configuration.

**Reported** — claimed by the project or its documentation but not independently established.

**Inferred possibility** — technically plausible based on supported capabilities, but requiring additional integration or development.

This lets Capability Explorer be imaginative **without pretending an idea is already a feature**.

## Try it

Attach [SKILL.md](skills/capability-explorer/SKILL.md) to your assistant and say:

```text
Follow the attached Capability Explorer instructions.
Analyze https://github.com/simular-ai/Agent-S for the project we are building.
Show a direct fit and one useful possibility I probably haven't considered.
Use only project context you actually have.
```

No project context yet? It will still explain the technology. A short project description makes the connections more specific. The host needs repository/web access or supplied source files; the skill does not grant access or memory.

For formal installation and host-specific status, see [INSTALL.md](INSTALL.md).

## Examples and demo

- [Agent-Reach](examples/agent-reach.md): a beginner-friendly repair notebook that notices gaps in its own instructions.
- [Agent-S](examples/agent-s.md): desktop automation becomes an integration handoff tester.
- [Hindsight](examples/hindsight.md): memory becomes a record of why a project rejected an approach.
- [Superpowers](examples/superpowers.md): development practices help turn vague bug reports into reproducible tests.
- [Watch the finished video demo](#video-demo) · [Original storyboard](launch/demo-storyboard.md).

## Principles

- **Project first.** Generic examples are a fallback when useful project context isn't available.
- **Plain English first.** Explain the idea before the jargon.
- **Possibility matters.** Explore what could be implemented, not just what exists today.
- **Evidence matters too.** Keep verified capabilities, developer claims, and inferred ideas distinct.
- **Depth on demand.** Quick View, Explorer View, and Deep Dive prevent information overload.
- **Resources are information.** Don't optimize every idea for minimum tokens or minimum complexity.
- **Don't overengineer the answer.** A few strong project-specific ideas beat a giant speculative architecture.

## Status and contributing

**v0.1.0 — early public skill specification, MIT licensed.** Results depend on the host model, available evidence, and project context. Native host installation recipes are documentation-checked, not end-to-end certified.

[Contribute an example, test repository, or correction](CONTRIBUTING.md). [Behavioral acceptance scenarios](tests/acceptance.md) are separate from automated structural checks; see [validation results](tests/RESULTS.md).

Run the dependency-free checks with Python 3.10+:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

[Launch drafts](launch/README.md) · [MIT License](LICENSE)
