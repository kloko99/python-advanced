"""
Die Funktion `filter()` in Python wird verwendet, um Elemente aus einem
iterierbaren Objekt zu filtern, basierend auf einer Funktion, die
wahrheitswertige Rückgaben liefert.

Syntax: filter(funktion, iterable)

Dabei wird jedes Element des iterierbaren Objekts an die Funktion
übergeben. Nur jene Elemente, für die die Funktion `True` zurückgibt,
werden im Ergebnis enthalten sein.

Der Rückgabewert ist ein Iterator. Um die Ergebnisse zu sehen,
muss man ihn z. B. in eine Liste umwandeln.

Typische Einsatzgebiete:
- Herausfiltern ungerader/gerader Zahlen
- Entfernen leerer oder ungültiger Werte
- Prüfung auf Bedingungen in Datenreihen

Vergleich:
filter(predicate, seq) ist äquivalent zu:
[el for el in seq if predicate(el)]

Dieses Skript zeigt grundlegende und praxisnahe Anwendungen von `filter()`.
"""


# Funktion, die prüft, ob eine Zahl größer als 100 ist
def greater_then_100(x) -> bool:
    return x > 100


# Liste mit Zahlen
zahlen = [1, 111, 2, 222, 3, 333]

# Filtere alle Zahlen > 100 mit filter()
z = filter(greater_then_100, zahlen)
print(list(z)) # [111, 222, 333]


# als List comprehension
[el for el in zahlen if greater_then_100(el)]

# Funktion, die prüft, ob ein Wort länger als 5 Buchstaben ist
def check_length(s):
    return len(s) > 5


# Liste von Wörtern
words = ["apple", "banana", "kiwi", "strawberry", "pear"]

# als Filter-Funktion
filter(check_length, words)

