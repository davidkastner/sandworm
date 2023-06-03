"""
Unit and regression test for the sandworm package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import sandworm


def test_sandworm_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "sandworm" in sys.modules
