import pytest
from app import app, routes


def test_index():
    result = routes.index()
    assert type(result) == str
