# Aufgabe. Sortiere nach Stringlänge
monty_crew = ["Cleese", "Idle", "Palin", "Chapman", "Gilliam", "Jones"]
sorted(monty_crew, key=lambda e: len(e)) 
sorted(monty_crew, key=len)    # len(e)

# Nach Name und dann nach Alter sortieren
user = {
    1: {"name": "Ali", "age": 13, "city": "New York"},
    2: {"name": "Ali", "age": 33, "city": "Paris"},
    3: {"name": "Ali", "age": 19, "city": "Istanbul"},
    4: {"name": "Ali", "age": 43, "city": "Kairo"},
    5: {"name": "Ali", "age": 8, "city": "Dortmund"},
    6: {"name": "Alex", "age": 2, "city": "Berlin"},
    7: {"name": "Alex", "age": 12, "city": "Hamburg"},
}
# Sortieren nach Name und Alter in einem Tupel (name, age)
print(sorted(user.items(), key=lambda e: (e[1]["name"], e[1]["age"])))


# nach Nachnamen im String sortieren mit split
python_heros = [
    "Aelric Duskmoor",
    "Thalara Windshade",
    "Balthor Emberveil",
    "Myrren Nightroot",
    "Cedric Fogthorn",
    "Isolde Starwhisper",
    "Morwenna Ashglen",
    "Vaelorn Mistwood",
    "Seraphina Dawnspell",
    "Orwyn Blackbriar",
    "Lyra Moonsong",
    "Galdric Runeweaver",
    "Tamsin Frostvale",
]
