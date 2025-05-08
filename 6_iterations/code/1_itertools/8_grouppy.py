"""
`groupby(iterable, key=None)` gruppiert aufeinanderfolgende Elemente eines
Iterables anhand eines Schlüssels. Die Gruppenbildung erfolgt nur für
aufeinanderfolgende Elemente mit demselben Schlüssel, daher sollte das
Iterable vorher nach dem Gruppierungskriterium sortiert werden.

Wichtig:
- Der Iterator liefert Paare (key, group), wobei `group` selbst ein Iterator ist.
- Die Gruppierung erfolgt nur für **aufeinanderfolgende gleiche Schlüssel**.

Typische Anwendungen:
- Gruppierung nach Kategorien oder Zuständen
- Zählen oder Aggregieren von Daten
- Verarbeitung von bereits vorsortierten Streams

`groupby()` ist speichereffizient und ideal für große sortierte Datenmengen.

Dieses Skript zeigt einfache und realistische Beispiele mit Zahlen und
Dictionaries.
"""

import itertools as it

# Beispiel 1: Gruppieren von direkt aufeinanderfolgenden Zahlen
grouped_numbers = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 1]
number_groups = it.groupby(grouped_numbers)
print("Gruppierte Zahlen:")
for key, group in number_groups:
    print(key, list(group))


# Beispiel 2: Real-World – Studenten nach Alter gruppieren
students = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 39},
    {"name": "Charlie", "age": 30},
]

# Sortierung nach Gruppierungskriterium erforderlich
students = sorted(students, key=lambda d: d["age"])

print("Studenten nach Alter gruppiert:")
result = it.groupby(students, key=lambda e: e["age"])
for age, group in result:
    print(age, list(group))


# Beispiel 3: Gruppieren von unendlicher Sequenz nach Modulo 3
def group_by(n):
    return n % 3


# Achtung: Ergebnis ist unendlich – nur erste 3 Gruppen zeigen
print("Modulo-Gruppen aus it.count():")
result = it.groupby(it.count(), key=group_by)
for _, group in zip(range(3), result):
    print(_, list(it.islice(group[1], 5)))
