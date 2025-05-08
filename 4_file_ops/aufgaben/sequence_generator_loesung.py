"""
Aufgabe SEQUENCE GENERATOR
Erzeugen Sie eine Sequenzvariable und schreiben Sie ihre Testsequen-
z in eine Datei. Nutzen Sie dazu das pickle-Modul.
Die Sequenz soll zufällig erstellt werden.

Der User kann über input eingeben:
    die Länge der Sequence, die generiert werden soll (int)
    der Zeichenvorrat, der verwendet werden soll. Z.b. ABC. Werte sind unique.
    der Name der Sequence. Dieser Name ist der Filename der Pickle Datei
    Die Datei hat keinen Dateisuffix


Beispiel:
Sequenz-Länge: 5
Zeichenvorrat: ABO
Name der Sequence: ABO5

Ergebnis: AABAO
die datei ABO5 enthält jetzt die Zeichenkette AABAO
"""
from pathlib import Path
import random
import pickle
import bz2

BASE_DIR = Path(__file__).resolve().parent

sequence_length = int(input("Enter length of sequence (e.g. 4): "))
chars = list(set(input("Enter valid chars (e.g. AB0): ")))
sequence_name = input("Enter name of Sequence: ")

# create sequence
sequence = "".join([random.choice(chars) for _ in range(sequence_length)])

# save that stuff
with open(BASE_DIR / sequence_name, "wb") as f:
    pickled = pickle.dumps(sequence)
    f.write(bz2.compress(pickled))

print(f"file successfully written to disc: {sequence_name}")
with open(BASE_DIR / sequence_name, "rb") as f:
    data = f.read()
    data = pickle.loads(bz2.decompress(data))
    print(data)
