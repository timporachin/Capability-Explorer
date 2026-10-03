# Capability Explorer

**Show it a tool. Discover what it can add to what you're already building.**

Capability Explorer is an AI skill for exploring GitHub repositories, plugins, skills, agents, MCP servers, models, SDKs, CLIs, and other developer/AI technologies.

It doesn't stop at **"What does this do?"**

It asks:

> **How could this capability be used in my projects — and what useful or surprising things could I implement with it that I probably haven't thought of?**

## The idea

When you paste a repository or ask about a technology, Capability Explorer:

1. **Understands the capability** — what the tool actually provides and what evidence supports it.
2. **Understands your project context** — using relevant project information already available to your AI assistant.
3. **Connects the two** — identifying concrete integration opportunities.
4. **Pushes beyond the obvious** — finding useful capability combinations you may not have considered.
5. **Explains what it would take** — dependencies, difficulty, tokens/compute when relevant, limitations, security, maturity, and licensing concerns.

The goal is not to summarize README files. The goal is to turn unfamiliar technology into **project-specific possibilities**.

## Example

Imagine you're building a desktop application and paste a repository for a computer-use agent.

A normal repository summary might say:

> "This project lets an AI interact with graphical interfaces."

Capability Explorer should go further:

> **How it fits your project:** Use it as a visual acceptance tester. After your coding agent finishes a feature, the computer-use agent could launch your application, navigate the affected screens, interact with controls, and report behavioral or visual failures.
>
> **Something you may not have considered:** Because it can operate software without a dedicated API, the same tester could exercise third-party desktop programs your application integrates with — coverage that ordinary unit tests may not provide.
>
> **What it would take:** A supported model, computer-control environment, acceptance-test instructions, and appropriate safeguards around actions the agent can perform.

That is the difference between **explaining a technology** and **exploring what the technology unlocks for you**.

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

## The signature question

After understanding a new technology, Capability Explorer deliberately asks:

> **What becomes possible when this capability intersects with what the user is already building?**

A useful pattern is:

```text
Capability from new technology
            ×
Existing project feature or problem
            ×
Existing tool or workflow
            =
New implementation possibility
```

The best output isn't the longest analysis. It's the one that gives the user a connection they wouldn't have made from reading the repository themselves.

## Try the skill

The skill instructions live here:

[skills/capability-explorer/SKILL.md](skills/capability-explorer/SKILL.md)

If your AI assistant supports installing skills, add the `skills/capability-explorer` folder using its supported installation method.

Otherwise, attach or provide the `SKILL.md` instructions to your assistant and then paste a repository or name a technology.

Example:

```text
Follow the Capability Explorer skill.

https://github.com/owner/project

Explain what this could add to the projects I'm already working on,
including useful ideas I probably haven't considered.
```

For accurate repository analysis, the assistant needs access to the repository or its relevant files.

## Principles

- **Project first.** Generic examples are a fallback when useful project context isn't available.
- **Plain English first.** Explain the idea before the jargon.
- **Possibility matters.** Explore what could be implemented, not just what exists today.
- **Evidence matters too.** Keep verified capabilities, developer claims, and inferred ideas distinct.
- **Depth on demand.** Quick View, Explorer View, and Deep Dive prevent information overload.
- **Resources are information.** Don't optimize every idea for minimum tokens or minimum complexity.
- **Don't overengineer the answer.** A few strong project-specific ideas beat a giant speculative architecture.

## Status

**v0.1 — early public skill specification.**

Capability Explorer is being refined against real repositories and real project contexts before a stable release.

Contributions, test cases, and examples are welcome.

[MIT License](LICENSE)
