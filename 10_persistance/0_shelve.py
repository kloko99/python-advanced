"""
Shelve: Daten persistent in einem dict-ähnlichen
Container speichern.
"""

import shelve
from pathlib import Path

DB_PATH = Path(__file__).parent / "example.db"

# Shelve-DB öffnen und Werte reinschreiben
with shelve.open(DB_PATH) as db:
    db["name"] = "Bob"
    db["fruits"] = [1, 2, 3, 4]

# Falls schon exisitert, wird alte example.db genommen ...
with shelve.open(DB_PATH) as db:
    db["neu"] = "neuer WErt"

print("Objekte aus shelve wieder auslesen...")

# Shelve-DB öffnen und die Items wie ein Dict auslesen.
with shelve.open(DB_PATH) as db:
    print(list(db.items()))
    print(db["name"])  # b
    print(db["fruits"])
    print(db["neu"])
