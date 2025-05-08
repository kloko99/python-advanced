"""
Das Thema dieser Datei ist die Arbeit mit Dateioperationen in Python.

- Python bietet zahlreiche Funktionen, um Dateien zu lesen, zu schreiben
  und zu manipulieren.
- Wir betrachten grundlegende Dateioperationen wie das Erstellen, Lesen,
  Schreiben und Löschen von Dateien.
"""

# 1. Datei erstellen und schreiben
from pathlib import Path

file_name = Path(__file__).parent / "example.txt"

# Schreiben in eine Datei (überschreibt den Inhalt, falls vorhanden)

# 2. Datei lesen
# Lesen des gesamten Inhalts

# Zeilenweise lesen

# Aufgabe:
# Implementiere eine Funktion, die die Datei oceans.txt zeilenweise liest und
# dabei jede Zeile nummeriert ausgibt. Starte die Nummerierung bei 1.
oceans_file = ...

# 3. Datei anhängen
# Hinzufügen neuer Inhalte


# 4. Datei manipulieren
# Umbenennen der Datei
new_file_name = "renamed_example.txt"

# 5. Datei löschen
# Löschen der Datei


# 6. Prüfung von Dateien
# Überprüfen, ob eine Datei existiert
