# Factory Pattern in Python

## Idee

Das Factory Pattern kapselt die Objekterzeugung und gibt statt konkreter Klasseninstanzierungen eine zentrale Erzeugerfunktion zurück. Vorteil: Flexible, austauschbare Objekte.

---

## Beispiel 1: Einfache Factory-Funktion

```python
class Hund:
    def sprechen(self):
        return "Wuff!"

class Katze:
    def sprechen(self):
        return "Miau!"

def tier_factory(art):
    if art == "hund":
        return Hund()
    elif art == "katze":
        return Katze()
    raise ValueError("Unbekanntes Tier")

tier = tier_factory("hund")
print(tier.sprechen())  # Wuff!
```

---

## Beispiel 2: Registrierende Factory (erweiterbar)

```python
class TierFactory:
    _registry = {}

    @classmethod
    def registrieren(cls, name, typ):
        cls._registry[name] = typ

    @classmethod
    def erzeugen(cls, name, *args, **kwargs):
        if name not in cls._registry:
            raise ValueError(f"{name} nicht registriert")
        return cls._registry[name](*args, **kwargs)

# Registrierung über Subklassen
class Tier:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        TierFactory.registrieren(cls.__name__.lower(), cls)

class Fisch(Tier):
    def sprechen(self):
        return "blubb"

f = TierFactory.erzeugen("fisch")
print(f.sprechen())  # blubb
```

---

## Vorteile

- Zentrale Kontrolle über Objekt-Erzeugung
- Austauschbarkeit konkreter Klassen
- Erweiterbar ohne bestehende Logik zu ändern

---

## Fazit

Das Factory Pattern ist nützlich, wenn viele Varianten eines Objekts erzeugt werden sollen – besonders bei Plugin- oder Komponenten-Systemen.
