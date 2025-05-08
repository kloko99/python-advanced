"""
Einfache Wallet-Klasse zur Verwaltung eines Bargeldbetrags.

Beinhaltet Methoden zum Hinzufügen und Ausgeben von Geld
sowie einen simulierten API-Aufruf bei Einzahlung.
"""

import requests


class InsufficientAmount(Exception):
    """Fehler beim Versuch, zu viel Geld auszugeben."""

    pass


class ServiceUnavailable(Exception):
    """Fehler beim externen Zahlungsdienst."""

    pass


class Wallet:
    """
    Eine virtuelle Geldbörse mit Einzahl- und Auszahlfunktionen.
    """

    def __init__(self, initial_amount=0):
        """
        Initialisiert das Wallet mit einem Startguthaben.
        """
        self.balance = initial_amount

    def spend_cash(self, amount: int) -> None:
        """
        Gibt einen Betrag aus dem Wallet aus.
        Löst InsufficientAmount aus, wenn Guthaben nicht ausreicht.
        """
        if self.balance < amount:
            raise InsufficientAmount(f"Not enough available to spend {amount}")
        self.balance -= amount

    def add_cash(self, amount: int) -> None:
        """
        Erhöht das Guthaben ohne weitere Prüfung.
        """
        self.balance += amount

    def add_cash_extended(self, amount: int) -> None:
        """
        Erhöht das Guthaben nach API-Abfrage.
        Wenn der Service-Code nicht 200 ist, wird eine Ausnahme ausgelöst.
        """
        # Hinweis: Abhängigkeit zu externer API ist schlecht testbar
        status_code = self.update_payment_service(amount)
        if status_code != 200:
            raise ServiceUnavailable(f"Payment error. Status code: {status_code}")
        self.balance += amount

    def update_payment_service(self, amount: int) -> int:
        """
        Simuliert teuren API-Aufruf an einen Zahlungsdienst.
        Gibt den HTTP-Statuscode zurück.
        """
        print("Updating payment service with amount:", amount)
        response = requests.get("https://example.com", params={"amount": amount})
        return response.status_code


if __name__ == "__main__":
    # Testlauf für die Wallet-Methoden
    wallet = Wallet(100)
    print("Initial balance:", wallet.balance)

    # Einzahlung über externen Service
    wallet.add_cash_extended(50)
    print("Balance after adding cash:", wallet.balance)

    # Versuch, mehr auszugeben als verfügbar
    try:
        wallet.spend_cash(200)
    except InsufficientAmount as e:
        print(e)

    print("Final balance:", wallet.balance)
