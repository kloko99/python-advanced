"""
Die Funktion `reduce()` stammt aus dem Modul `functools` und wird
verwendet, um eine Folge von Werten zu einem einzelnen Ergebnis
zusammenzufassen, indem eine Funktion wiederholt auf jeweils zwei
Elemente angewendet wird.

Syntax: reduce(funktion, sequenz[, startwert])

Typische Anwendungen:
- Aufsummieren oder Multiplizieren von Zahlen
- Finden von Minima oder Maxima
- Verketten von Strings
- Aggregation oder Akkumulation beliebiger Daten

Hinweis:
Ohne Startwert beginnt `reduce()` mit den ersten beiden Elementen.
Mit Startwert wird dieser als Anfangswert verwendet.

Dieses Skript enthält praktische Beispiele für die Nutzung von `reduce()`
in Kombination mit vordefinierten und anonymen Funktionen sowie
Operatoren.
"""

from functools import reduce
import operator as op

# Produkt aller Zahlen in der Liste berechnen
num = [2, 4, 5]
print(reduce(op.mul, num))



# Verketten von Zeichen zu einem String
num2 = ["B", "O", "R"]

# Produkt mit Startwert 0 ergibt 0
num = [2, 4, 5, 9]

# Minimum aus einer Liste berechnen
num = [0.1, 5, 9, 1]


# Logging innerhalb einer eigenen Multiplikationsfunktion
def produkt(x, y):
    print("x:", x)
    print("y:", y)
    print("res:", x * y)
    return x * y


print("num:", num)
produkt_result = reduce(produkt, num)
print("produkt:", produkt_result)


# Schnittmenge mehrerer Sub-Listen berechnen (Intersection)
input_list = [[1, 2, 3, 4, 5, 9], [2, 3, 4, 5, 6, 1], [3, 4, 5, 6, 7, 1]]
result = reduce(set.intersection, map(set, input_list))
print("Intersection:", result)