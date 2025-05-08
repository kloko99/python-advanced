"""
Aufgabe SEQUENCE READER

Der Sequence reader öffnet zwei Pickle-Sequence-Dateien, die mit dem
Sequence-Generator erstellt wurden und vergleicht sie.

1. Prüfen Sie, ob die Sequenzen die gleiche Länge haben. Ist das nicht der
Fall, soll das Programm nur ausgeben, dass die Sequenzen nicht gleich
lang sind.

2. Sind die Sequenzen gleich lang, zählen Sie die Anzahl der Matches
an allen Positionen mit Hilfe einer Schleife und eines Vergleichs der
Zeichen an der aktuellen Position. Sind diese gleich, sollte eine Zähler-
variable um 1 erhöht werden.

3. Berechnen Sie aus der Anzahl der Matches und der Länge der Sequen-
zen die prozentuale Sequenzidentität.

Vergleich zweier Sequenzen (strings)

AAA
AAB
**-

ident count: 2
identity: 66.6 %

"""
from pathlib import Path
import pickle
import bz2


BASE_DIR = Path(__file__).resolve().parent
ident_count = 0
failed = True
error_msg = ""
sequences = []

# get filenames from user
sequence_name_1 = input("Enter name of first Sequence: ")
sequence_name_2 = input("Enter name of second Sequence: ")

# open files via pickle, transform to string and append to sequences list
for seq_name in [sequence_name_1, sequence_name_2]:
    if (BASE_DIR / seq_name).exists():
        with open(BASE_DIR / seq_name, "rb") as f:
            data = pickle.loads(bz2.decompress(f.read()))
            sequences.append(data)
    else:
        print("File missing...")


# unpack
sequence_1, sequence_2 = sequences

if len(sequence_1) != len(sequence_2):
    error_msg = "Sequencen haben nicht die gleiche Länge"

elif not len(sequence_1):
    error_msg = "Die Sequencen haben eine Länge von 0"

else:
    failed = False
    print(sequence_1)
    print(sequence_2)

    for i in range(len(sequence_1)):

        if sequence_1[i] == sequence_2[i]:
            ident_count += 1
            print("*", end='')
        else:
            print("_", end='')


# print Stats
if failed:
    print("Es sind Fehler aufgetreten: ")
    print(error_msg)
else:
    print("\nStats: ")
    print("ident_count:", ident_count)
    identity = (ident_count / len(sequence_1))
    print(f"identity: {identity:0.1%}")
