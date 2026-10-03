# Capability Explorer

**Found an interesting AI tool, but have no idea what you could actually do with it?**

Give Capability Explorer its link. It explains what the tool does, what you need to use it, and useful ideas you might not have thought of.

It's a **skill**: a set of instructions your AI assistant follows to give you a better explanation.

## See what you get: Agent Reach

**You paste:**

```text
https://github.com/Panniantong/Agent-Reach
What is this, and what could I do with it?
```

**Capability Explorer explains:**

> **Agent Reach helps an AI assistant get information from the internet.**
>
> It helps set up and check the tools an assistant uses to read websites, explore GitHub, get YouTube subtitles, and access other sources. Some sources need extra setup or a signed-in account.
>
> **Why you might care:** An assistant could look up current information rather than rely only on what its model learned during training.
>
> **Three things you could do with it:**
>
> - Ask a compatible local AI assistant to look up information for a question.
> - Research a tool using its GitHub page, video tutorials, and community discussions.
> - Gather source material for a comparison, with links you can check.
>
> **An idea you might not expect:** Create a technology scout that finds interesting projects and suggests how they could work together to make a new app, plugin, or skill.
>
> **What you need:** An assistant that can run command-line tools, Agent Reach and its dependencies, and any account access required by your chosen sources.
>
> **The catch:** Access depends on the website and its underlying tools. Getting information is not the same as checking whether it is true.

### Take the idea further: an AI research workshop

This was the exciting possibility in our Agent Reach exploration:

**What if your AI could discover useful tools, understand them, and help turn combinations of them into something new?**

For example, you could ask:

> “Find projects that could help build an assistant that remembers its work, researches new ideas, and tests the apps it creates. Explain what each project contributes and suggest one small prototype.”

The pieces would have different jobs:

| Piece | Its job in the proposed workshop |
| --- | --- |
| Agent Reach | Help the assistant access online source material. |
| Capability Explorer | Explain the tools, their requirements, and promising combinations. |
| A memory system | Keep useful findings and lessons from earlier experiments. |
| A coding assistant and test environment | Build and check an approved prototype. |

**This is a possible combination, not a built-in Agent Reach feature.** An autonomous version would also need scheduling, coordination, permissions, and a way to evaluate results. Start with one research question and one prototype.

That is what Capability Explorer is for: helping you see both what a tool does today and what you could build with it.

<details>
<summary>Show example ratings, setup details, and sources</summary>

| Meter | Meaning | Example rating and reason |
| --- | --- | --- |
| Difficulty | How much setup and technical knowledge you need | **Medium, depending on sources:** public sources are simpler; authenticated services need more configuration. |
| Capability Payoff | How useful the added capability could be | **High for research assistants:** access to several kinds of sources expands what they can investigate. |
| Token Intensity | How much AI context and processing a workflow uses | **Variable:** reading one page is lighter than comparing many repositories and discussions. |
| Ecosystem Leverage | How much it helps other tools do more | **High:** retrieved material can feed research, coding, and memory workflows. |

These are explanatory judgments, not measured scores. Resource use is information, not a reason to dismiss an ambitious idea.

**Project reports:** Agent Reach selects, installs/configures with authorization, checks, and routes access to upstream tools. Those tools do the actual reading. Its README describes web, GitHub, YouTube, RSS, and other channels, with additional authentication requirements for some services.

**Inferred possibilities:** The technology scout and research workshop need additional components and development. Connecting a local model also requires a host that can execute tools; installing Agent Reach does not give every chat app internet access automatically.

**Source:** [Agent Reach README](https://github.com/Panniantong/Agent-Reach#readme), checked October 3, 2026.

This is a shortened, rewritten example from the exploration used to develop Capability Explorer, not a verbatim transcript or an installation test. Current project claims were checked against documentation; runtime reliability was not independently verified.

</details>

## Start simple. Ask for more when you want it.

You do not need to learn special commands. Ask naturally:

| Ask this | Get this |
| --- | --- |
| “What is this? Keep it simple.” | **Quick View:** a short explanation and a few useful examples. |
| “What could I do with it?” | **Explorer View:** uses, setup needs, interesting combinations, and limitations. |
| “How does it work, and how would I connect it to my app?” | **Deep Dive:** the relevant technical details. |

You can also request a view by name. A repository link by itself defaults to Explorer View.

## Try it with your assistant

1. Open [the skill instructions](skills/capability-explorer/SKILL.md).
2. Download the file and attach it to your AI chat, or copy its contents into the chat.
3. Send this:

```text
Follow the attached Capability Explorer instructions.
Explain this in simple terms and show me what I could do with it:
https://github.com/Panniantong/Agent-Reach
```

Your assistant needs web or repository access to inspect the project. If it cannot open the link, provide the project's README and relevant files.

If your assistant supports installing skills, add the `skills/capability-explorer` folder through its supported installation process.

## What makes the explanation useful?

- **Plain language first.** Understand the idea before meeting the jargon.
- **Examples you can picture.** See what you could actually do.
- **Room for imagination.** Explore creative possibilities as well as everyday uses.
- **Honest limits.** Learn what needs setup and what remains uncertain.
- **Costs explained.** More computing power or AI usage can be worthwhile; you decide.

<details>
<summary>How it separates facts from ideas</summary>

**Verified** means supported by inspected code or configuration, with the scope stated. Reading code does not prove it ran successfully.

**Reported** means the project or its documentation says it can do something.

**Inferred** means a plausible idea based on its capabilities, often requiring extra tools or development.

The example above uses project-reported capabilities and clearly marked possibilities. Capability Explorer should never pass off an interesting idea as a feature that already exists.

</details>

<details>
<summary>For contributors: package and validation</summary>

**Version:** 0.1.0. This repository contains an AI skill, not a standalone app. It does not install itself into your assistant.

The skill itself does not require a service, API key, GPU, or Python runtime. Your assistant and the tool you explore may have their own costs and requirements.

Run `python3 scripts/validate.py` from the repository root to check the package structure and document links. Python is needed only for this validation command.

[Behavioral acceptance scenarios](tests/acceptance.md) cover explanation depth, evidence handling, missing access, and untrusted repository instructions. These checks do not guarantee consistent behavior across every AI model.

</details>

[MIT license](LICENSE)
