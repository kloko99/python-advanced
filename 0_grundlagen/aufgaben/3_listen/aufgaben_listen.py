# leicht bis mittel

# 1. Iteration über Liste (leicht)
"""
Iteriere über die Liste und gebe die Elemente aus!
Zusatzaufgabe: gebe zusätzlich den enstprechenden Index aus,
zb. für Banane den Index 0

0 Banane
1 Apfel
2 Kirsche
"""
fruits = ["Banane", "Apfel", "Kirsche"]

# 2. Filtern einer Liste 1 (leicht)
"""
Erstelle aus einer gegebenen Liste eine neue Liste filtered_fruits. Die neue Liste darf nur Elemente enthalten, die mit einem großen B anfangen.

Tip: Nutze dazu die string-Methode startswith oder 
den Index-Operator [].

Result: filtered_fruits = ["Banane", "Birne"]
"""
fruits = ["Banane", "Apfel", "Kirsche", "Birne"]


# 3. Filtern einer Liste 2 (mittel)
"""
Erstelle aus einer gegebenen Liste eine neue Liste filtered_numbers. Die neue Liste darf nur Elemente enthalten, die größer als 5 sind und kleiner als 100. Die filtered_numbers-Liste muss sortiert ausgegeben werden.

result = [23, 42, 99]
"""
numbers = [1, 4, 5, 2, 42, 2, 1, 99, 23, 23]


# 5. das letzte Element (mittel)
"""
Gegeben ist eine Liste, die auch leer sein kann. Prüfe, ob sich mindestens ein Element in der Liste befindet und printe das letzte Element in der Liste.

Erinnerung: eine Liste ist True, wenn sie mindestens 
ein Element enthält.
"""
symbols = ["B", "C"]


# 6. erlaubte Werte (mittel)
"""
Gegeben sind zwei Listen:
eine Ausgangsliste a und
eine Liste mit erlaubten Werten allowed_values.

Prüfe für jedes Element in a, ob es in der erlaubten Liste enthalten ist, und füge es einer neuen Liste c hinzu, wenn das zutrifft. 

tip: 
Iteriere über a und prüfe für jedes Element, ob es erlaubt ist.
Nutze dazu den Membership-Operator in.

result = [50, 200, 50]
"""
a = [50, 100, 40, 20, 200, 50, 100, 10]
allowed_values = [50, 200]


# 7. Bereiningen der Liste (mittel)
"""
Gegeben ist eine Liste a mit String-Elementen. Bereinige diese Elemente von _ (underscore) und speichere sie in einer neuen Liste. Leere Elemente sollen nicht in die neue Liste aufgenommen werden.

result = [xx, alphabeta]

"""
a = ["x_x", "alpha_beta", "_"]


# 8. Bereiningen der Liste von Steuerzeichen und x (schwer) 
"""
Gegeben ist eine Liste a mit String-Elementen. Bereinige diese Elemente von Whitespace und Steuerzeichen. Entferne alle x aus den Strings.

Tip:
Die String-Methode strip() entfernt Steuerzeichen 
am Anfang und Ende eines Strings.

result = ["halt", "and", "catch", "fire"]
"""
a = ["haxlt ", "\nandx", "\tcatch ", " xfire "]


# 9. Zusammenführen von zwei Listen (schwer)
"""
Gegeben sind zwei Listen a und b, wobei
- Liste a eine variable Länge aufweisen kann (auch leere Mengen sind erlaubt) und
- Liste b immer aus 5 Elemente besteht.

a = ["A", "B", "C", "D"]
b = [1, 2, 3, 4, 5]


Führe diese beiden Listen zu einer neuen Liste zusammen,
und zwar so, dass jeweils das Element am selben Index zu einem String konkateniert wird.

Ist a kleiner als b, wird die Zusammenführung entsprechend reduziert.
Ist a größer als b, werden die überschüssigen Elemente ignoriert.

Beispiel (a gleich groß b): Zusammenführung aller 
Elemente 
a =  ["A", "B", "C", "D"]
b = [1, 2, 3, 4, 5]

Ergebnis c:
["A1", "B2", "C3", "D4", "E5"]

Beispiele (a kleiner als b): Zusammenführung wird auf drei Elemente reduziert
a = ["A", "B", "C"]
b = [1, 2, 3, 4, 5]

Ergebnis c: ["A1", "B2", "C3"]

Beispiele (a größer als b): überschüssige Elemente von a werden ignoriert
a =  ["A", "B", "C", "D", "E", "F"]
b = [1, 2, 3, 4, 5]

Ergebnis c:
["A1", "B2", "C3", "D4", "E5"]

Prüfe für alle drei Fälle!
"""
a = ["A", "B", "C"]
b = [1, 2, 3, 4, 5]
c = []
