"""
Aufgabe – Generator‑Funktion chunked(iterable, size)

Schreibe eine Funktion chunked(iterable, size), die mithilfe von
yield aufeinanderfolgende Teilstücke («Chunks») der Länge size liefert.
Der letzte Chunk darf kürzer sein, wenn die Elemente nicht aufgehen.

    >>> list(chunked("abcdefg", 3))
    ['abc', 'def', 'g']

Regeln:
    • Keine Listen in voller Länge anlegen – iteriere einmalig.
    • size > 0 voraussetzen, sonst ValueError werfen.
    • Nur Standard‑Bibliothek, kein itertools.chunked verwenden.
"""
