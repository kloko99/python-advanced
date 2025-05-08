"""(mittel)

Das Inventar eines Players (inventory) soll upgedated werden mit den Inhalt einer 
erbeuteten Truhe (loot)

Falls sich der Gegenstand aus der Truhe schon im Inventar befindet, soll 
er mit dem Wert addiert werden. Ansonsten soll er mit dem gegbenen Wert eingefügt werden.

inventory = {
    "potion": 2, 
    "shield": 1, 
    "map": 2
}

loot = {
    "potion": 2, 
    "map": 1,
    "food": 1
}

führe die Dictionaries zu einem Dict zusammen. 
Falls ein Key doppelt vorkommt, addiere die Values 

inventory_new: 

{
    "potion": 4,
    "map": 3,
    "food": 1,
    "shield": 1,
}

(!)-----------------------------------------------------------------------------
Hinweise: 
1) um zwei Dicts zu einem Dict zusammenzufügen, gibt es den 
| - Operator. 

c = a | b 

Allerdings werden die Values bei mehrmaligen Vorkommen von Keys überschrieben. 
Das ist also nur ein Teil der Lösung. 

2) Um auf einen Value zuzugreifen, kann man via dem Key den []-Operator nutzen
value = a[KEYNAME]

eine andere Möglichkeit ist die get-Methode, die bei Nicht-Vorkommen einen 
Defaultwert hat.

value = a.get(KEYNAME, DEFAULTWERT)

-----------------------------------------------------------------------------

"""
inventory = {"potion": 2, "shield": 1, "map": 2}
loot = {"potion": 2, "map": 1, "food": 1}

inventory_new = {}
