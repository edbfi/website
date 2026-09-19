# Dependency updates and validation

Renovate owns ongoing dependency merging after the protected native canary
[automation#39](https://github.com/edbfi/automation/pull/39). Native PR rebase merges
retain genuine author sign-offs. All application jobs—guard, hygiene and website—
must pass the fail-closed `ci / required` aggregate for the current head and base.
The separately required `policy / ci / policy` check validates Conventional Commit
titles, author-matching DCO, Renovate provenance, reviews and hold labels.
Protection requires both checks from GitHub Actions and up-to-date branches.
Release ages and review restrictions remain enforced; shared automation
configuration updates remain manual. Platform automerge is disabled, and the
legacy Actions merger and maintainer merge commands are retired.

Hygiene retains workflow lint, commit conventions and deployment freshness tests.
The website lane runs a strict build and generated-site checks, then serves the
built output and verifies routes and local assets through mandatory HTTP/content
assertions. This does not execute JavaScript or prove browser hydration. Explicit
CI dispatches verify the current PR/default revision at the start and aggregate;
they cannot substitute for a missing policy check. Policy metadata/review events
refresh independently without cancelling earlier evaluations. Inspect complete
default-branch CI and deployment results after each merge.

Successful exact-default CI triggers the existing Pages workflow for web.edb.fi.
It validates the requested revision and successful final push or dispatched CI
before building, and rechecks the revision before deployment. Manual deployment
remains available. Repository fork scanning is explicitly enabled.
