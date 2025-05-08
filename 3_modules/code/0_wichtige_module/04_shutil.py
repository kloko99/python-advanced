"""
Das Thema dieser Datei ist das `shutil`-Modul in Python.

- Das `shutil`-Modul bietet Funktionen zum Kopieren, Verschieben und Löschen
  von Dateien und Verzeichnissen sowie zum Arbeiten mit Archiven.
- Es wird häufig für Aufgaben im Zusammenhang mit der Dateiverwaltung verwendet.
"""

import shutil
from pathlib import Path

# --- Datei kopieren ---
source_file = Path(__file__).parent / "source.txt"
destination_file = Path(__file__).parent / "destination.txt"

source_dir = Path(__file__).parent / "data"
destination_dir = Path(__file__).parent / "backup"


# Datei im gleichen Verzeichnis kopieren

# --- Verzeichnis kopieren ---

# Prüfen, ob das Zielverzeichnis bereits existiert und ggf. löschen

# Verzeichnis kopieren

# 6. Disk- und Speicherplatzinformationen

# 5. Arbeiten mit Archiven
#

# Entpacken eines Archivs
