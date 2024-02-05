#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class."""
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test has_license method of GithubOrgClient."""
        # Instantiate the GithubOrgClient
        test_client = GithubOrgClient("testorg")

        # Call the has_license method
        result = test_client.has_license(repo, license_key)

        # Assert that the result is as expected
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
