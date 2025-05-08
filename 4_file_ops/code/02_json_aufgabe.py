"""
Praktische Aufgabe: Arbeiten mit JSON-Dateien (Geographie)

Aufgabe:
Erstelle eine JSON-Datei mit dem Namen "geographie.json" und folgendem Inhalt:

--- Inhalt von geographie.json ---
[
    {
        "stadt": "Berlin",
        "land": "Deutschland",
        "einwohner": 3769000
    },
    {
        "stadt": "Paris",
        "land": "Frankreich",
        "einwohner": 2148000
    },
    {
        "stadt": "München",
        "land": "Deutschland",
        "einwohner": 1472000
    },
    {
        "stadt": "Madrid",
        "land": "Spanien",
        "einwohner": 3223000
    }
]
--- Ende ---

Schreibe ein Python-Programm, das die Datei "geographie.json" einliest
und alle Städte aus einem bestimmten Land (z.B. "Deutschland") filtert.
Die gefilterten Daten sollen in eine neue Datei "gefiltert.json" gespeichert werden.

Bonus:
- Gib die Gesamtanzahl der gefilterten Städte aus.
- Berechne die Gesamtanzahl der Einwohner der gefilterten Städte.
"""

# Lösungsvorschlag

import json
from pathlib import Path

# Land, nach dem gefiltert werden soll
filter_land = "Deutschland"

file_path_in = Path(__file__).parent / "geographie.json"
file_path_out = Path(__file__).parent / "gefiltert.json"
