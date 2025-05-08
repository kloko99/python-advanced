"""
Funktionen mit `yield` sind sogenannte Generatorfunktionen.
Statt mit `return` einen Wert zurückzugeben und zu beenden, liefern
sie mit `yield` einen Wert und pausieren ihren Zustand – beim nächsten
Aufruf wird der Code direkt nach dem `yield` fortgesetzt.

Generatorfunktionen erzeugen automatisch einen Iterator und sind
speichereffizient, da sie Werte bei Bedarf liefern (Lazy Evaluation).

Typische Anwendungen:
- Große Datenmengen sequentiell verarbeiten
- Unendliche Sequenzen generieren
- Zustandsbehaftete Abläufe abbilden

Dieses Skript zeigt verschiedene Anwendungsbeispiele für `yield`.
"""
from typing import Iterator

def print_numbers(numbers) -> Iterator:
    for i in numbers:
        yield i


numbers_generator = print_numbers([1, 2, 3])  # Iterator
print(next(numbers_generator))
print(next(numbers_generator))
print(next(numbers_generator))
# print(next(numbers_generator)) # Stop Iteration

# Beispiel: Zahlen filtern: alle Zahlen größer als 3
def filter_values(values: list[int]) -> list[int]:
    """KLassische Implementierung einer Filterfunktion."""
    results = []
    for value in values:
        if value > 3:
            results.append(value)

    return results


def filter_values_advanced(values: list[int]) -> Iterator:
    """Filterfunktion als Generatorfunktion implementiert."""
    for value in values:
        if value > 3:
            yield value
        

for i in filter_values_advanced([4, 1, 23, 2]):
    print(i)


def infinite_counter():
    """Implementierung eines unendlichen Counters."""
    i = 0
    while True:
        yield i 
        i += 1


for i in infinite_counter():
    print(i)