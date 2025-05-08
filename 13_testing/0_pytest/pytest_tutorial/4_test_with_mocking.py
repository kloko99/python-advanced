"""
Unittests mit Mocking

Mocking erlaubt dir, externe oder teure Aufrufe im Test zu simulieren und
stattdessen zu kontrollieren, ob sie korrekt aufgerufen wurde.

- Verwende Mock, wenn du das Zielobjekt direkt besitzt (z. B. Methoden
deiner eigenen Klasse).

- Verwende patch, wenn du externe Aufrufe oder Module temporär
  austauschen willst.

python -m pytest 4_test_with_mocking.py

"""

import pytest
from unittest.mock import Mock, patch
from wallet import Wallet


@pytest.fixture
def wallet():
    return Wallet(20)
