"""Tests for safe-csrf-token."""

import pytest
from safe_csrf_token import token


class TestToken:
    """Test suite for token."""

    def test_basic(self):
        """Test basic usage."""
        result = token("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            token("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = token(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
