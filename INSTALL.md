# Install or use Capability Explorer

Capability Explorer v0.1.0 is a Markdown skill. It runs through your existing AI assistant. It includes no model, server, app, browser, credentials, or automatic project-memory system. Python is needed only for repository validation, not for using the skill.

## Fastest route: no installation

1. Open [SKILL.md](skills/capability-explorer/SKILL.md), then download the raw file or copy its complete contents.
2. Attach it to a conversation, or paste it and ask the assistant to follow it.
3. Paste a repository URL and ask what it could add to your project. If the assistant lacks project context, attach relevant files or add two sentences about your goal and current stack.

Try: “Follow the attached Capability Explorer instructions. Explore this repository using the project context already available. Separate evidence from proposed integrations.”

This is conversation-scoped manual use, not persistent installation. A URL alone is insufficient if the assistant cannot open it.

## Native skill installation

These paths are supported by the linked host documentation, checked October 3, 2026. We have **not run end-to-end installation tests in these hosts**. Managed accounts and older versions may differ. This repository does not ship a plugin manifest or universal installer.

Download this repository using GitHub's **Code → Download ZIP** and extract it, or clone it:

```sh
git clone https://github.com/timporachin/Capability-Explorer.git
```

Copy the **whole `skills/capability-explorer` folder**, not the repository root, to one destination below. The final file must be `…/capability-explorer/SKILL.md`. Do not create an extra nested folder. Review an existing installation before replacing it.

| Host | Project-only destination | Personal destination | Status |
| --- | --- | --- | --- |
| Codex local CLI/app | `.agents/skills/capability-explorer/` | `~/.agents/skills/capability-explorer/` | Documentation-checked |
| Claude Code | `.claude/skills/capability-explorer/` | `~/.claude/skills/capability-explorer/` | Documentation-checked |
| Gemini CLI | `.gemini/skills/capability-explorer/` | `~/.gemini/skills/capability-explorer/` | Documentation-checked |

Project paths are relative to **the project you want to work on**. `~` means your user home directory; on Windows use the corresponding folder inside your user profile. A local personal installation does not automatically install into a cloud session or another device.

- **Codex:** request “Use capability-explorer to analyze this repository for my project.” Check the available skills list if it does not load. [Official skill locations](https://developers.openai.com/codex/skills/).
- **Claude Code:** invoke `/capability-explorer` followed by the repository and request. [Official instructions](https://code.claude.com/docs/en/skills).
- **Gemini CLI:** use `/skills reload`, then `/skills list` to confirm discovery and ask it to use Capability Explorer. [Official instructions](https://geminicli.com/docs/cli/skills/).
- **ChatGPT:** use the attachment/paste route above. If your workspace exposes custom skill import, use that supported interface with this folder. No universal ChatGPT installation command or account-wide availability is claimed here.
- **Other assistants:** use manual instructions unless their documentation explicitly supports `SKILL.md` folders.

## Confirm it works

Ask: “Quick View: what could this repository add to the project described above?” Confirm that the assistant uses the available context, distinguishes claims from evidence, and proposes a concrete connection. Merely copying a file does not prove the host loaded it.

If it cannot see the skill, check the folder path and host discovery settings; use manual attachment meanwhile. If it cannot inspect the target, provide the README, manifest, and relevant source files. It should disclose missing evidence, not pretend it read the repository.

## Access, privacy, updates

Repository inspection needs read-only web/repository tools or supplied files. Private repositories require your existing authorized connection. Project context comes only from material the host can actually access; the skill does not retrieve all chat history or install any connectors.

Review what you share, remove secrets, and use only relevant context. Analysis does not require executing target installers or giving a target repository credentials.

To update, review and replace the installed skill folder with the new version. To remove a local copy, remove only that folder from its skill location. For managed/imported skills use the host's own controls. Existing chat instructions may remain in that conversation.
