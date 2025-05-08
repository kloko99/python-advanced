"""
Wie man Kapselung nicht machen sollte in Python
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

    def set_name(self, name):
        """Validiert und prüft."""
        if len(name) >= 3:
            self.name = name
        else:
            raise ValueError("Ungültiger Name")
    
    def get_name(self):
        return self.name
    


bob = Person("Bob", 44)
bob.set_name("Bobby")
