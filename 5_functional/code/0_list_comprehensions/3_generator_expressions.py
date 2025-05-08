"""
Generator Expressions ähneln List Comprehensions, erzeugen aber keine
vollständige Liste im Speicher. Stattdessen geben sie einen Iterator
zurück, der die Werte bei Bedarf (lazy evaluation) erzeugt.

Ein Iterator ist ein Objekt, das mit der Funktion `next()` den nächsten
Wert liefert. Sobald alle Werte verbraucht sind, ist der Iterator
erschöpft. Generatoren sind besonders speichereffizient bei großen
Datenmengen, da sie nicht alles auf einmal im Speicher halten.

In diesem Skript zeigen wir den Unterschied zwischen Generator Expressions
und List Comprehensions, insbesondere beim Speicherverbrauch.
"""

import sys

# List Comprehension: Erzeugt sofort eine komplette Liste im Speicher
liste = [x**2 for x in range(1000)]
print(liste[342])


# Generator Expression: Erzeugt Werte bei Bedarf (lazy evaluation)
generator_expression = (x**2 for x in range(1000))  # KEINE TUPLE Comprehensions
print(generator_expression)  # Iterator
print(next(generator_expression))   # 0
print(next(generator_expression))   # 1
print(next(generator_expression))   # 4
for i in generator_expression:
    print(i)


# print(next(generator_expression)) # StopIteration!!!!!

# Hinweis: Generator Expressions können direkt in Schleifen und
# Funktionen wie sum(), max(), etc. verwendet werden:
result = sum(i for i in range(832))
print(result)
