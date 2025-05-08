"""
Die Funktion `map()` ist eine eingebaute Funktion in Python, mit der
man eine Funktion auf jedes Element eines iterierbaren Objekts anwenden
kann. Dabei entsteht ein Iterator mit den Ergebnissen der Anwendung.

Syntax: map(funktion, iterable)

Oft wird `map()` in Kombination mit `lambda` oder einer definierten
Funktion genutzt, um Transformationen effizient durchzuführen.

Wichtig: Der Rückgabewert von `map()` ist ein Iterator, keine Liste.
Will man das Ergebnis als Liste haben, muss man `list()` verwenden.

Reale Anwendungsbeispiele:
- Umrechnung von Einheiten (z. B. Celsius → Fahrenheit)
- Extraktion oder Transformation von Feldern in Datensätzen
- Normalisierung oder Formatierung von Strings

Dieses Skript zeigt den Einsatz von `map()` in mehreren realistischen
Szenarien.
"""

import timeit

# Alle Elemente der String-Liste in Int konvertieren
numbers_str = ["3", "34", "34", "23"]
numbers = list(map(int, numbers_str))


# Quadriere alle Zahlen in einer Liste
numbers = [1, 3, 4]

quadrierte_zahlen = []
for i in numbers:
    quadrierte_zahlen.append(i**2)

# in python bevorzugte Schreibweise (laut GvR), pythonisch
quadrierte_zahlen = [i**2 for i in numbers]

# via Map
quadrierte_zahlen_neu = map(lambda n: n**2, numbers)
print(list(quadrierte_zahlen_neu))  # ein Iterator, ein Map-Objekt


# Länge jedes Worts in einer Liste berechnen
words = ["the", "brown", "fox", "jumps"]
print(list(map(lambda s: len(s), words)))
print(list(map(len, words)))

# Zwei Listen elementweise addieren
def summe(a, b):
    return a + b


lst1 = [2, 4, 6, 8]
lst2 = [1, 3, 5, 7, 9]

print("Summe:", list(map(summe, lst1, lst2)))  # [3, 7, 11, 15]

# ###########################################
# Drei Listen elementweise multiplizieren
# ###########################################


def multiply(a, b, c):
    return a * b * c


lst3 = [2, 3, 5, 7, 11, 13, 17]
lst2 = [1, 3, 5, 7, 9]
lst1 = [2, 4, 6, 8]

print("Multiply:", list(map(multiply, lst1, lst2, lst3)))

# zip-Funktion
zip_object = zip(lst1, lst2)  # [(1,2), (3, 4), (32, 5)]
for a, b in zip_object:
    print(a, b)


# Alternative mit zip und List Comprehension
multiply_alternative = [a * b * c for a, b, c in zip(lst1, lst2, lst3)]


# Aufgabe: erstelle eine Funktion, die als Parameter eine Liste erwartet und
# jeweils den ersten Buchstabens eines Elements in Uppercase wandelt.
# z.b eggs => Eggs spam whomp = Spam Whomp
# Return Liste
monty = ["eggs", "spam whomp", "cheese", "ham"]


# Messung Listen Comprehension vs. map
# List Comprehension ist unter Umständen etwas langsamer
