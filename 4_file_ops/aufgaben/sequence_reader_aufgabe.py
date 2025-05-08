"""
mittel

Aufgabe SEQUENCE READER

Der Sequence reader öffnet zwei Sequence-Dateien, die mit dem
Sequence-Generator erstellt wurden und vergleicht sie.

1. Prüfe, ob die Sequenzen die gleiche Länge haben. Ist das nicht der
Fall, soll das Programm nur ausgeben, dass die Sequenzen nicht gleich
lang sind.

2. Sind die Sequenzen gleich lang, zähle die Anzahl der Matches
an allen Positionen mit Hilfe einer Schleife und eines Vergleichs der
Zeichen an der aktuellen Position.

3. Berechne aus der Anzahl der Matches und der Länge der Sequenzen die prozentuale Sequenzidentität.

Vergleich zweier Sequenzen (strings)

AAA
AAB
**-

ident count: 2
identity: 66.6 %

"""
