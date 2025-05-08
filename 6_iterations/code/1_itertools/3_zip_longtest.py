"""
`zip_longest()` gehört zum Modul `itertools` und erlaubt das Verknüpfen
zweier oder mehrerer Iterables bis zur Länge des längsten Iterables.
Fehlende Werte werden dabei mit einem Platzhalter (`fillvalue`) ergänzt,
standardmäßig `None`.

Im Gegensatz zu `zip()`, das beim kürzesten Iterable stoppt, bleibt bei
`zip_longest()` alles erhalten – nützlich z. B. bei Datenabgleichen
unterschiedlicher Länge (z. B. CSV-Spalten, Schüler-Listen, Log-Zeilen).
"""

import itertools as it

students = ["Paul", "Peter", "Maria", "Klaus", "Mohammad", "Sibi"]
notes = [3, 1, 2, 5, 1]

# zip(): Nur so viele Paare wie das kürzeste Iterable erlaubt
print("zip:", list(zip(students, notes)))
# [('Paul', 3), ('Peter', 1), ('Maria', 2), ('Klaus', 5), ('Mohammad', 1)]


# zip_longest(): Ergänzt fehlende Werte mit None (oder anderem Wert)
print("zip_longest:", list(it.zip_longest(students, notes)))
# [('Paul', 3), ('Peter', 1), ('Maria', 2), ('Klaus', 5), ('Mohammad', 1), ('Sibi', None)]

# Optional: mit eigenem Platzhalter
print(
    "zip_longest (mit Ersatzwert):",
    list(it.zip_longest(students, notes, fillvalue="kein Wert")),
)
# [('Paul', 3), ..., ('Sibi', 'kein Wert')]

