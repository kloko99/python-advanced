# Mocking mit Pytest in Python

Mocking ist ein wichtiger Bestandteil des Testens in Python, besonders wenn externe Abhängigkeiten oder teure Ressourcen involviert sind. In Pytest können Sie das `unittest.mock`-Modul verwenden, um Objekte zu mocken. Hier ist ein Tutorial, wie Sie Mocks in Verbindung mit dem `pytest` Framework erstellen können, illustriert am Beispiel einer hypothetischen `Wallet`-Klasse.

## Grundlagen

Ein Mock-Objekt simuliert das Verhalten eines echten Objekts. Es wird hauptsächlich verwendet, um die Interaktionen zwischen Code und externen Systemen zu isolieren, wodurch Tests schneller und zuverlässiger werden.

## Installation

Stellen Sie sicher, dass Sie Pytest installiert haben:

```bash
pip install pytest
```

`unittest.mock` ist ein Teil der Standardbibliothek, daher ist keine zusätzliche Installation erforderlich.

## Ein einfaches Mock-Beispiel

Nehmen wir an, wir haben eine `Wallet`-Klasse, die eine externe Zahlungs-API aufruft. Wir wollen diese API-Aufrufe mocken.

### Die Wallet-Klasse

```python
class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def add_cash(self, amount):
        self.balance += amount
        self.update_payment_service(amount)

    def update_payment_service(self, amount):
        # Stellt eine Verbindung zu einem externen Zahlungsdienst her
        pass
```

### Test mit Mock

Wir verwenden `unittest.mock` um die Methode `update_payment_service` zu mocken.

```python
import pytest
from unittest.mock import Mock
from wallet import Wallet

@pytest.fixture
def wallet():
    return Wallet(20)

def test_wallet_add_cash_with_mock(wallet):
    wallet.update_payment_service = Mock()
    wallet.add_cash(80)
    assert wallet.balance == 100
    wallet.update_payment_service.assert_called_with(80)
```

## Erweitertes Mocking

Sie können auch spezifizieren, wie der Mock reagieren soll, wenn er aufgerufen wird, beispielsweise bestimmte Werte zurückgeben oder Ausnahmen auslösen.

### Rückgabewerte und Seiteneffekte festlegen

```python
def test_wallet_add_cash_with_return_value(wallet):
    wallet.update_payment_service = Mock(return_value=True)
    wallet.add_cash(50)
    assert wallet.update_payment_service.called
    assert wallet.balance == 70
```

### Ausnahmen auslösen

```python
def test_wallet_add_cash_with_exception(wallet):
    wallet.update_payment_service = Mock(side_effect=Exception("Fehler!"))
    with pytest.raises(Exception) as e:
        wallet.add_cash(50)
    assert str(e.value) == "Fehler!"
```

