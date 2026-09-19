"""Deployment refuses stale revisions and unsuccessful latest CI attempts."""
import os
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch
import json

SHA = 'a' * 40
SCRIPT = Path(__file__).resolve().parents[1] / 'tools/check_deploy.py'


class DeploymentTest(unittest.TestCase):
    def evaluate(self, branch=SHA, runs=None):
        if runs is None:
            runs = [dict(event='push', head_sha=SHA, head_branch='master',
                         run_number=2, run_attempt=1, status='completed', conclusion='success')]
        responses = [json.dumps({'commit': {'sha': branch}}), json.dumps({'workflow_runs': runs})]
        with patch.dict(os.environ, {'GITHUB_REPOSITORY': 'edbfi/website', 'DEPLOY_SHA': SHA}), \
             patch('subprocess.check_output', side_effect=responses):
            runpy.run_path(str(SCRIPT), run_name='__main__')

    def test_current_success(self):
        self.evaluate()

    def test_stale_revision(self):
        with self.assertRaisesRegex(SystemExit, 'no longer current'):
            self.evaluate(branch='b' * 40)

    def test_missing_ci(self):
        with self.assertRaisesRegex(SystemExit, 'not successful'):
            self.evaluate(runs=[])

    def test_newer_pending_or_failed_attempt_wins(self):
        for status, conclusion in [('queued', None), ('completed', 'failure'), ('completed', 'cancelled'), ('completed', 'skipped')]:
            with self.subTest(conclusion=conclusion):
                old = dict(event='push', head_sha=SHA, head_branch='master', run_number=2,
                           run_attempt=1, status='completed', conclusion='success')
                new = dict(old, run_attempt=2, status=status, conclusion=conclusion)
                with self.assertRaisesRegex(SystemExit, 'not successful'):
                    self.evaluate(runs=[old, new])

    def test_pr_ci_is_insufficient(self):
        with self.assertRaisesRegex(SystemExit, 'not successful'):
            self.evaluate(runs=[dict(event='pull_request', head_sha=SHA, head_branch='master',
                                    run_number=2, run_attempt=1, status='completed', conclusion='success')])


if __name__ == '__main__':
    unittest.main()
