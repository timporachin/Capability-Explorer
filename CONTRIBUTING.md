# Contributing

A small, concrete contribution is enough. Open an issue or pull request; no proposal document or special tooling is required.

## Useful contributions

- **Suggest a test repository:** exact URL, why it is interesting, and a short fictional or shareable project context. State which connection would be worth exploring without claiming it already works.
- **Report an inaccurate analysis:** include the prompt, relevant context, model/host, skill version, problematic excerpt, and evidence that contradicts it. Remove secrets and private project details.
- **Add an example:** follow the short format in [examples](examples/README.md): technology → capability → supplied context → direct fit → unexpected fit → requirements/caveats. Link sources, prefer commit permalinks, and label VERIFIED / REPORTED / INFERRED POSSIBILITY. Do not submit full conversations or third-party code dumps.
- **Propose behavior changes:** describe the observed failure, the smallest instruction change, and a scenario that would reveal a regression. Preserve project-aware discovery and progressive disclosure.

Avoid making scoring the product, forcing generic brainstorming, assuming access to unavailable memory, or suppressing worthwhile ideas solely for cost or complexity. Source inspection is not runtime verification.

## Checks

Use Python 3.10+; no third-party packages are required:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
git diff --check
```

For behavior changes, run affected [acceptance scenarios](tests/acceptance.md) in fresh contexts with the changed skill. Record prompt, evidence, output, model/version, date, and pass/fail rationale. Structural checks do not grade an AI response. Clearly mark scenarios or host installations you did not run.

A pull request should explain the problem, change, and checks performed. Keep the installable skill self-contained and the repository small. Contributions use the existing [MIT license](LICENSE).
