# Hindsight × project decision memory

**Supplied project context:** “Our assistant saves issue notes and implementation decisions, but repeatedly suggests approaches we already rejected. We have a review step before accepting design changes.”

**REPORTED capability:** [Hindsight's README](https://github.com/vectorize-io/hindsight#readme) describes retain, recall, and reflect operations for agent memory, with bank-scoped storage and temporal retrieval. This example is documentation-based; no implementation or benchmark was independently verified.

**Direct integration — INFERRED POSSIBILITY:** store approved decision notes and retrieve related decisions before the assistant proposes a design. This connects existing notes to a memory query in the existing proposal workflow. Add ingestion, project isolation, source links, and update/deletion handling.

**Unexpected integration — INFERRED POSSIBILITY:** a “reconsideration queue.” When a dependency or requirement changes, retrieve formerly rejected approaches and draft a question: “Does the reason we rejected this still apply?” Memory supplies prior reasoning; a new change detector and comparison step connect it to current evidence. Your existing review step decides whether to reopen the idea. Memory itself does not prove an old decision is now wrong.

**Requirements/caveats:** choose an upstream-supported deployment and model provider, budget storage and model usage, and define retention/access rules. Preserve source dates and rejection reasons; stale or misretrieved memories can mislead. A bank identifier alone should not be assumed to enforce your application's authorization boundary.

**Difficulty ⓘ:** setup/integration effort. **Moderate–High. Why this rating:** retrieval wiring and memory lifecycle controls.

**Capability Payoff ⓘ:** useful functionality. **High for repeated decisions. Why this rating:** prior work can inform current choices instead of being rediscovered.
