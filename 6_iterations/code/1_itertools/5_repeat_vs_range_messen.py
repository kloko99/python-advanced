"""
Dieses Skript behandelt `itertools.repeat()` – eine Funktion, die ein
beliebiges Element speichereffizient und mehrfach liefert.

`repeat(obj, n)` erzeugt einen Iterator, der `obj` exakt `n`-mal
liefert. Wird `n` weggelassen, läuft der Iterator unendlich lange.

Typische Einsatzszenarien:
- Initialisierung gleichartiger Werte
- Dummy-Iteration in Loops (als Alternative zu range)
- Kombination mit `map()` oder `zip()` für wiederholte Argumente

Da `repeat` rein in C implementiert ist, ist es oft deutlich schneller
als `range()` – besonders bei sehr großen Wiederholungen, bei denen kein
zählerischer Zugriff nötig ist.

Im folgenden Beispiel vergleichen wir die Ausführungszeit von `range()`
und `repeat()` bei einer Dummy-Iteration.
"""

import itertools as it
import timeit


def create_range(n):
    # Dummy-Schleife mit range
    for _ in range(n):
        ...


def create_repeat(n):
    # Dummy-Schleife mit repeat
    for _ in it.repeat(None, n):
        ...


N = 100_000

# Messen der Laufzeit mit range
result_range = timeit.timeit("create_range(N)", globals=globals(), number=1000)

# Messen der Laufzeit mit repeat
result_repeat = timeit.timeit("create_repeat(N)", globals=globals(), number=1000)

print(f"Zeit mit range():  {result_range:.4f} Sekunden")
print(f"Zeit mit repeat(): {result_repeat:.4f} Sekunden")
