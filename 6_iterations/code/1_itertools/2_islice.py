"""
`islice()` ist eine Funktion aus dem Modul `itertools`, mit der man
aus einem beliebigen Iterator einen Ausschnitt entnehmen kann – ähnlich
wie bei einem Slice in einer Liste, aber speichereffizient auch für
große oder unendliche Iteratoren.

Vorteile:
- funktioniert mit Generatoren und Streams
- verhindert unnötigen Speicherverbrauch
- erlaubt gezielte Extraktion (z. B. Zeilenbereiche, Zeitfenster)

Dieses Skript zeigt Grundlagen und ein praxisnahes Beispiel für mathematische
Filterung und gezielten Zugriff per `islice`.
"""

import random
import itertools as it
import math

# iterator = enumerate(["a", "b", "c"])
# print(iterator[0:2])
# exit()

# ----------------------------------
# Grundlagen: islice() auf riesiger Range  [0:4]
# ----------------------------------
a = range(800_000_000)
print("Range-Objekt:", a)

# Hole nur Elemente 200_000_000 bis 200_000_099
iterator = it.islice(a, 200_000_000, 200_000_005)
print("Startwert:", next(iterator))
for v in iterator:
    print(v)


# ----------------------------------
# Real-World-Beispiel: Zahlen mit ganzzahliger Wurzel & Kubikwurzel
# ----------------------------------
def ist_perfekte_wurzelkombination(i):
    sq = math.sqrt(i)
    cb = math.cbrt(i)
    return sq.is_integer() and cb.is_integer()


# Generator für passende Tupel (Zahl, Wurzel, Kubikwurzel)
zahlen = (
    (i, int(math.sqrt(i)), int(math.cbrt(i)))
    for i in range(500_000_000)
    if ist_perfekte_wurzelkombination(i)
)

# Sammle die ersten 10 passenden Ergebnisse
erste_10 = [next(zahlen) for _ in range(10)]

# Extrahiere gezielt einen Teilbereich daraus mit islice
auswahl = it.islice(erste_10, 3, 5)
print("Auswahl aus Wurzelkombinationen:", list(auswahl))


# ----------------------------------
# Beispiel: Textverarbeitung – nur bestimmte Zeilen eines Texts extrahieren
# ----------------------------------
text = """
Zeile 1: Überschrift
Zeile 2: Einleitung
Zeile 3: Inhalt A
Zeile 4: Inhalt B
Zeile 5: Inhalt C
Zeile 6: Fazit
Zeile 7: Abspann
""".strip().split("\n")

mittelteil = it.islice(text, 2, 5)  # Zeilen 3 bis 5 (Index 2–4)
print("Mittlerer Textabschnitt:")
for zeile in mittelteil:
    print(zeile)


# ----------------------------------
# Aufgabe für Fortgeschrittene:
# ----------------------------------
# Gegeben ist ein endloser Generator von Zufallszahlen zwischen 1 und 100.
# 1. Filtere mit einer Generatorfunktion alle Zahlen, die Vielfache von 3 UND 5 sind.
# 2. Nutze `islice()`, um die ersten 10 davon auszugeben.


def zufallszahlen():
    while True:
        yield random.randint(1, 100)


def vielfache_von_3_und_5(quelle):
    return (x for x in quelle if x % 3 == 0 and x % 5 == 0)


quelle = zufallszahlen()
gefiltert = vielfache_von_3_und_5(quelle)

auswahl = it.islice(gefiltert, 10)
