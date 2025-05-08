"""
Das Thema dieser Datei ist die Verwendung des `shelve`-Moduls in Python.

- `shelve` ist ein Modul der Python-Standardbibliothek, das einfache
  persistente Speicherlösungen bietet.
- Es ermöglicht das Speichern von Python-Objekten in einer Datei
  mithilfe eines Dictionary-ähnlichen Interfaces.
- Die gespeicherten Daten werden automatisch serialisiert.
- Keys dürfen nur Strings sein, während die Werte beliebige Python-Objekte
  sein können.

Die gespeicherten Daten werden intern von einem Datenbankmodul (wie dbm)
verwaltet. Dadurch entstehen beim Speichern mehrere Dateien

Die Daten liegen nach Speicherung in drei Dateien vor:
- basename.db: Enthält die Daten.
- basename.dat: Enthält die serialisierten Daten.
- basename.bak: Enthält eine Sicherungskopie der Datenbank.
- basename.dir: Enthält die Indexdatei.

Je nach Betriebssystem und DBM-Backend können auch weniger oder andere Dateien
entstehen. Beispielsweise erzeugt dbm.dumb nur .dat und .dir.

Aufgrund dieser Tatsache ist shelve nicht platformunabhängig und sollte
nur genutzt werden, wenn die Datenbankdateien auf dem gleichen System
genutzt werden.

Alternativen zu `shelve` sind:
- pickle: Einfaches Modul zum Serialisieren von Python-Objekten.
- json: Modul zum Serialisieren von Python-Objekten in JSON-Dateien.
"""

import shelve
from pathlib import Path

# 1. Einführung in das `shelve`-Modul
# Das `shelve`-Modul speichert Python-Objekte wie Strings, Listen,
# Dictionaries und mehr.
db_path = Path(__file__).parent / "my_shelve.db"

# Beispiel-Daten
data = {
    "name": "Anna",
    "age": 30,
    "languages": ["Deutsch", "Englisch"],
    "is_employed": True,
}

# 2. Schreiben von Daten in ein Shelve

# 3. Lesen von Daten aus einem Shelve


# 4. Aktualisieren von Daten in einem Shelve


# 5. Daten löschen


# 6. Shelve auslesen

# 7. Aufräumen
# Entfernen der Shelve-Datei
