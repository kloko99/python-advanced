"""
Dieses Skript behandelt `itertools.chain()` – eine Funktion zur effizienten
Verkettung mehrerer iterierbarer Objekte, als wären sie ein einziges.

`chain(it1, it2, ...)` erzeugt einen Iterator, der nacheinander durch alle
elemente in den übergebenen Iterables läuft. Das ist besonders nützlich, wenn:

- man mehrere Listen oder Generatoren zusammen verarbeiten möchte,
- große Datenmengen iterativ verarbeitet werden sollen, ohne sie vorher
  zu kopieren oder zusammenzufügen,
- Eingaben aus verschiedenen Quellen sequentiell behandelt werden.

**Vorteile gegenüber Listenverkettung (`+`):**
- keine Kopie im Speicher – besonders bei großen Datenmengen relevant
- funktioniert mit beliebigen Iterables (z. B. auch Generatoren)
- eignet sich ideal für Lazy Evaluation, z. B. beim Parsen, Log-Auswertung, Streaming

"""

import itertools as it

# Beispiel: Zeichenfolgen zusammenfassen ohne explizite Verkettung
result = it.chain("ABC", "DEF")
print(next(result))  # A
print(next(result))  # B
print(next(result))  # C
print(next(result))  # D
print(next(result))  # E
print(next(result))  # F

# Vollständig iterieren
print("Komplett durchlaufen:", list(it.chain("123", "456", "789")))


# Beispiel: Listen kombinieren, z. B. bei Logdateien aus verschiedenen Quellen
logs1 = ["log1: ok", "log1: error"]
logs2 = ["log2: warn", "log2: ok"]
logs3 = ["log3: fail"]

alle_logs = it.chain(logs1, logs2, logs3)
for eintrag in alle_logs:
    print(eintrag)


# Vorteil: Auch kombinierbar mit Generatoren oder Streams


# Generator für einfache Datenquelle
def gen_a():
    yield from ["a1", "a2"]


def gen_b():
    yield from ["b1", "b2", "b3"]


kombiniert = it.chain(gen_a(), gen_b())
print("Generator kombiniert:", list(kombiniert))
