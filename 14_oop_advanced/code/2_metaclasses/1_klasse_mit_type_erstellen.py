"""
Thema: Dynamisches Erzeugen von Klassen mit der Funktion type()

In Python ist alles ein Objekt – auch Klassen. Die Funktion type() kann
nicht nur den Typ eines Objekts zurückgeben, sondern auch **neue Klassen
dynamisch erzeugen**.

Aufbau:
type(classname, bases, dict)

- classname: Name der neuen Klasse als String
- bases: Tupel der Basisklassen (für Vererbung)
- dict: Dictionary mit Methoden und Attributen

Das ist besonders nützlich für:
- dynamische Klassenerzeugung (z. B. in Frameworks oder Metaprogrammierung)
- automatisiertes Erzeugen von Klassen zur Laufzeit
- tieferes Verständnis von Python als dynamische Sprache
"""
Animal = type("Animal", (), {"ears": 2, "dance": lambda self: print("is dancing")})

rabbit = Animal()
print(rabbit.ears)
rabbit.dance()