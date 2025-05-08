"""
Dieses Skript demonstriert die Nutzung von `itertools.combinations()`.

`combinations(iterable, r)` erzeugt alle möglichen Kombinationen der Länge `r`
aus dem gegebenen `iterable`, wobei die Reihenfolge der Elemente keine Rolle
spielt und jedes Element höchstens einmal verwendet wird.

Das ist nützlich für Wahrscheinlichkeitsrechnungen, Optimierungsprobleme und
die Simulation realer Szenarien wie Kartenspiele, Geldwechsel oder Inventar-
kombinationen.

Die Funktion ist Teil des in C implementierten `itertools`-Moduls und eignet
sich besonders bei speichereffizienter Verarbeitung großer Kombinationsräume.
"""

import itertools as it

# -------------------------------------------
# Beispiel 1: Wie viele Möglichkeiten gibt es, 100 Dollar zu bilden?
# -------------------------------------------
# Verfügbare Geldscheine
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

# Suche alle Kombinationen beliebiger Länge, die genau 100 Dollar ergeben
treffer = []
for i in range(1, len(bills) + 1):
    for kombi in it.combinations(bills, r=i):
        if sum(kombi) == 100:
            treffer.append(kombi)

print(f"Wechselmöglichkeiten für 100$: {len(treffer)}")

# Optional: erste 5 anzeigen
print("Beispiele:")
for k in treffer[:5]:
    print(k)


# -------------------------------------------
# Beispiel 2: Poker – Wieviele mögliche 5er-Kartenhände gibt es?
# -------------------------------------------
ranks = list(map(str, list(range(2, 11)) + ["J", "Q", "K", "A"]))
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

# Erzeuge ein vollständiges Kartendeck
deck = list(it.product(ranks, suits))  # 52 Karten

# Alle Kombinationen von 5 Karten (ohne Reihenfolge)
hands = it.combinations(deck, 5)
anzahl_haende = sum(1 for _ in hands)
print(f"Anzahl möglicher Pokerhände: {anzahl_haende}")  # 2.598.960
