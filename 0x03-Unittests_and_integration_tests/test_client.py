#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class."""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public_repos method of GithubOrgClient."""
        # Mocked payload for get_json
        mocked_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Set up the mocks
        mock_public_repos_url.return_value = "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = mocked_payload

        # Instantiate the GithubOrgClient
        test_client = GithubOrgClient("testorg")

        # Call the public_repos method
        result = test_client.public_repos()

        # Assert that the result is as expected
        self.assertEqual(result, ["repo1", "repo2", "repo3"])

        # Assert that _public_repos_url property and get_json were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")


if __name__ == '__main__':
    unittest.main()
