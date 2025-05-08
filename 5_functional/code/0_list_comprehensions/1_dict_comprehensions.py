"""
Dict Comprehensions sind ähnlich wie List Comprehensions, aber sie
werden verwendet, um Dictionaries auf elegante und kompakte Weise zu
erstellen. Dabei werden Schlüssel-Wert-Paare direkt erzeugt.

Dieses Skript zeigt grundlegende Anwendungen von Dict Comprehensions.
"""

# Klassisches Erstellen eines Dictionaries mit einer Schleife
quadrate = {}
for i in range(6):
    quadrate[str(i)] = i**2
print(quadrate)


# Das gleiche Dictionary mit einer Dict Comprehension erzeugen
quadrate = {str(i): i**2 for i in range(6)}
print(quadrate)

# Dict Comprehension mit Bedingung: Nur ungerade Zahlen berücksichtigen


# Umkehrung eines Dictionaries: Schlüssel und Werte tauschen
original = {"a": 1, "b": 2, "c": 3}   # {1: "a", 2:"b", 3:"c"}
umgekehrt = {v:k for k, v in original.items()}
print(umgekehrt)


# Aufgabe: Erzeuge ein Dictionary aus einer Liste von Zahlen,
# wobei jede Zahl der Schlüssel ist und ihr Quadrat der Wert.
zahlen = [1, 2, 3, 4, 5]


# Aufgabe: Verdoppele alle Werte in einem gegebenen Dictionary
preise = {"Apfel": 1.0, "Banane": 0.5, "Kiwi": 1.5}
