# Abstrakte Klassen in Python

## Was ist eine abstrakte Klasse?

Eine **abstrakte Klasse** definiert eine gemeinsame Schnittstelle, 
aber **kann nicht direkt instanziiert werden**. Sie dient als **Vorlage** für Subklassen.

Verwendet wird sie mit dem Modul `abc` (`abstract base classes`).
Sie sind sehr ähnlich zu abstrakten Klassen in Java oder C#.
In C++ werden sie als **reine virtuelle Klassen** bezeichnet.

---

## Warum abstrakte Klassen?

- Schnittstellen klar definieren
- Subklassen zu bestimmten Methoden zwingen
- Einheitliches Verhalten für unterschiedliche Implementierungen

---

## Beispiel: Abstrakte Tier-Klasse
Die abstrakte Klasse `Tier` hat eine abstrakte Methode `sprich()`.
Diese muss von den Subklassen `Hund` und `Katze` implementiert werden.

```python
from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def sprich(self):
        pass

class Hund(Tier):
    def sprich(self):
        return "Wuff!"

class Katze(Tier):
    def sprich(self):
        return "Miau!"

# tier = Tier()       → TypeError (abstrakte Klasse)
hund = Hund()
print(hund.sprich())  # Wuff!
```

---

## Eigenschaften abstrakter Klassen

- Ableitung von `ABC` (Abstract Base Class)
- Mindestens eine Methode mit `@abstractmethod`
- Kann auch normale Methoden/Attribute enthalten
- Subklassen **müssen** alle `@abstractmethod`s implementieren

---

## Beispiel: Teilimplementierung

```python
class Fahrzeug(ABC):
    def start(self):
        print("Motor startet...")

    @abstractmethod
    def bewege(self):
        pass

class Auto(Fahrzeug):
    def bewege(self):
        print("Auto fährt los")

a = Auto()
a.start()      # Motor startet...
a.bewege()     # Auto fährt los
```

---
## Alternative zu abstrakten Klassen ist das Protocol
Allerdings wird das Protocol nur zur statischen Typprüfung verwendet.
Es findet keine Überprüfung zur Laufzeit statt.

```python
from typing import Protocol

class DruckerProto(Protocol):
    def drucken(self, text: str) -> None:
        ...

class MeinDrucker:
    def drucken(self, text: str) -> None:
        print(text)

def nutze_drucker(d: DruckerProto):
    d.drucken("Testseite")

nutze_drucker(MeinDrucker())
```


## Fazit

Abstrakte Klassen sind hilfreich, um **Verträge** im Code zu definieren. Sie sorgen dafür, dass Subklassen gewisse Methoden **implementieren müssen**, und sind besonders nützlich bei APIs, Frameworks und Architekturen mit Plug-ins oder Strategiemustern.

