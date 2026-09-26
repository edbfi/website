# Container documentation

Documentation for the retained edbfi container images at https://web.edb.fi. Based on hotio/website, with canonical content maintained in edbfi/repo-patches.

## Validate locally

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/zensical build --strict
python3 tools/check_site.py
```

Upstream updates use the explicit revision in .upstream.json and candidates prepared with `tools/prepare_sync.py` in edbfi/repo-patches. Review the generated patch on a feature branch before merging. Preserve the site overlay and existing tag data. Never force-replace master.

The GPL-3.0 license and upstream attribution are retained. Canonical overlay contributions originate in the AGPL-3.0 repo-patches repository; its license is included as LICENSE-overlay. Image availability follows individual migration and publication; pages for later containers remain documented ahead of their migration.
