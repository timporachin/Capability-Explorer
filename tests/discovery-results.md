# Discovery and catalog checks — 2026-10-04

## Scope

Fresh-context assistant runs used only the skill and the prompt/context recorded
with each answer. They were not given the expected ideas or grading criteria.
This is a small qualitative sample, not a controlled benchmark or a reliability guarantee.
Caddy, SQLite and FFmpeg were inspected through primary-source tools; no target
applications were installed or executed. Model override: none (inherited host model).

| Run | Observation | Assessment |
| --- | --- | --- |
| Caddy, first revision | Recorded-drive replay and a simulator/build preview switchboard overlapped. | Partial; added a rule rejecting an ambitious idea that merely packages an earlier idea. |
| [Caddy, fresh rerun](discovery-runs/caddy.md) | Startup recovery interface, temporary authenticated review rooms, and recorded-drive replay use different outcomes. Each states missing components. | Bounded pass; usefulness/novelty remain qualitative. |
| [SQLite](discovery-runs/sqlite.md) | OCR coordinates plus text search, time-aligned incident evidence, and simulation changesets. Explicit hypothetical project; no invented user context. | Bounded pass on first revised contract. |
| [FFmpeg](discovery-runs/ffmpeg.md) | Interaction-driven camera motion, sensor-aligned evidence reels, and branching video. | Bounded pass on first revised contract. |
| [Memory limits and Quick View](discovery-runs/memory-scope.md) | Acknowledged unavailable prior chats and storage; distinguished reported search from inspected file reading; respected short scope. | Bounded pass before catalog opt-in extension. |

The SQLite and FFmpeg runs preceded the extra overlap rule and prior-history
paragraph. The Caddy rerun and memory check used those changes. The later catalog
protocol was tested locally as below, not through a fresh end-to-end multi-chat run.

## Catalog helper checks

Six executable unit tests passed:
1. 120 matching entries return five and flag a broader pass.
2. More than five requires expanded mode; expansion cannot exceed 15.
3. An oversized entry cannot overflow the record-character budget.
4. Upserts deduplicate canonical GitHub URLs and preserve unrelated entries,
   settings, and fields.
5. JSON round-trip succeeds; duplicate entries are rejected.
6. No match produces no invented history.

The personal skill validator passed after the final edits. Catalog source and
public package source are identical. A private user catalog was created separately;
neither its contents nor its identifier are part of this repository.

The six tests exercise the local helper. They do not prove assistant compliance,
storage concurrency behavior, or cross-chat tool availability. Those depend on
the host and the workflow in the catalog reference. Future behavioral scenarios
are listed in acceptance.md and must not be represented as already run.

Run the helper tests with:
`python3 -m unittest discover -s tests -p 'test_catalog.py' -v`
