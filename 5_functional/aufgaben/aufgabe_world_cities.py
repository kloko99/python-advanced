# Lese die Datei worldcities.csv mit dem CSV - Reader ein,
# sortiere die Einträge nach dem Feld "city_ascii" (siehe worldcities.csv) und speichere sie in einer
# neuen Daten worldcities_sorted.csv ab.
# Schreibe dazu die Funktion load_cities, sort_cities_by_ascii_name und
# save_cities_to_file.

# 1.b) Länder-Filter
# Erweitere die Aufgabe um einen Länder-Filter: es sollen nur Einträge
# in die neue Datei kommen, die einem eingegebenen Land entsprechen (zb. India)

import csv
from pathlib import Path


def load_cities(filename: str) -> list[dict]:
    """Load Cities from CSV File and return list of dicts."""
    with open(Path(__file__).parent.resolve() / filename, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        return list(reader)
    

def sort_cities_by_ascii_name(cities: list[dict]) -> list[dict]:
    """Sort cities by column ascii_name and return list."""
    return sorted(cities, key=lambda e: e["city_ascii"])


def save_cities_to_file(filename, cities):
    """Save rows to file."""
    with open(Path(__file__).parent.resolve() / filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cities[0].keys())
        writer.writeheader()
        writer.writerows(cities)


if __name__ == "__main__":
    cities = load_cities("worldcities.csv")
    sorted_cities = sort_cities_by_ascii_name(cities)
    save_cities_to_file("worldcities_sorted.csv", sorted_cities)