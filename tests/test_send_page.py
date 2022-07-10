#!/usr/bin/env python3

"""Tests for app/send_page.py"""

from app.send_page import send_page


def test_send_page_no_env() -> None:
    """Ensure the API returns an error if no API key specified."""
    result = send_page(
        name='Unit Test',
        email='none@none.com',
        message='Unit Test'
    )
    assert not result[0] and result[1].get('token') == 'invalid'
