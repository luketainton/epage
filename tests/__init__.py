#!/usr/bin/env python3

"""PyTest unit tests."""

import pytest

from app.app import app


@pytest.fixture
def client():
    """Set up Flask client for use in tests."""
    client = app.test_client()
    yield client
