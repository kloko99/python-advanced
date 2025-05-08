"""
Thema: Operator Overloading – arithmetische & Vergleichsoperatoren

In Python lassen sich Operatoren wie +, -, ==, < usw. durch das
Überladen spezieller Methoden (z. B. __add__, __eq__) für eigene
Klassen anpassen.

So kann man benutzerdefinierte Objekte mit natürlichem Syntaxverhalten
versehen.
"""
from __future__ import annotations   # kann dann A in der Klasse benutzen

class A:
    def __init__(self, x):
        self.x = x

    def __gt__(self, other: A):
        if isinstance(other, A):
            if self.x > other.x:
                return True
            else:
                return False
        raise NotImplementedError("nicht implementiert")


a = A(3)
b = A(4)


print(a < b)