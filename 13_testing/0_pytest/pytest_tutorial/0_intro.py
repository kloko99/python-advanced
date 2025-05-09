"""
# Pytest Tutorials:

pip install pytest

## Pytest Primer
https://realpython.com/pytest-python-testing/

## Django Pytest
https://djangostars.com/blog/django-pytest-testing/

## good pytest tutorial
https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

call this: pytest 0_intro.py
"""

import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError("Please provide a string argument")
    return x.capitalize()


def capital_case_old(x):
    return x.capitalize()


# assert 1 == 2, "1 und 1 muss wahr sein"
def test_capital_case():
    assert capital_case("hamburg") == "Hamburg"
    assert capital_case("a b") == "A b"
