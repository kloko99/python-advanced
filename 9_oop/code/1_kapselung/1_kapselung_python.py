"""
Thema: Kapselung in Python mit @property

In Python wird Kapselung nicht über strikte Zugriffsmodifikatoren
(gibt es nicht wie in Java), sondern über Konventionen und das
@property-Decorator realisiert.

Mit @property kann man Methoden wie Attribute verwenden. Damit ist
es möglich, den Zugriff auf interne Variablen zu kontrollieren,
ohne die äußere Schnittstelle zu verändern.

Typisches Anwendungsbeispiel:
- Private Variable _name (non-public)
- Getter mit @property
- Setter mit @<name>.setter

So lässt sich Logik beim Lesen und Schreiben von Attributen
unterbringen, ohne dass der Benutzer eine Methode aufrufen muss.
"""
class Person:
    def __init__(self, name, age):
        self.name = name # self.name(name)
        self.age = age
    
    def __str__(self) -> str:
        """Userfreundliche Darstellung eines Objekts.  Dunder STring"""
        return self.name + "-" + str(self.age)
    
    def __repr__(self) -> str:
        """Eher für interne, Debugging-Zwecke gedachte Repräsentation."""
        return f"Person(name={self.name!r}, age={self.age!r})"
    
    @property
    def name(self):
        """Getter von Name"""
        return self._name 
    
    @name.setter
    def name(self, name):
        """Setter von name."""
        if len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name ist zu kurz")


bob = Person("Bob", 44)
bob.age = 32  # offizielle API für Zugriff auf Attribute
print(bob.age)  # Getter Zugriff
bob.name = "Bob"
