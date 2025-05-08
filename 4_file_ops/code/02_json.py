"""
Das Thema dieser Datei ist das Schreiben und Lesen von JSON-Daten in Python.

- JSON (JavaScript Object Notation) ist ein leichtgewichtiges Datenformat,
  das häufig für den Datenaustausch verwendet wird.
- Python bietet das Modul `json`, um JSON-Daten zu verarbeiten.
- In diesem Dokument behandeln wir grundlegende Operationen wie das Schreiben,
  Lesen und Verarbeiten von JSON-Daten.
"""

import json
from pathlib import Path

# 1. Einführung in JSON
# JSON-Daten bestehen aus Schlüssel-Wert-Paaren, ähnlich wie Python-Dictionaries.
data = {
    "name": "Anna",
    "age": 30,
    "languages": ["Deutsch", "Englisch"],
    "is_employed": True,
}

# 2. Schreiben von JSON-Daten in eine Datei
file_path = Path(__file__).parent / "data.json"

# JSON-Daten in eine Datei schreiben
#
#
# 3. Lesen von JSON-Daten aus einer Datei
# JSON-Daten aus einer Datei lesen

# 4. Verarbeitung von JSON-Daten
# Zugriff auf JSON-Daten

# 6. Umgang mit Fehlern beim JSON-Parsen
# Ungültiges JSON (zusätzliches Komma)
invalid_json = '{"name": "Anna", "age": 30, }'
