# Dependency updates and validation

Renovate dependency updates, including majors and shared-policy versions, merge
unattended only after all four current-head jobs pass: guard, hygiene, website,
and ci / required. The checked action verifies genuine author sign-offs and
requests full final CI for the exact merged commit. Explicit dispatches validate
the current PR or default-branch SHA at the start and aggregate gate.

Hygiene retains full workflow lint and per-commit Conventional Commit/DCO checks.
The website lane retains its strict build. No dashboard approval, branch
protections or rulesets are configured; native GitHub automerge stays disabled.
Other changes retain exact head/base, full diff, author/DCO and full CI/artifact
review through the maintainer's ghmerge process, followed by final verification.

Successful exact-default CI triggers the existing Pages workflow for web.edb.fi.
It validates the requested revision and successful final push or dispatched CI
before building, and rechecks the revision before deployment. Manual deployment
remains available. Repository fork scanning is explicitly enabled.
