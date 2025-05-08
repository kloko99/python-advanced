"""
While-Schleifen in Python

Die `while`-Schleife ist eine Kontrollstruktur, die einen Codeblock so lange
wiederholt, wie eine bestimmte Bedingung `True` ist. Python bietet auch
zusätzliche Steuerungsmöglichkeiten wie `break`, um Schleifen zu
unterbrechen, und die Kombination `while-else`.

Themenübersicht:
1. Grundlagen der while-Schleife
2. Verwendung von `while-else`
3. Endlose Schleifen
4. Abbruch von Schleifen mit `break`
5. `while` mit Benutzerinteraktion
"""

# 1. Grundlagen der while-Schleife
# Eine Schleife, die Zahlen von 1 bis 5 ausgibt

# 2. Verwendung von `while-else`
# Der `else`-Block wird ausgeführt, wenn die Bedingung der Schleife `False`
# wird, und die Schleife nicht durch `break` unterbrochen wurde.
number = 3

# 3. Endlose Schleifen
# Eine Schleife ohne Ende (vorsichtig verwenden, da sie den Code blockieren
# kann). Abbruch mit `Ctrl+C` während der Ausführung.
# while True:
#     print("Diese Schleife läuft unendlich.")

# Endlos mit Bedingung und `break`
print("Endlose Schleife mit Bedingung:")
i = 0

# 4. Abbruch von Schleifen mit `break`
# Eine Schleife, die endet, wenn ein bestimmter Wert erreicht wird
number = 10

# 5. `while` mit Benutzerinteraktion
# Eine Schleife, die Benutzereingaben verarbeitet und bei "quit" endet
print("Geben Sie Text ein (oder 'quit' zum Beenden):")
