"""
Thema: Klassenmethoden in Python – @classmethod

Klassenmethoden sind Methoden, die auf die Klasse selbst statt auf
eine Instanz zugreifen. Sie werden mit dem Decorator @classmethod
gekennzeichnet und erhalten cls (statt self) als ersten Parameter.

Damit können sie auf Klassendaten zugreifen oder alternative
Konstruktoren bereitstellen.

Typische Anwendungsfälle:
- Factory-Methoden
- Zugriff auf oder Veränderung von Klassenattributen
- Klassenspezifische Initialisierungen

Aufruf: über die Klasse oder eine Instanz möglich (Klasse.methode()).
"""
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    @classmethod
    def from_string(cls, daten_string):
        """
        Fabrik-Methode um neues Objekt aus String zu erstellen. 
        cls ist die Referenz auf die Klasse.
        """
        teile = daten_string.split(";")
        name, age = teile
        return cls(name=name, age=age)
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age!r})"


namen = ["Max;43", "Peter;23"]
personen_string = namen.pop()
print(personen_string)

# Personenobjekt erstellen
personenobjekt = Person.from_string(personen_string)
print(personenobjekt)