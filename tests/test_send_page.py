#!/usr/bin/env python3

from app.send_page import send_page


def test_send_page_no_env() -> None:
    result = send_page(
        name='Unit Test',
        email='none@none.com',
        message='Unit Test'
    )
    assert result[0] == False and result[1].get('token') == 'invalid'
