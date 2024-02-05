#!/usr/bin/env python3
"""Integration tests for client.GithubOrgClient class."""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


@parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
                     [(org_payload, repos_payload, expected_repos, apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        # Start a patcher for requests.get
        cls.get_patcher = patch('client.requests.get')

        # Mock requests.get to return example payloads
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        # Stop the patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method of GithubOrgClient."""
        # Instantiate the GithubOrgClient
        test_client = GithubOrgClient("testorg")

        # Call the public_repos method
        result = test_client.public_repos()

        # Assert that the result is as expected
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license argument of GithubOrgClient."""
        # Instantiate the GithubOrgClient
        test_client = GithubOrgClient("testorg")

        # Call the public_repos method with license="apache-2.0"
        result = test_client.public_repos(license="apache-2.0")

        # Assert that the result is as expected
        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
