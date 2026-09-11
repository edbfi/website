#!/usr/bin/env python3
"""Check generated canonical pages, assets and deployment domain."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
expected = {p.stem for p in (root / 'docs/containers').glob('*.md')}
if expected != {'base-image', 'caddy', 'obzorarr', 'qbittorrent', 'qflood', 'sabnzbd'}:
    raise SystemExit('Unexpected container inventory')
if (root / 'docs/CNAME').read_text().strip() != 'web.edb.fi':
    raise SystemExit('Incorrect custom domain')
for name in expected:
    html = (root / '.build/containers' / name / 'index.html').read_text()
    if 'https://web.edb.fi/containers/' + name + '/' not in html:
        raise SystemExit('Incorrect canonical: ' + name)
    if 'ghcr.io/engels74' in html or 'engels74.net' in html:
        raise SystemExit('Obsolete image/domain reference: ' + name)
    json.loads((root / 'docs/containers' / (name + '-tags.json')).read_text())
for asset in ['img/edbfi.svg', 'javascripts/tagcopy.js', 'javascripts/tablesort.js',
              'stylesheets/extra-13.css', 'stylesheets/extra-custom.css']:
    if not (root / '.build' / asset).is_file():
        raise SystemExit('Missing generated asset: ' + asset)
print('Six canonical container pages, tag data, domain and runtime assets verified')
