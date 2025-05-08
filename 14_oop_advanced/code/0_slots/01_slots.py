"""
Thema: __slots__ – Speicher sparen bei vielen Instanzen

Mit dem Attribut __slots__ kann man in Klassen festlegen, welche
Attribute erlaubt sind. Dadurch wird verhindert, dass ein dynamisches
__dict__ für jedes Objekt angelegt wird – was Speicher spart.

Vorteile:
- Weniger Speicherverbrauch bei vielen Instanzen
- Schnellere Attributzuweisungen (leicht messbar)
- Kann unbeabsichtigte Attribut-Erweiterungen verhindern

Einschränkungen:
- Kein __dict__ → keine dynamische Erweiterung zur Laufzeit
- Kein __weakref__ (außer explizit angegeben)

__slots__ ist sinnvoll bei großen Datenklassen oder vielen Objekten,
z.B. in Simulationen, Parsern, oder bei numerischen Datenmodellen.
"""
class Robot:
    def __init__(self, name, serialnumber):
        self.name = name 
        self.serialnumber = serialnumber 


r2d2 = Robot("R2D2", 23749823798)
r2d2.age = 3
print(r2d2.__dict__)
print(vars(r2d2))


class Human:
    """Nutzt Slots, um zu verhindern, dass weitere Attribute 
    zur Laufzeit hinzugefügt werden können."""

    __slots__ = ("name", "age")  # klasse hat nur diese Attribute

    def __init__(self, name, age):
        self.name = name 
        self.age = age


class Player(Human):
    """Erbt von Human, hat aber keine Slots."""

    def __init__(self, name, age, player_id):
        super().__init__(name, age)
        self.player_id = player_id


bob = Human("Bob", 3)
# bob.nickname = "Bobby"    ERROR
# print(vars(bob))          ERROR
print(bob.__slots__)        # (name, age)

alice = Player("Alice", 34, "ID 232343")
print(alice.__slots__)      # (name, age)
print(alice.__dict__)       # {'player_id': 'ID 232343'}