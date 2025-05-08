"""
Dieses Skript demonstriert eine rekursive Implementierung der
Binärsuche (Binary Search) in Python.

Die Binärsuche ist ein effizientes Verfahren, um ein Element in einer
**sortierten** Liste zu finden. Dabei wird die Liste bei jedem Schritt
halbiert, sodass der Suchbereich logarithmisch schrumpft (O(log n)).

**Voraussetzung:** Die Liste muss aufsteigend sortiert sein.

Vorteile der rekursiven Variante:
- eleganter und kompakter Code
- gut geeignet für bildungsorientierte Zwecke (z. B. Algorithmenlernen)

Nachteile:
- tiefe Rekursion kann bei sehr großen Listen zum Stack Overflow führen

Dieses Skript enthält eine rekursive Funktion zur Binärsuche und ein
Beispiel zur Anwendung.
"""
import random 
import timeit
import bisect   # binary search in Python als Modul vorhanden.

def get_dataset(population: int, k: int) -> list[int]:
    """ERzeuge Datensatz aus Sampeln einer Population."""
    return sorted(random.sample(population=[i for i in range(population)], k=k))

def naive_search(arr, tar):
    """Suche iterativ in einem Array nach target."""
    for index, value in enumerate(arr):
        if tar == value:
            return index 
        
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """Rekursive Implementierung von Binary Search."""

    if left > right:
        return -1

    mid = (left + right) // 2

    if target == arr[mid]:
        return mid
    
    if target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)



dataset = get_dataset(population=10_000, k=1000)
target = dataset[random.randint(0, 1000)]

result_naive = timeit.timeit(
    # stmt="naive_search(dataset, target)",
    stmt="dataset.index(target)",
    globals=globals(),
    number=50_000
)
print(result_naive)

result_binary = timeit.timeit(
    stmt="binary_search_recursive(dataset, target, 0, len(dataset) - 1)",
    globals=globals(),
    number=50_000
)
print(result_binary)

