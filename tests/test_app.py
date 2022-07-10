#!/usr/bin/env python3

import pytest

from tests import client


def test_index(client) -> None:
    req = client.get('/')
    assert req.status_code == 200 and "ePage" in req.text
