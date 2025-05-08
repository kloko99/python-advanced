"""
Unit tests for the Wallet class.

Nutzung:
    python -m pytest 1_test_wallet.py -v
"""

import pytest
from wallet import Wallet, InsufficientAmount


# TODO

if __name__ == "__main__":
    w = Wallet(initial_amount=400)
    w.spend_cash(400)
