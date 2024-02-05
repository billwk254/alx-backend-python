#!/usr/bin/env python3
"""Unit tests for utils.memoize decorator."""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator."""

    class TestClass:
        """Test class for memoize decorator."""
        def a_method(self):
            """A method returning 42."""
            return 42

        @memoize
        def a_property(self):
            """A memoized property."""
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_method):
        """Test memoize decorator."""
        test_instance = self.TestClass()

        # Call a_property twice
        result1 = test_instance.a_property
        result2 = test_instance.a_property

        # Assert that a_method is only called once
        mock_method.assert_called_once()

        # Assert that the results are correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
