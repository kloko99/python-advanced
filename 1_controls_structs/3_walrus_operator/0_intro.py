"""
Dieses Modul gibt eine Einführung in den sogenannten "Walrus Operator"
(:=), der mit Python 3.8 eingeführt wurde.

Er erlaubt es, einer Variablen **während** eines Ausdrucks einen Wert
zuzuweisen. Das reduziert doppelte Berechnungen und erlaubt kompaktere,
aber weiterhin lesbare Code-Konstruktionen.

Syntax:
    variable := Ausdruck

Typische Anwendungen:
- While-Schleifen mit Input oder IO
- Bedingungen, die gleichzeitig speichern und prüfen
- List Comprehensions mit Bedingungsspeicherung

Hinweis: Der Operator hat seine Grenzen und sollte nur dort verwendet
werden, wo er wirklich Klarheit schafft.

Hinweis: Der Walrus-Operator (:=) hat eine geringere Priorität als viele
andere Operatoren – daher sollte er in komplexeren Ausdrücken immer in
Klammern gesetzt werden, um unerwartetes Verhalten zu vermeiden.
"""

import re

# ---------------------------------------------
# Beispiel 1: klassische while-Schleife mit input()
# ---------------------------------------------


# ---------------------------------------------
# Beispiel 2: Zwischenspeichern im If-Ausdruck
# ---------------------------------------------


def pruefe_email(email: str):
    """Prüfe, ob die E-Mail-Adresse gültig ist.

    Hinweis:
    Einfache Prüfung auf das Vorhandensein von '@' und '.'.
    """
    pass


pruefe_email("user@example.com")
pruefe_email("keine.email")

# ---------------------------------------------
# Beispiel 3: List Comprehension mit Bedingungsergebnis
# ---------------------------------------------
werte = ["Apfel", "Banane", "Kiwi", ""]

# ---------------------------------------------
# Beispiel 4: mehrfach verwendetes Ergebnis vermeiden
# ---------------------------------------------


def quadrat_und_vergleich(x):
    """Vergleiche das Quadrat von x mit 100 und gib das Ergebnis aus."""
    pass


quadrat_und_vergleich(5)
quadrat_und_vergleich(11)

# ---------------------------------------------
# Beispiel 5: Stream-Verarbeitung mit Limit
# ---------------------------------------------


def lese_zeilen(dateipfad):
    """Lese Zeilen aus einer Datei und gebe sie aus."""
    pass


# lese_zeilen("beispiel.txt")  # Datei nötig


# ---------------------------------------------
# Beispiel 6: Iterator-Zwischenspeicherung
# ---------------------------------------------
iterator = iter([1, 2, 3, 4, 5])


# ---------------------------------------------
# Negativbeispiel 1: unnötig verschachtelt
# ---------------------------------------------
# Schlechter Stil: reduziert Lesbarkeit deutlich
def negativ1():
    if (x := len((temp := input("Wert: ")))) > 3:
        print(f"'{temp}' ist zu lang mit Länge {x}")


negativ1()
