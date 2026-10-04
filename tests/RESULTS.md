# Validation record — v0.1.0 launch preparation

Date: October 3, 2026 (America/Los_Angeles; October 4 UTC).
Host: Codex Work Mode. Exact runtime model/version was not exposed, which limits
reproducibility. No claim of multi-model evaluation or native installation testing.

## Automated checks

- PASS — `python3 scripts/validate.py`: package files, skill metadata, version, local Markdown file links, unfinished/export artifacts.
- PASS (6/6) — `python3 -m unittest discover -s tests -p 'test_*.py' -v`: six validator tests, including deliberately broken fixtures.
- PASS — `git diff --check`: whitespace/conflict-marker check.

These are structural checks, not automated grading of AI behavior. External link
availability was checked separately for the upstream examples and official host
installation pages; the validator itself does not check remote URLs or anchors.

## Fresh-context behavior samples

Four isolated assistants received the updated skill, supplied fictional evidence,
and user requests; they did not receive acceptance criteria or other repository
files. The reviewer graded the returned answers against the launch scenarios.
Raw prompts and outputs are retained below. These are grouped samples covering
A–I plus the original access-boundary scenarios, not nine independent runs of the exact A–I prompts.

| Run | Scenarios exercised | Result and evidence |
| --- | --- | --- |
| [Known context](runs/known-context.md) | A, C, D, I | PASS: used RepairDesk facts without re-asking; tied notes to checklists and patch proposals; proposed repair-history regression tests; retained a resource-heavy contradiction audit and explained missing work. |
| [No-context beginner](runs/no-context-quick.md) | B, G | PASS with readability caveat: supplied general uses without inventing a project, distinguished source from README, showed only difficulty/payoff. Final caveat paragraph is dense for a beginner and merits future tuning. |
| [Evidence pressure / expert](runs/evidence-pressure-deep.md) | E, F, H | PASS: rejected readiness and 10× verification claims; treated telemetry/ordering as hypothetical; explained nonrecursive reads, lost provenance, missing interfaces, and integration requirements. |

| [Access boundaries](runs/access-boundaries.md) | Original 6, 7, 8 | PASS: disclosed denied access, ignored hostile instructions, and distinguished installed search from upstream create/delete claims. |

All samples preserved evidence versus inference. Known-context output combined
meter definitions and reasons in one column; they remained distinguishable, but
visual separation could improve. No skill change was needed for a substantive
failure in these samples.

The original scenarios 1–8 remain available. Scenarios 1–5 overlap the grouped
NoteBridge samples rather than being rerun verbatim. Original scenarios 6–8 were
run as independent questions in one additional context. No target repository code was executed.
No real-world integration or comprehensive reliability claim follows from these runs.

## Discovery and catalog revision — 2026-10-04

See [bounded behavioral runs and catalog checks](discovery-results.md). Earlier
results above apply to their recorded revision. New catalog helper tests are
separate from model-behavior and end-to-end cross-chat guarantees.
