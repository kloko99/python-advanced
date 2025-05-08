"""
Gegeben sind zwei Dicts, a und b
Erstelle ein neues Dict, dass nur Keys enthält, die in beiden
dicts vorkommen.
der Key dieses neuen Dicts ist jeweils der Key, der Value ist
ein Tupel aus den Werten der Ursprungsdicts.

a = {"a": 1, "b": 2, "z": 3, "c": 4}
b = {"a": 4, "b": 4, "c": 43, "s": 3}

c = {'c': (4, 43), 'a': (1, 4), 'b': (2, 4)}
"""
a = {"a": 1, "b": 2, "z": 3, "c": 4}
b = {"a": 4, "b": 4, "c": 43, "s": 3}
c = {}
