# Einführung in Enums in Python

## Was ist ein Enum?

Ein **Enum** (Enumeration) ist eine Aufzählung benannter, unveränderlicher Werte. Ideal für feste Wertebereiche wie Wochentage, Statuscodes oder Farbnamen.

Enums verbessern Lesbarkeit, Validierung und Wartbarkeit – besonders bei festen Wertebereichen.

## Grundlegendes Beispiel

```python
from enum import Enum

class Farbe(Enum):
    ROT = 1
    GRUEN = 2
    BLAU = 3

print(Farbe.ROT)         # Farbe.ROT
print(Farbe.ROT.name)    # ROT
print(Farbe.ROT.value)   # 1
```

---

## Vergleiche & Identität

```python
print(Farbe.ROT == Farbe['ROT'])   # True
print(Farbe(1) == Farbe.ROT)       # True
```

---

## IntEnum: Verhalten wie int

```python
from enum import IntEnum

class Status(IntEnum):
    OK = 200
    NOT_FOUND = 404

print(Status.OK + 1)     # 201 → funktioniert wie ein int
print(isinstance(200, Status))  # False (Achtung!)
```

---

## StrEnum (ab Python 3.11): Verhalten wie str

```python
from enum import StrEnum

class Tier(StrEnum):
    HUND = "hund"
    KATZE = "katze"

print(Tier.HUND.upper())  # HUND
print("hund" in Tier.__members__.values())  # False!
```

---

## Durch alle Werte iterieren

```python
for farbe in Farbe:
    print(farbe.name, farbe.value)
```

---

## Enums vergleichen

```python
farbe = Farbe.ROT
if farbe is Farbe.ROT:
    print("Es ist rot!")
```

---

## Fazit

- `Enum`: Basis für symbolische Konstanten
- `IntEnum`: wie `Enum`, aber verhält sich wie `int`
- `StrEnum`: wie `Enum`, aber wie `str` benutzbar (ab 3.11)


