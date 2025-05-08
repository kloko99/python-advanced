import random

"""
mittel

Aufgabe SEQUENCE GENERATOR
Erzeuge eine Sequenzvariable und schreibe die Testsequenz in eine Datei.
(Falls pickle im Unterricht besprochen wurde, nutze Pickle)
Die Sequenz soll zufällig erstellt werden.

Der User kann über input eingeben:
    die Länge der Sequence, die generiert werden soll (int)
    der Zeichenvorrat, der verwendet werden soll. Z.b. ABC. Werte sind unique.
    der Name der Sequence.

Beispiel:
Sequenz-Länge: 5
Zeichenvorrat: ABO
Name der Sequence: ABO5

Ergebnis: AABAO
die datei ABO5 enthält jetzt die Zeichenkette AABAO
Die Sequence soll in eine Datei geschrieben werden.
"""
# Beispiel: random.choice zieht aus einer Menge ein Element (mit zurücklegen)
random.choice(["a", "b", "c"])
