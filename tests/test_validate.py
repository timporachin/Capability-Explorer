"""Negative fixtures prove the package validator catches packaging regressions."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def test_package_passes(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_install_guide(self):
        (self.root / 'INSTALL.md').unlink()
        self.assertTrue(any('Missing: INSTALL.md' in e for e in validator.validate(self.root)))

    def test_bad_metadata(self):
        path = self.root / 'skills/capability-explorer/SKILL.md'
        path.write_text(path.read_text().replace('name: capability-explorer', 'name: wrong-name'))
        self.assertTrue(any('Skill name' in e for e in validator.validate(self.root)))

    def test_broken_relative_link(self):
        with (self.root / 'README.md').open('a') as f:
            f.write('\n[broken](absent.md)\n')
        self.assertTrue(any('Broken link' in e for e in validator.validate(self.root)))

    def test_wrong_version(self):
        (self.root / 'VERSION').write_text('99.0.0\n')
        self.assertTrue(any('Unexpected version' in e for e in validator.validate(self.root)))

    def test_unfinished_document(self):
        (self.root / 'unfinished.md').write_text('TO' + 'DO: complete me\n')
        self.assertTrue(any('Unfinished' in e for e in validator.validate(self.root)))


if __name__ == '__main__':
    unittest.main()
