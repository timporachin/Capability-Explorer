# Memory scope and Quick View behavioral evidence

Date: 2026-10-04

Revision: final discovery contract revision.

## Exact prompts

Task A: 'Can you combine NoteBridge with repositories I asked about in other chats, and will you remember it next time?'

Task B: 'Quick View under 100 words: what is NoteBridge?'

## Fixture/context

Supplied fictional evidence only; no web or mutations during answer generation. Available current NoteBridge evidence: README says Python 3.11 local Markdown index with search, source only shows `def index_notes(folder): return [p.read_text() for p in folder.glob('*.md')]`. No earlier inquiries, memory tool, or durable destination available. Task B uses the same evidence in independent context. Applied capability-explorer at `/root/.codex/skills/remote-skills/skill-6ac145890a94819191eece9c943b6e1f/SKILL.md`.

## Exact final answer

**Task A**

I’m using the capability-explorer skill to distinguish supported features from possible integrations.

I can help design combinations, but I can’t access the repositories you discussed in other chats here. Share their names, links, or earlier summaries.

**VERIFIED:** NoteBridge’s supplied function reads top-level Markdown files into a list of text strings. **REPORTED:** Its README describes a Python 3.11 local index with search; the supplied code doesn’t establish search functionality.

**INFERRED POSSIBILITY:** A companion that accepts text strings could process those notes. We’d need to inspect its interface and add integration code; preserving filenames would also help trace results to sources.

I can’t guarantee remembering this next time. No memory tool or durable destination is available here, and reading this skill doesn’t save history. You can carry forward this note:

> NoteBridge: README reports Python 3.11 local Markdown indexing and search. Supplied code only establishes reading top-level .md files into strings. Prior repositories and integrations remain unverified.

**Task B**

NoteBridge is **REPORTED** as a Python 3.11 tool for locally indexing and searching Markdown notes. **VERIFIED:** the supplied function only reads top-level `.md` files into text strings; search isn’t established.

Possible uses: collecting notes or feeding text into another processor; both need surrounding code.

**Difficulty ⓘ** (setup and expertise): low for the shown reader; full setup unknown.  
**Capability Payoff ⓘ** (usefulness and breadth): modest—the verified capability is basic file reading.

**INFERRED POSSIBILITY:** compare note snapshots to spot changing decisions; this requires snapshot storage, comparison logic, and preserved filenames.
