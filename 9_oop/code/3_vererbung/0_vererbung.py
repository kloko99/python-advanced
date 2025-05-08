"""
Thema: Vererbung in Python – Klassen erweitern und wiederverwenden

Vererbung erlaubt es, eine Klasse (Basisklasse) zu definieren, deren
Eigenschaften und Methoden von anderen Klassen (Subklassen) übernommen
werden.

Die Syntax lautet: class Unterklasse(Oberklasse):
Dabei kann man geerbte Methoden überschreiben oder erweitern.

Python unterstützt auch Mehrfachvererbung, was vorsichtig verwendet
werden sollte.

Vererbung fördert Code-Wiederverwendung und hilft bei der Modellierung
von „ist-ein“-Beziehungen.
"""
class Tier:
    """Basisklasse Tier."""
    def __init__(self, name, year):
        self.name = name
        self.year = year
    


class Schaf(Tier):
    """Spezialfall eines Tiers."""
    def __init__(self, name, year, wollmenge):
        super().__init__(name, year)
        self.wollmenge = wollmenge
        



schaf = Schaf("Dolly", 2024, wollmenge=100)
print(schaf.name, schaf.year, schaf.wollmenge)