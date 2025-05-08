"""
`itertools` ist ein Standardmodul, das effiziente Iteratoren für
verschiedene kombinatorische, filternde und erweiternde Aufgaben bietet.
Die meisten Funktionen sind in C implementiert und daher deutlich
performanter als äquivalente Konstruktionen in reinem Python.

Das Modul ist besonders hilfreich bei speichereffizienten Operationen,
Stream-Verarbeitung, Lazy Evaluation und funktionalem Programmieren.

Dieses Skript zeigt einen Überblick über häufig genutzte Funktionen:
- repeat(), cycle(), compress(), permutations(), zip_longest(), groupby()
- eigene Hilfsfunktionen mit map() und groupby()
"""

import itertools as it

# repeat(): Wiederholt ein Element n-mal (hier: None)
result = it.repeat(None, times=3)
print("repeat:", next(result))
print("repeat:", next(result))
print("repeat:", next(result))

# repeat() in einer Schleife: führe eine Aktion n-mal aus
for _ in it.repeat(None, times=3):
    print("x")


# cycle(): Zyklisches Wiederholen einer Sequenz
cycle_iter = it.cycle([1, 2, 3])
print("cycle:", next(cycle_iter))  # 1
print("cycle:", next(cycle_iter))  # 2
print("cycle:", next(cycle_iter))  # 3
print("cycle:", next(cycle_iter))  # 1


# compress(): Filtert Elemente basierend auf Maske
text = "UVWXYZ"
maske = [1, 1, 0, 0, 0, 1]
ergebnis = it.compress(text, maske)
print("compress:", list(ergebnis))  # ['U', 'V', 'Z']


# permutations(): Alle Permutationen der Länge 2 aus "ABCD"
p = it.permutations("ABCD", 2)
print("permutations:", next(p))  # ('A', 'B')
print("permutations:", next(p))  # ('A', 'C')
print("permutations:", next(p))  # ('A', 'D')


# compress(): Schüler mit Note < 3 herausfiltern
students = ["Paul", "Peter", "Maria", "Klaus", "Mohammad"]
notes = [3, 1, 2, 5, 1]
ausgezeichnete = it.compress(students, map(lambda x: x < 3, notes))
print("Top-Noten:", list(ausgezeichnete))  # ['Peter', 'Maria', 'Mohammad']

# Alternative mit List Comprehension
print([students[i] for i, x in enumerate(notes) if x < 3])


# quantify(): Zählt, wie oft die Bedingung erfüllt ist
def quantify(iterable, pred=bool):
    "Zählt True-Werte bei Anwendung der Funktion pred()"
    return sum(map(pred, iterable))


print("Quantify < 3:", quantify([1, 2, 3, 4], lambda x: x < 3))  # 2


# all_equal(): Prüft, ob alle Elemente gleich sind (nützlich mit groupby)
def all_equal(iterable) -> bool:
    "Gibt True zurück, wenn alle Elemente gleich sind"
    g = it.groupby(iterable)
    return next(g, True) and not next(g, False)


print("equal 1,1,1:", all_equal([1, 1, 1]))  # True
print("equal 1,2,1:", all_equal([1, 2, 1]))  # False
print("equal a,a,a:", all_equal(["a", "a", "a"]))  # True


# pairwise(): Elementweise Paare bilden (ab Python 3.10)
try:
    from itertools import pairwise

    a = [1, 2, 3, 4, 5, 6]
    print("Pairwise:", list(pairwise(a)))
except ImportError:
    print("pairwise() ist erst ab Python 3.10 verfügbar.")

