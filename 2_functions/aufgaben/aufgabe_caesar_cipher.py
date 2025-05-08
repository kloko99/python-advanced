"""
Erstelle Caesar Cipher Verschlüsselung mit positiver sowie negativer Rotation
im ASCII-Alphabet (a-z A-Z)
https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung
https://en.wikipedia.org/wiki/Caesar_cipher

1) Implementiere die beiden Funktionen MITTEL
encrypt(word: str, rot: int): Verschlüsselt einen String
decrypt(word: str, rot: int): Entschlüsselt einen String
Gegeben ist das Alphabet. Wir gehen von legalem Input aus (ASCII-Zeichen)

Zeichen, die sich nicht im Alphabet befinden, sollen ignoriert und nicht
verschlüsselt werden, zum Beispiel Steuerzeichen wie newline oder Umlaute.
Damit ist die vorliegene Verschlüsselung nicht symmetrisch!

ZUSATZAUFGABEN SCHWER
2) Verschlüssele die Datei gregor_samsa.txt mit Roationsindex 3 und gebe das
Ergebnis auf der Standard-Ausgabe aus.

3) Lagere die Funktionen decrypt und encrypt in das Modul caesar_encryption
   aus und importiere die Funktionen aus diesem Modul.

4) Führe eine Frequenzanalyse (char count) für far_far_away.txt aus.
Kann man von der Zeichenfrequenz dieser Datei auf die Rotation, 
die bei der Verschlüsselung von gregor_samsa.txt (aus 2) verwendet wurde, schließen?
Führe dazu auch eine Frequenzanalyse des verschlüsselten gregor_samsa-Textes aus 2)
aus.

Plotte die 10 häufigsten Vorkommen in beiden Analysen als Bar-Plot.
https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm

"""
import string
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
from typing import Final

BASE_DIR: Final = Path(__file__).parent

# Alphabet is the complete printable ASCII Space
ALPHABET: Final = string.printable[:95]
LEN: Final = len(ALPHABET)
ROTATION: Final = 3


def encrypt(word: str, rot: int = 5) -> str:
    """Encrypt a string using Ceasars Cipher with given rotation."""


def decrypt(word: str, rot: int = 5) -> str:
    """Decrypt a string using Ceasars Chiper with given rotation."""


def tests():
    """These tests must pass young padawan ..."""
    assert encrypt("a", 1) == "b"
    assert encrypt("a", LEN) == "a"
    assert encrypt("}", rot=1) == "~"
    assert encrypt("}", rot=2) == " "
    assert encrypt("}", rot=3) == "0"
    assert decrypt("0", rot=3) == "}"
    assert encrypt("abc", rot=-1) == "9ab"
    assert encrypt("Solaris 3", rot=-21) == "x30[6}7,:"
    assert decrypt("x30[6}7,:", rot=-21) == "Solaris 3"
    assert encrypt("affe sieht rot", rot=99) == "ejji3wmilx3vsx"
    assert encrypt("^_`{|}~", rot=3) == "{|}~ 01"
    assert decrypt(word=encrypt("0fayz~ ", rot=3), rot=3) == "0fayz~ "
    print("all tests run successfully")


def main():
    tests()
    # print(encrypt("Zen", rot=1))
    # print(decrypt(encrypt("zen", 12), 12))
    pass


if __name__ == "__main__":
    main()
