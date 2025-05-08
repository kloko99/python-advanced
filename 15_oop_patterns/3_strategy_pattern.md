# Strategy Pattern in Python

## Was ist das Strategy Pattern?

Das **Strategy Pattern** kapselt eine Familie von Algorithmen 
(oder Verhalten) in eigene Klassen und macht sie **austauschbar**. 
Der aufrufende Code kennt nur die **Schnittstelle**, nicht die konkrete Implementierung.

---

## Ziel

- Verhalten zur Laufzeit ändern können  
- Kein if/else-Spaghetti-Code  
- Leicht erweiterbar durch neue Strategien

---

## Beispiel: Zahlungsstrategien

```python
from abc import ABC, abstractmethod

class Zahlungsstrategie(ABC):
    @abstractmethod
    def zahle(self, betrag: float) -> None:
        pass

class Kreditkarte(Zahlungsstrategie):
    """Konkrete Strategie für Kreditkartenzahlung."""
    def zahle(self, betrag):
        print(f"Zahle {betrag} € mit Kreditkarte")

class PayPal(Zahlungsstrategie):
    """Konkrete Strategie für PayPal-Zahlung."""
    def zahle(self, betrag):
        print(f"Zahle {betrag} € mit PayPal")

class Bezahlvorgang:
    def __init__(self, strategie: Zahlungsstrategie):
        self.strategie = strategie

    def durchfuehren(self, betrag: float):
        self.strategie.zahle(betrag)


vorgang = Bezahlvorgang(Kreditkarte())
vorgang.durchfuehren(50)

vorgang.strategie = PayPal()
vorgang.durchfuehren(75)
```

---

## Vorteile

- Verhalten leicht austauschbar
- Offen für Erweiterung (neue Strategien), ohne bestehenden Code zu ändern
- Ermöglicht sauberen, testbaren Code

---

## Wann verwenden?

- Wenn sich eine Aktion auf verschiedene Arten durchführen lässt
- Wenn du Code vermeiden willst, der auf `if/elif` für Typ/Modus basiert
- Wenn sich Verhalten zur Laufzeit ändern soll

## Fazit

Das Strategy Pattern trennt **"was gemacht wird"** von **"wie es gemacht wird"**. 
Perfekt, um komplexes Verhalten sauber und austauschbar zu halten.

