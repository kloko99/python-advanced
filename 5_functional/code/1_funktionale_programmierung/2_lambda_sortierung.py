"""
In Python kann die eingebaute Funktion `sorted()` verwendet werden,
um Listen und andere iterierbare Objekte zu sortieren. Dabei kann man
mit dem Parameter `key` eine Funktion übergeben, die bestimmt, nach
welchem Kriterium sortiert werden soll.

Oft wird dafür eine Lambda-Funktion verwendet, da sie es erlaubt,
einfach und direkt ein Sortierkriterium zu definieren, ohne eine
separate Funktion schreiben zu müssen.

Beispiel:
sorted(liste, key=lambda x: x[1])  # Sortiert nach dem zweiten Element

Python verwendet eine stabile Sortierung. Das bedeutet, dass Elemente
mit gleichem Sortierwert ihre ursprüngliche Reihenfolge beibehalten.
Dies ist nützlich, wenn man mehrfach sortieren möchte – z. B. erst
nach Nachnamen, dann nach Vornamen.

Dieses Skript zeigt, wie man `lambda` mit `sorted()` nutzt und erklärt
anhand von Beispielen, was stabile Sortierung bedeutet.
"""

# unsortierte Liste
liste = [3, 5, 1, 9, 1]
# liste.sort()  # inplace Sortierung
liste_sorted = sorted(liste)
print(liste_sorted)  # erzeugt neue Liste


# unsortierte ASCII Buchstaben
chars = ["a", "f", "c", "d", "e"]
print(sorted(chars))


# Großbuchstaben kommen vor Kleinbuchsten (A=65, a=97)
chars = ["a", "f", "b", "B", "A", "d", "e", "ü", "u", "z"]
# a f b b a d e ü i z
print(sorted(chars, key=lambda e: e.lower()))  # e steht für jedes Element der Liste
# ['a', 'A', 'b', 'B', 'd', 'e', 'f', 'u', 'z', 'ü']


# AUFGABE
# Sortiere nach der Zahl
# Ergebnis:
# ids sorted:  ['idx1', 'id2', 'id3', 'id4', 'id5', 'idy5']
ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
print(sorted(ids, key=lambda e: int(e[-1])))  

def fn(e):
    return int(e[-1])

print(sorted(ids, key=fn))  


# SNACKS 1
snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}

# nach Name des Produkts aufsteigend sortiert:
sorted_snacks = sorted(snacks)
print(sorted_snacks)


# nach Preis des Produkts aufsteigend sortiert:
print(snacks.items())
sorted_snacks = sorted(snacks.items(), key=lambda e: e[1])
print(sorted_snacks)

# Aufabge
# Schreibe eine Funktion sort_cities, die eine Liste von Städten entgegennimmt
# und nach Einwohnerzahl sortiert und als Liste von Tupeln zurückgibt
#  Sortierte Städte:  [('New York', 8800000), ('Berlin', 3400000), ...

cities = {
    "Köln": 1_200_000,
    "Berlin": 3_400_000,
    "New York": 8_800_000,
    "München": 1_500_000,
    "Dresden": 900_000,
}
sorted_cities = sorted(cities.items(), key=lambda e: e[1], reverse=True)
print(sorted_cities)

# SNACKS 2
snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}
# e ist ein Tuple aus Key und Dict. Um auf den Preis des Dicts zuzugreifen, 
# nutzen wir e[1] um an das Dict zu kommen und "price" um den Key des Dicts anzusprechen
print(sorted(snacks.items(), key=lambda e: e[1]["price"]))

