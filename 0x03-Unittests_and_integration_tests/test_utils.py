#!/usr/bin/env python3
"""Module for testing utility functions."""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Verifies that `access_nested_map` retrieves the correct value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_exception: Exception,
            ) -> None:
        """Checks that `access_nested_map` raises the expected exception."""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit tests for the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            url: str,
            expected_payload: Dict,
            ) -> None:
        """Validates that `get_json` fetches and returns the correct JSON data."""
        mock_response = {'json.return_value': expected_payload}
        with patch("requests.get", return_value=Mock(**mock_response)) as mocked_get:
            self.assertEqual(get_json(url), expected_payload)
            mocked_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Unit tests for the `memoize` decorator."""
    def test_memoize(self) -> None:
        """Ensures that `memoize` caches the results of a method call."""
        class SampleClass:
            def compute(self):
                return 42

            @memoize
            def cached_property(self):
                return self.compute()

        with patch.object(
                SampleClass,
                "compute",
                return_value=lambda: 42,
                ) as mock_compute:
            instance = SampleClass()
            self.assertEqual(instance.cached_property(), 42)
            self.assertEqual(instance.cached_property(), 42)
            mock_compute.assert_called_once()
