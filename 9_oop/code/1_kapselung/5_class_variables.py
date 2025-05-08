"""
Thema: Klassenvariablen in Python

Klassenvariablen sind Variablen, die auf Klassenebene definiert
werden und von allen Instanzen gemeinsam genutzt werden.

Im Gegensatz zu Instanzvariablen (self.var), die nur für ein
bestimmtes Objekt gelten, sind Klassenvariablen für **alle Objekte
der Klasse gleich** – sofern sie nicht auf Instanzebene überschrieben
werden.

Typischerweise werden sie verwendet für:
- Zähler über alle Instanzen
- Konstante Klasseneigenschaften
- Gemeinsame Konfigurationswerte

Klassenvariablen werden direkt in der Klasse definiert, nicht im
__init__-Konstruktor.

Diese Datei zeigt, wie Klassenvariablen definiert, verwendet und
überschrieben werden können.
"""
class Robot:
    # KLassenvariable
    population = 0
    default_speed = 100
    
    def __init__(self, name):
        self.name = name 
        Robot.population += 1
    
    def inspect(self):
        """Gebe den Namen der Klasse und die Attribute aus."""
        print("Klassenname=", self.__class__.__name__)


c3po = Robot(name="C3PO")
r2d2 = Robot(name="R2D2")

r2d2.population = 4  # ändert nicht die Klassenvariable population
print(vars(r2d2))
print(vars(c3po))
print("Anzahl Roboter:", Robot.population)
print("Anzahl Roboter:", r2d2.population)


# Klassenname Ausgeben
c3po.inspect()