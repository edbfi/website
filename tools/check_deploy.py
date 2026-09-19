#!/usr/bin/env python3
"""Permit deployment only for the current default revision with complete CI."""
import json
import os
import re
import subprocess


def read(path):
    return json.loads(subprocess.check_output(['gh', 'api', path], text=True))


repo = os.environ['GITHUB_REPOSITORY']
sha = os.environ['DEPLOY_SHA']
if not re.fullmatch(r'[0-9a-f]{40}', sha):
    raise SystemExit('Invalid deployment revision')
branch = read(f'repos/{repo}/branches/master')
if branch['commit']['sha'] != sha:
    raise SystemExit('Deployment revision is no longer current master')
runs = read(f'repos/{repo}/actions/workflows/ci.yml/runs?head_sha={sha}&branch=master&per_page=100')['workflow_runs']
runs = [run for run in runs if run['event'] in {'push', 'workflow_dispatch'}]
latest = max(runs, key=lambda run: (run['run_number'], run['run_attempt']), default=None)
if not (latest and latest['head_sha'] == sha and latest['head_branch'] == 'master'
        and latest['status'] == 'completed' and latest['conclusion'] == 'success'):
    raise SystemExit('Latest complete master CI is not successful for this exact revision')
print('Current master and latest successful CI verified: ' + sha)
