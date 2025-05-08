"""
Dieses Skript gibt eine Einführung in die Rekursion (recursion) in Python.

**Rekursion** bedeutet, dass sich eine Funktion selbst aufruft, um ein Problem
in kleinere Teilprobleme zu zerlegen. Sie besteht aus:
1. einer Abbruchbedingung (base case)
2. einem rekursiven Schritt, der sich dem Abbruch annähert

Rekursion kann elegante Lösungen für Probleme mit wiederholter Struktur liefern –
zum Beispiel für:
- das Durchlaufen von verschachtelten Strukturen (z. B. Verzeichnisse, JSON)
- das Umwandeln oder Durchsuchen von Baumstrukturen
- das Auflösen von Pfadproblemen

"""
import math

def factorial(n: int) -> int:
    """Rekursive Implementierung der Fakultät. 
    """
    if n < 0:
        raise ValueError("Fakultät von negativen Zahlen ist nicht definieren")
    
    print(f"{n=}")
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    print(f"{result=}")
    return result


result = factorial(-2)   # Fakultät: 4 * 3 * 2 * 1
print(result)


# def print_nested_iterativ(data):
#     pass


# def print_nested(data, indent=0):
#     pass


# nested = ["a", ["b", ["c", "d"], "e"], "f"]
# print("Verschachtelte Liste:")
# # print_nested(nested)
# print_nested_iterativ(nested)


# # Beispiel 2: Durchsuchen eines verschachtelten Wörterbuchs nach einem Schlüssel
# def find_key(d, target):
#     pass


# person = {
#     "name": "Alice",
#     "details": {
#         "age": 30,
#         "contact": {"email": "alice@example.com", "phone": "123-456"},
#     },
# }

# print("Email gefunden:", find_key(person, "email"))
