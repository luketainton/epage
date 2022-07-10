#!/usr/bin/env python3

import pytest

from app.app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client
