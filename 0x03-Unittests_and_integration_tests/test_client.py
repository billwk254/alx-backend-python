#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class."""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    def test_public_repos_url(self):
        """Test _public_repos_url property of GithubOrgClient."""
        # Known payload to be returned by the patched org property
        known_payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

        # Patch the org property to return the known payload
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = known_payload

            # Instantiate the GithubOrgClient
            test_client = GithubOrgClient("testorg")

            # Get the value of _public_repos_url
            result = test_client._public_repos_url

            # Assert that the result is as expected
            self.assertEqual(result, "https://api.github.com/orgs/testorg/repos")


if __name__ == '__main__':
    unittest.main()
