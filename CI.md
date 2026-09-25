# Dependency updates and validation

Renovate owns ongoing dependency merging through the shared `automerge.json`
preset of automation `v4.0.0`: it arms GitHub auto-merge with the rebase strategy,
so merges retain genuine author sign-offs and happen only after every required
check passes. All application jobs—hygiene and website—must pass the
fail-closed `ci / required` aggregate for the current head and base.
The separately required `policy / ci / policy` check validates Conventional Commit
titles, author-matching DCO, Renovate provenance, reviews and hold labels.
Protection requires both checks from GitHub Actions and up-to-date branches.
Release ages and review restrictions remain enforced; shared automation
configuration updates remain manual. The legacy Actions merger and maintainer
merge commands are retired.

Hygiene retains workflow lint, commit conventions and deployment freshness tests.
The website lane runs a strict build and generated-site checks, then serves the
built output and verifies routes and local assets through mandatory HTTP/content
assertions. This does not execute JavaScript or prove browser hydration. A manual
CI dispatch takes no inputs and cannot substitute for a missing policy check.
Policy metadata/review events refresh independently without cancelling earlier
evaluations; after a pass, policy re-runs the other event's older failed verdict
for the same head. Inspect complete default-branch CI and deployment results
after each merge.

Successful exact-default CI triggers the existing Pages workflow for web.edb.fi.
It validates that the revision is current master with successful final push or
dispatched CI before building, and rechecks the revision before deployment.
Manual deployment remains available. Repository fork scanning is explicitly enabled.
