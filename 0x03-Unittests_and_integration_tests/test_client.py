#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method of GithubOrgClient."""
        test_client = GithubOrgClient(org_name)
        mock_get_json.return_value = {"login": org_name}

        result = test_client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"login": org_name})


if __name__ == '__main__':
    unittest.main()
