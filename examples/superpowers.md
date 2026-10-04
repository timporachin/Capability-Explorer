# Superpowers × a support-to-fix workflow

**Supplied project context:** “We maintain a small app, receive vague support reports, and already have a test runner and code review. Fixes sometimes miss what users meant.”

**REPORTED capability:** [Superpowers](https://github.com/obra/superpowers#readme) describes skills for clarifying work, planning, testing, and reviewing implementation. These are upstream workflow claims, not proof that every host will follow them or that quality improves by a measured amount.

**Direct integration — INFERRED POSSIBILITY:** use the relevant workflow instructions to turn a support report into a scoped plan, failing test, fix, and review using your existing runner. Complement the review process; do not replace its acceptance criteria.

**Unexpected integration — INFERRED POSSIBILITY:** turn clarification into a reusable “meaning of this bug” record: user intent, ambiguous terms, reproduction, and expected behavior. When a similar ticket arrives, propose the old scenario as a candidate regression case. Planning and clarification supply the structure; your issue store and matching logic supply reuse. Superpowers alone is not a support database or duplicate-ticket detector.

**Requirements/caveats:** a compatible coding assistant and access to the project/tests; select the relevant skills and resolve conflicts with existing team instructions. Add issue storage/matching only if the reuse proves useful. More planning and review can consume more model calls; judge the payoff against avoided rework.

**Difficulty ⓘ:** setup and technical knowledge. **Moderate. Why this rating:** adapt workflow instructions to your team and tests.

**Capability Payoff ⓘ:** useful functionality. **Potentially high. Why this rating:** vague reports become explicit, reusable behavior expectations.
