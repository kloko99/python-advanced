"""
Das Thema dieser Datei ist das Erstellen und Verwenden eigener Module in Python.

- Ein Modul ist eine Datei, die Python-Code enthält (z. B. Funktionen, Klassen).
- Eigene Module helfen dabei, Code besser zu organisieren und wiederzuverwenden.
- Module werden mit `import` in anderen Python-Dateien verwendet.
"""

# Schritt 1: Ein eigenes Modul erstellen
# -------------------------------------
# Erstelle eine neue Datei namens `mymodule.py` mit folgendem Inhalt:
#
# def greet(name):
#     """Gibt eine Begrüßung für den angegebenen Namen aus."""
#     return f"Hello, {name}!"
#
# def add(a, b):
#     """Addiert zwei Zahlen."""
#     return a + b
# -------------------------------------

# Schritt 2: Ein Modul importieren
# -------------------------------------
# Importiere das erstellte Modul und verwende die Funktionen.

# Beispielaufrufe der Funktionen aus `mymodule`

# Aufgabe:
# 1. Erstelle weitere Funktionen in `mymodule`, z. B. für Subtraktion oder Multiplikation.
# 2. Importiere und teste sie in dieser Datei.

# Schritt 3: Verwendung von Aliasen beim Import
# -------------------------------------
# Module oder Funktionen können mit Aliasen importiert werden.

# Beispielaufrufe mit Aliasen

# Schritt 4: Verwendung von `__name__ == "__main__"`
# -------------------------------------
# Um ein Modul sowohl als eigenständiges Skript als auch
# als importierbares Modul zu nutzen, kann man folgendes verwenden:
#
# if __name__ == "__main__":
#     # Dieser Code wird nur ausgeführt, wenn die Datei direkt aufgerufen wird
#     print("Das Modul wurde direkt ausgeführt.")
# -------------------------------------

# Schritt 5: Organisation von Modulen in Paketen
# -------------------------------------
# Ein Paket ist ein Verzeichnis, das mehrere Module enthält.
# Es muss eine Datei namens `__init__.py` enthalten, um als Paket erkannt zu werden.
# Beispielstruktur:
#
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
#
# Aufgabe:
# 1. Erstelle ein Paket namens `mypackage` mit mindestens zwei Modulen.
# 2. Importiere und verwende Funktionen aus diesen Modulen.
