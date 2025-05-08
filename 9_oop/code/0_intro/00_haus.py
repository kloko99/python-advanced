"""
Eine einfache Klasse, die ein Haus beschreibt.
"""

class House:
    """Das ist eine Klasse Haus. Erbt implizit von object."""
    pass 


small_house = House()  # Instanziieren eines Hausobjects
big_house = House()
# zahl = int("3")


print(type(small_house))  # Objekt der Klasse <class '__main__.House'>
print(id(small_house))    # die Speicheradresse des Objekts
print(id(big_house))

# Identitätsoperator is
if small_house is big_house:
    print("Beide Objekte sind das selbe Objekt")
else:
    print("es sind zwei unterschiedliche Objekte")

# Prüfen, ob ein Obejkt eine Instanz einer Klasse ist
print("is instance house:", isinstance(small_house, House))
print("is instance int:", isinstance(1, int))