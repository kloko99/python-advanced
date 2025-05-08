"""
Thema: __post_init__ in @dataclass – Nachbearbeitung nach der Initialisierung

In einer mit `@dataclass` dekorierten Klasse wird der Konstruktor
(__init__) automatisch generiert. Wenn man zusätzliche Logik nach der
Initialisierung aller Felder ausführen möchte, kann man die Methode
__post_init__ definieren.

Diese Methode wird **automatisch nach __init__ aufgerufen** und eignet
sich besonders für:

- Validierung abhängiger Felder
- Umwandlung von Rohwerten in ein gewünschtes Format
- Ableitung von Werten aus anderen Feldern
- Aufruf externer Initialisierungsschritte

Beispiel:

    @dataclass
    class Person:
        name: str
        age: int

        def __post_init__(self):
            if self.age < 0:
                raise ValueError("Alter darf nicht negativ sein.")

__post_init__ ist eine einfache Möglichkeit, individuelle Logik in
automatisch generierten Klassen unterzubringen.
"""

from dataclasses import dataclass, asdict, field


@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 18:
            raise ValueError("Du bist zu jung für diesen Content.")


bob = Person("Bob", 17)  # Schlägt fehl, weil Business-Regel in post_init verletzt wurde
