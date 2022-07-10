#!/usr/bin/env python3

"""Tests for app/app.py"""


from tests import client  # pragma: no cover


def test_index(client) -> None:
    """Ensure that the index page is loaded correctly."""
    req = client.get('/')
    assert req.status_code == 200 and "ePage" in req.text
