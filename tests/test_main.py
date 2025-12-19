"""Unit tests for myapp.main."""
from myapp.main import greet


def test_greet_with_name():
    assert greet("Venkat") == "Hello, Venkat!"


def test_greet_default():
    assert greet(None) == "Hello, World!"
