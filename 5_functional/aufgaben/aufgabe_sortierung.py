# 1. Sortiere nach Einwohner (LEICHT)
lst = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]


# 2. Sortiere nach Bundesstaaten (Alabama, California...) LEICHT
states = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]


# 3. Sortiere absteigend (LEICHT)
lst = [500, 1000, 400, 40000, 999, 2, 0.5, 17]


# 4. Sortiere nach Vornamen(MITTEL)
people = [
    {
        "first": "Arthur",
        "last": "Dent",
        "id": "23s",
    },
    {
        "first": "Zaphod",
        "last": "Beeblebrox",
        "id": "42ai",
    },
    {
        "first": "Ford",
        "last": "Perfect",
        "id": "233",
    },
]

# 5. Sortiere nach Punkten (aufsteigend) LEICHT
player = {"peter": 100, "klaus": 34, "wizz": 222, "angela": 23, "sabine": 400}

# 6 Gegebene eine Liste mit Personen und deren Verkäufen. MITTEL
# Der Verkaufserlös errechnet sich durch die letzten beiden Positionen,
# z.b. 46 x 18.67 für John Miller. Sortiere nach Verkaufserlös
umsaetze = [
    ("John", "Miller", 46, 18.67),
    ("Randy", "Steiner", 48, 27.99),
    ("Tina", "Baker", 53, 27.23),
    ("Andrea", "Baker", 40, 31.75),
    ("Eve", "Turner", 44, 18.99),
    ("Henry", "James", 50, 23.56),
]


# 7. Sortiere aufsteigend nach max-Wert der Liste. SCHWER
stox = [
    ["a", [22, 25, 14, 23]],
    ["b", [122, 25, 14, 233]],
    ["c", [422, 25, 14, 33]],
    ["d", [22, 1025, 14, 33]],
    ["e", [2, 5, 4, 3]],
]


# 8 Sortiere aufsteigend nach Modul-Name
"""
falsch: ['pre-commit', 'pytest-cov', 'pytest==5.2', "waldo-parillo;sys_platform=='win32'"]

richtig: ['pre-commit', 'pytest==5.2', 'pytest-cov', "waldo-parillo;sys_platform=='win32'"]
"""

modules = [
    "waldo-parillo;sys_platform=='win32'",
    "pytest==5.2",
    "pytest-cov",
    "pre-commit",
]


def sort_key(s: str) -> str:
    """Extrahiere Modulnamen aus String."""

    # Falls Versionsnummer fix gepinnt ist (zb. pytest==2.3.1), splitten und 
    # vorderen Teil nehmen
    if "==" in s:
        s = s.split("==", maxsplit=1)[0]

    # Falls Platform angegeben ist (zb. waldo-parillo;sys_platform=='win32'), 
    # an ";" splitten und  vorderen Teil nehmen
    if ";" in s:
        s = s.split(";", maxsplit=1)[0]
    
    return s 


sorted_modules = sorted(modules, key=sort_key)
print(sorted_modules)