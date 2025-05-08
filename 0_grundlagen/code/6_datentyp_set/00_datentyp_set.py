"""
Einführung in den Datentyp `set` in Python

Ein Set (Menge) ist eine ungeordnete Sammlung von einzigartigen Elementen.
In Python wird der Datentyp `set` verwendet, um Mengen zu repräsentieren.
Er eignet sich besonders für Operationen wie Vereinigung, Schnittmenge oder
Unterschied.

Themenübersicht:
1. Erstellung und Eigenschaften von Sets
2. Hinzufügen und Entfernen von Elementen
3. Mengenoperationen: Vereinigung, Schnittmenge, Unterschied
4. Methoden und Anwendungen
"""

# 1. Erstellung und Eigenschaften von Sets
# Ein Set wird mit geschweiften Klammern `{}` oder der Funktion `set()` erstellt.
# Sets enthalten keine doppelten Elemente.

# Erstellung eines leeren Sets (Achtung: {} erzeugt ein leeres Dictionary)

# Automatische Entfernung doppelter Elemente

# 2. Hinzufügen und Entfernen von Elementen
# `add()`: Fügt ein Element hinzu.

# `remove()`: Entfernt ein Element (KeyError, wenn das Element nicht existiert).

# `discard()`: Entfernt ein Element (kein Fehler, wenn das Element nicht existiert).

# `pop()`: Entfernt ein zufälliges Element.

# `clear()`: Entfernt alle Elemente aus dem Set.

# 3. Mengenoperationen
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Vereinigung (`union()` oder `|`)

# Schnittmenge (`intersection()` oder `&`)

# Unterschied (`difference()` oder `-`)

# Symmetrische Differenz (`symmetric_difference()` oder `^`)

# 4. Methoden und Anwendungen
# `issubset()`: Prüft, ob ein Set eine Teilmenge eines anderen ist.

# `issuperset()`: Prüft, ob ein Set eine Obermenge eines anderen ist.

# `isdisjoint()`: Prüft, ob zwei Sets keine gemeinsamen Elemente haben.
