"""
Dieses Modul zeigt die Verwendung von Pattern Matching (ab Python 3.10)
mit verschiedenen **Datentypen** wie `int`, `str`, `bool`, `list`, `dict`
und benutzerdefinierten Objekten.

Pattern Matching ermöglicht es, Datenstrukturen direkt anhand ihres
Typs und Aufbaus zu prüfen – eleganter als viele `if isinstance(...)`-Konstrukte.

Dieses Modul demonstriert:
- Typbasiertes Matching von primitiven Datentypen
- Listen und Dictionaries mit konkreter Struktur
- Kombination mit Guards
- Erste Idee für eigene Klassen (dataclass)
"""

# ---------------------------------------------
# Beispiel 1: primitive Typen erkennen
# ---------------------------------------------


def beschreibe_wert(wert):
    """
    Beschreibt den Typ des Wertes.
    """


beschreibe_wert(42)  # Das ist eine Ganzzahl
beschreibe_wert(3.14)  # Das ist eine Fließkommazahl
beschreibe_wert("Hallo")
beschreibe_wert(True)

# ---------------------------------------------
# Beispiel 2: Listen- und Dictionary-Strukturen
# ---------------------------------------------


def analysiere(eingabe):
    # 1) prüfe auf Listen mit zwei Elementen mit Int
    # 2) prüfe auf Dict mit zwei Keys name und age
    pass


analysiere([3, 7])
analysiere({"name": "Alice", "age": 30})
analysiere({"name": 3, "age": "30"})
analysiere("Test")

# ---------------------------------------------
# Beispiel 3: Kombination mit Guards
# ---------------------------------------------


def prüfe(wert):
    pass


prüfe(150)
prüfe("Anna")
prüfe("Bob")
