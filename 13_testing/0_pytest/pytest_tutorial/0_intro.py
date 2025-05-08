"""
# Pytest Tutorials:

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
