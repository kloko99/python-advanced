"""
Dieses Skript demonstriert den Einsatz von drei verwandten Funktionen aus dem
Modul `itertools`: `dropwhile()`, `takewhile()` und `filterfalse()`.

Alle drei Funktionen erwarten eine Prüffunktion und ein Iterable.
Sie verhalten sich aber unterschiedlich in ihrer Anwendung:

- `dropwhile(predicate, iterable)` überspringt so lange Elemente,
  wie die Bedingung `True` ergibt. Sobald sie einmal `False` ist,
  werden alle weiteren Elemente ohne Prüfung zurückgegeben.

- `takewhile(predicate, iterable)` liefert so lange Elemente,
  wie die Bedingung `True` ergibt. Danach wird die Iteration beendet,
  auch wenn danach wieder passende Elemente folgen würden.

- `filterfalse(predicate, iterable)` ist das Gegenteil von `filter()`.
  Sie liefert alle Elemente, für die die Bedingung `False` ergibt.

Die Funktionen sind speichereffizient und ideal für Streaming oder
große Datenmengen.
"""

import itertools as it


def f(x):
    """Prüffunktion: Gibt True zurück, wenn ein Element ein
    Kleinbuchstabe ist."""
    return isinstance(x, str) and x.islower()


iterable = "abcdefgHIJKLMnopQRStuvWXYz"

print(iterable)
# dropwhile(): Entfernt Anfangswerte solange f True ergibt
print("dropwhile:", list(it.dropwhile(f, iterable)))

# takewhile(): Nimmt Anfangswerte solange f True ergibt
print("takewhile:", list(it.takewhile(f, iterable)))

# filterfalse(): Nimmt nur Elemente, bei denen f False ist
print("filterfalse:", list(it.filterfalse(f, iterable)))

# Vergleich mit List Comprehension
print("list-compr:", [x for x in iterable if not f(x)])

