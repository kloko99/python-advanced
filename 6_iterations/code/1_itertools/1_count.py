"""
Dieses Skript demonstriert den Einsatz von `itertools.count()`, einer
Funktion aus dem Modul `itertools`.

`count(start=0, step=1)` erzeugt eine unendliche Folge von Werten, beginnend
bei `start` mit dem Abstand `step`. Das ist besonders nützlich, wenn man
laufende Zähler benötigt, etwa zum numerischen Labeln von Daten oder zur
Erzeugung fortlaufender IDs.

Das Modul ist ideal für speicherschonendes, lazy-basiertes Zählen und
kombiniert sich gut mit Funktionen wie `zip()`, `map()` oder `islice()`.
"""

import itertools as it

# ---------------------------------
# Einfaches Hochzählen mit count()
# ---------------------------------
result = it.count(10, step=1)
print(next(result))  # 10
print(next(result))  # 11
print(next(result))  # 12

# enumerate
names = ["Bob", "alice"] # 1: Bob, 2: Alice

# Klassiche Variante
i = 1 
for name in names:
    print(f"{i}: {name}")
    i += 1

# pythonische VAriante
for index, name in enumerate(names, start=1):   # [(1, Bob), (2, Alice)]
    print(f"{index}: {name}")


# ---------------------------------
# Kombination mit zip(): Monate mit Verkaufszahlen verbinden
# ---------------------------------
sales_per_month = [24, 12, 34, 22, 55, 11, 234, 22, 44, 12, 42, 1562]
month_sales = list(zip(it.count(start=1), sales_per_month))
print("Monatlicher Umsatz (itertools):", month_sales)

# Alternative mit List Comprehension
month_sales_alt = [(month, sale) for month, sale in enumerate(sales_per_month, start=1)]
print("Monatlicher Umsatz (klassisch):", month_sales_alt)


# ---------------------------------
# Generiere die ersten 5 geraden Zahlen
# ---------------------------------
evens = it.count(start=0, step=2)
print("Gerade Zahlen:", [next(evens) for _ in range(5)])


# ---------------------------------
# Rückwärts zählen mit negativem Schrittwert
# ---------------------------------
negativ_counter = it.count(10, step=-1.5)
print("Rückwärts:", next(negativ_counter))  # 10
print("Rückwärts:", next(negativ_counter))  # 8.5
print("Rückwärts:", next(negativ_counter))  # 7.0


# ---------------------------------
# Mathematische Funktion mit count() und map()
# ---------------------------------
def f(x):
    return 5 * x**2 + x - 2


reihe = map(f, it.count())
print("Funktionswerte:", next(reihe))
print("Funktionswerte:", next(reihe))
