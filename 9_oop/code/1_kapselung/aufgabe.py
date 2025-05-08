""" 
Erstelle eine Klasse Rechteck mit den Attributen breite und hoehe.
Die Klasse benötigt eine Methode area, die die Fläche ausrechnet und zurückgibt.

breite darf nicht < 0 sein: ValueError
hoehe darf nicht < 0 sein: ValueError

r1 = Rechteck(breite=10, hoehe=13)
r1.hoehe = 3
print(r1.area()) # 30

r1.hoehe = -12 # ValueError
r2 = Rechteck(breite=10, hoehe=-1)
ValueError!

__str__
__repr__
"""