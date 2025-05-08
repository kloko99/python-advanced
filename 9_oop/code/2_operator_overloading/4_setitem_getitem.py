"""
Thema: __getitem__ und __setitem__ – Zugriff wie bei Listen und Dictionaries

Mit den Methoden __getitem__(self, key) und __setitem__(self, key, value)
kann man eigenen Klassen das Verhalten von Index- oder Schlüsselzugriff
verleihen – ähnlich wie bei Listen oder Dictionaries.

Damit lässt sich z. B. obj[key] lesen oder schreiben, anstatt Methoden
wie get(key) oder set(key, value) zu verwenden.

Dieses Konzept wird häufig in containerartigen Klassen, Datenstrukturen
und internen APIs verwendet.

d["x"] = 3  # schreibend
d["x"]       # lesend
"""
class Building:
    """eine einfache Gebäudeklasse mit Stockwerken."""
    def __init__(self, floors: int):
        self._floors = [None] * floors

    def __setitem__(self, floor_number: int, floor_name: str):
        """Ein Stockwerk mit einem Namen belegen."""
        if floor_number > len(self._floors) - 1:
            raise ValueError("Dieses Stockwerk gibt es nicht!")
        
        self._floors[floor_number] = floor_name
    
    def __getitem__(self, floor_number: int):
        return self._floors[floor_number]


rockefeller_center = Building(floors=4)
rockefeller_center[0] = "Reception"  # __setitem__ wird aufgerufen
rockefeller_center[1] = "Office"     # __setitem__ wird aufgerufen
rockefeller_center[2] = "Office"     # __setitem__ wird aufgerufen
rockefeller_center[3] = "Office"     # __setitem__ wird aufgerufen
# rockefeller_center[4] = "Pent House"  #  Error! 5 STock (Index 4) gibts nicht
print(rockefeller_center[1])

