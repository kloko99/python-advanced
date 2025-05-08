"""
Thema: __new__ – Kontrolle über Objekterzeugung in Python

Die Methode __new__(cls, ...) ist ein spezieller Konstruktor, der
verwendet wird, um eine neue Instanz einer Klasse zu erzeugen, bevor
__init__ aufgerufen wird.

Im Gegensatz zu __init__, das nur ein bereits erzeugtes Objekt
initialisiert, ist __new__ dafür zuständig, dieses Objekt überhaupt
erst zu erstellen.

Typische Einsatzgebiete für __new__:
- Erzeugung von Singleton-Objekten
- Veränderung oder Austausch der Instanz beim Erzeugen
- Unterklassen von Immutable-Typen (z. B. int, str, tuple), bei denen
  Änderungen nur beim Erzeugen möglich sind

__new__ wird seltener benötigt, ist aber zentral, wenn man tiefen
Einfluss auf die Objekterzeugung nehmen möchte.
"""
class Haus:
    def __new__(cls, *args, **kwargs):
        """Wird aufgerufen, wenn eine neue Instanz eines Hauses gebildert werden soll."""
        print("Haus Objekt wurde erstellt!")
        obj = super().__new__(cls)
        obj.x = 42
        obj.y = 43
        return obj
    
    def __init__(self, name):
        """Wird aufgerufen, NACHDEM das Objekt erstellt wurde."""
        self.name = name 
        

house = Haus("Bauernhaus")
print(type(house)) # <class '__main__.Haus'>

print(type(Haus))  # Wer hat das Haus-Objekt erstellt?


# Attribute, die in __new__ hinzugefügt wurden, ausgeben
print(house.x)  # 42