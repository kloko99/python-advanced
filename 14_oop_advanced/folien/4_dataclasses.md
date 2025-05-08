# Klassen VS Datenklassen VS NamedTuple

Wir können grundsätzlich zwischen eher datenzentrierten Klassen und
herkömmlichen Klassen unterscheiden. Datenzentrierte Klassen haben als
Hauptaufgabe oder gar als einzige Aufgabe das Halten von Daten. Ein klassisches
Beispiel ist die Klasse Point, die nur die Aufgabe hat, x- und y Wert
eines Punktes zu verwalten.

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    

    p1 = Point(0, 0)
    p2 = Point(0, 0)
    p1 == p2


Der Nachteil an dieser Klasse ist, dass bisher noch keine Methoden oder
arithemtischen Operatoren implementiert sind.

Für solche Klassen bietet Python bessere Alternativen zu "normalen" Klassen an.
Diese Alternativen haben den Vorteil, dass sie wichtige Dunder-Methoden wie
__str__, __repr__ sowie in gewissen Rahmen arithmetische Funktionen bereits
out-of-the-box implementieren.


## typing.NamedTuple: bei unveränderlichen Werten
Aus dem typing Modul lässt sich die Klasse NamedTuple importieren, die intern
einfach ein benanntes Tuple ist. Sie ist die erste Wahl bei unveränderlichen
Objekten.
   
    >>> from typing import NamedTuple
 
    >>> class Point(NamedTuple):
        ... """Point in euclidian plane"""
        ... x: int
        ... y: int
     
    >>> p1 = Point(0, 0)
    >>> p2 = Point(2, 2)
    >>> p1
    Point(x=0, y=0)
    >>> help(p1)
    >>> p1.__doc__
    Point in euclidian plane
    >>> p2 > p1
    True
    >>> p1.x = 2
    AttributeError: can't set attribute
    >>> p1 = Point(0, 0)
    >>> p2 = Point(0, 0)
    >>> p1 == p2
    True
    
    >>> # über NamedTuples lässt sich auch iterieren

    >>> for value in p1:
          print(value)
    1
    1
    1

## collections.namedtuple: bei unveränderlichen Werten
Wer es noch einfacher will, nimmt die namedtuple-Klasse aus dem
collections-Modul, allerdings mit dem Nachteil, dass hier kein Type-Hinting
möglich und nicht die Möglkichkeit eines Docstrings ist. 
namedtuple bietet eine einfache Konstruktor-Api, die einfach als String
übergeben wird und auch Default-Werte möglich sind (beginnend von rechts).
  
    >>> import math
    >>> from collections import namedtuple
    
    >>> Point = namedtuple("Point", "x y z", defaults=[0])
    >>> p1 = Point(1, 1)
    >>> p2 = Point(2, 2, 2)
    >>> p1
    Point(x=1, y=1, z=0)
    >>> p2
    Point(x=2, y=2, z=2)
    >>> p2 > p1
    True
    >>> p1 > p2
    False
    >>> math.dist(p1, p2)
    2.449489742783178
    >>> p1 = Point(1, 1, 1)
    >>> p2 = Point(1, 1, 1)
    >>> p1 == p2
    True

    >>> # über namedtuples lässt sich auch iterieren

    >>> for value in p1:
          print(value)
    1
    1
    1


## Datenklassen: bei veränderlichen Werten
Python bietet seit der Version 3.6 sogenannte Datenklassen an. Der Zweck der
Klasse wird schon im Namen deutlich. Auch sie bietet die notwendigen magischen
Methoden out-of-the-box, zusätzlich sind die Werte der Klasse aber 
veränderlich. Man kann sich eine Dataclass vorstellen, wie ein veränderbares
NamedTuple mit Typehints und Defaultwerten.


    >>> from dataclasses import dataclass

    >>> @dataclass
    ... class Person:
    ...     name: str
    ...     age: int
    ...     height: float
    ...     weight: float
    ...     country: str = "Canada"
    ...

    >>> jane = Person("Jane", 25, 1.75, 67)
    >>> jane
    Person(name='Jane', age=25, height=1.75, weight=67, country='Canada')
    >>> jane.name
    'Jane'
    >>> jane.name = "Jane Doe"
    >>> jane.name
    'Jane Doe'

## Datenklassen um Vergleichsoperatoren  erweitern 
Wir können den dataclass-Dekorator mit weiteren Argumenten erweitern. 
Mit `order=True` lassen sich zum Beispiel die  __lt__, __le__, __gt__, __ge__ - Methoden
generieren, um arithmetische Vergleiche zu realisieren. 


    >>> @dataclass(order=True)
    ... class Member:
    ...     name: str
    ...     age: int = field(compare=True)
    ... 
    >>> bob = Member(name="Bob", age=34)
    >>> alice = Member(name="Alice", age=23)
    >>> bob >= alice
    True
    >>> bob < alice
    False

## immutable Datenklassen
Datenklassen sind von Haus aus mutable, können also verändert werden.
Dazu kann das Keyword-Argument `frozen=True` genutzt werden.

    >>> @dataclass(order=True, frozen=True)
    ... class ImmutableMember:
    ...     name: str
    ...     age: int = field(compare=True)
    ... 
    >>> bob = Member(name="Bob", age=34)
    >>> bob.name = "Bobby"
    dataclasses.FrozenInstanceError: cannot assign to field 'name'

## Slots
Um einen gewissen Performance- und Speichergewinn zu erhalten, kann man
natürlich auch in Datenklassen Slots nutzen.


    >>> @dataclass
    ... class SlotPos:
    ...     __slots__ = ['lon', 'lat']
    ...     lon: float
    ...     lat: float
    ... 
    >>> p = SlotPos(-3.4, 33.3)
    >>> p

## eigene Methoden
Datenklassen lassen sich wie NamedTuples mit eigenen Methoden anreichern.
Darüberhinaus gibt es die magische Methode `__post_init__`, um beim Initialisieren einer Instanz  
Validierungen oder andere Aufgaben durchzuführen.

    >>> @dataclass
    ... class Citizen:
    ... 
    ... name: str
    ... email: str
    ... age: int

    ... def __post_init__(self):
            if self.age < 0:
                raise ValueError("Age cannot be negative.")

            if len(self.name) > 20:
                raise ValueError("Name cannot exceed 20 characters.")


    >>> donald = Citizen("Donald Duck", "donald.duck.com", 127)
