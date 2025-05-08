"""
List Comprehensions sind eine kompakte Möglichkeit in Python, um
Listen zu erstellen. Sie kombinieren Schleifen und Bedingungen auf
elegante Weise und machen den Code oft kürzer und lesbarer.

Dieses Skript zeigt grundlegende Anwendungen von List Comprehensions.
"""

# Klassisch: Liste der Quadrate von 0 bis 9 mit einer for-Schleife
result = []
for i in range(0, 10):
    result.append(i**2)

print(result)

# Gleiche Funktionalität mit einer List Comprehension
result = [i**2 for i in range(0, 10)]
print(result)

result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)

# List Comprehension mit Bedingung: Nur gerade Zahlen
result = [i for i in range(10) if i % 2 == 0]
print(result)

# List Comprehension mit Strings: Länge jedes Worts in der Liste
woerter = ["Apfel", "Banane", "Kiwi"]  # [5, 6, 4]
length_words = [len(s) for s in woerter]
print(length_words)  # [5, 6, 4]

# Verschachtelte List Comprehension: Kartesisches Produkt aus zwei Listen 
liste_a = [1, 2, 3]
liste_b = [4, 5]

cart_produkt = []
for a in liste_a:
    for b in liste_b:
        cart_produkt.append((a, b))
print(cart_produkt)

cart_produkt = [(a, b) for a in liste_a for b in liste_b]
print(cart_produkt)



# Ternärer Operator C: x = Bedingung ? 1 : 2

# 1) Aufgabe: Erstelle eine Liste aller Zahlen zwischen 1 und 20,
# die durch 3 oder 5 teilbar sind, mit einer List Comprehension


# 2) Aufgabe: Erstelle eine Liste mit Paaren (i, j) für i von 0 bis 2
# und j von 0 bis 2, aber nur wenn i != j