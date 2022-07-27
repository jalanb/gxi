from unittest import TestCase

from semantic_version import Version

import gxi

class TestGxiVersion(TestCase):
    """gxi should have a version

    version should conform to SemVer
        so should have major/minor/patch attributes
    """

    def setUp(self):
        """Convert gxi's version to semantic"""
        self.version = Version(gxi.__version__)

    def test_major(self):
        """Project exists, major version is at least 0"""
        assert self.version.major >= 0

    def test_minor(self):
        """Project exists, minor version is at least 0"""
        assert self.version.minor >= 0

    def test_patch(self):
        """Some code exists, patch version is at least 1"""
        assert self.version.patch >= 1

