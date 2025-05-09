"""
Unit tests for the Wallet class.

Nutzung:
    python -m pytest 1_test_wallet.py -v
"""

import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amout():
    """Teste ob neues Wallet ein Anfangsguthaben von 0 hat."""
    wallet = Wallet()
    assert wallet.balance == 0


def test_wallet_raises_insufficient_amount():
    wallet = Wallet(10)
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(20)


if __name__ == "__main__":
    w = Wallet(initial_amount=400)
    w.spend_cash(400)
