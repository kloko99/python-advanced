"""
Aufgabe:
Erstelle eine Klasse Vector, die eine Klassen-Methode implementiert soll.

# Gegeben:

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y




# Gesucht:

die Klassen-Methode heisst from_dict und erstellt ein Vector-Objekt
auf Basis eines Dict in der Form:

d = {
    "x_point": 2,
    "y_point": 10,
}

oder

d = {
    "y_point": 11,
    "x_point": 3,
}

(Beachte, dass die Reihenfolge der Keys in dem Dict unterschiedlich sein kann!)

Zudem soll die Klasse die __repr__() - Methode implementieren

>>> v2 = Vector.from_dict(d)
>>> print(v2)
Vector(x=3, y=11)
>>> print(type(v2))
<class '__main__.Vector'>

"""

from __future__ import annotations
