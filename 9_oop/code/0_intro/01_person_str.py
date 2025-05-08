"""
Thema: __str__ und __repr__ in Python (Dunder-Methoden)

In Python gibt es spezielle Methoden, die mit doppelten Unterstrichen
beginnen und enden – sogenannte "dunder"-Methoden. Zwei wichtige davon
sind:

- __str__(self): Wird aufgerufen, wenn ein Objekt in einen String
  umgewandelt oder mit print() ausgegeben wird. Ziel: leserliche
  Darstellung für den Benutzer.

- __repr__(self): Wird aufgerufen, wenn die "repr()" Funktion genutzt
  wird oder ein Objekt in einer interaktiven Konsole angezeigt wird.
  Ziel: eine eindeutige, oft technische Darstellung, die im Idealfall
  wieder zu demselben Objekt führt (eval(repr(obj))).

Diese Datei zeigt den Unterschied beider Methoden mit praktischen
Beispielen.
"""
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def __str__(self) -> str:
        """Userfreundliche Darstellung eines Objekts.  Dunder STring"""
        return self.name + "-" + str(self.age)
    
    def __repr__(self) -> str:
        """Eher für interne, Debugging-Zwecke gedachte Repräsentation."""
        return f"Person(name={self.name!r}, age={self.age!r})"


bob = Person(name="Bob", age=23)
alice = Person(name="Alice", age=324)
print(bob)  # Bob


persons = [bob, alice]   # Liste ausdrucken ruft intern __repr__ für jedes Objekt aufgerufen
print(persons)