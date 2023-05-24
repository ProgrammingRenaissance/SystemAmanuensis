"""Test driver for the InstallationConfiguration module."""

import unittest
import sys
from installationConfiguration import InstallationConfiguration


class TestInstallationConfiguration(unittest.TestCase):
    """Control testing of the Installation Configuration Module."""

    def test_noConfigurations(self) -> None:
        """
        Tests the basic infrastructure.

        If nothing is reported, the test was successful.
        """
        icg: InstallationConfiguration = InstallationConfiguration()
        icg.main()

    def test_EmptyConfiguration(self) -> None:
        """
        Tests an empty configuration by itself.

        If nothing is reported, the test was successful.
        """
        icg: InstallationConfiguration = InstallationConfiguration({})
        icg.main()


if __name__ == "__main__":
    unittest.main()
sys.exit(0)
