"""
Datentyp `bool` in Python

Der Datentyp `bool` repräsentiert in Python die zwei Wahrheitswerte `True`
und `False`. Er wird häufig in Kontrollstrukturen, Vergleichen und logischen
Operationen verwendet.

Themenübersicht:
1. Grundlagen des Datentyps `bool`
2. Erzeugung von Booleschen Werten
3. Vergleichsoperatoren
4. Logische Operationen
5. Konvertierung in und von `bool`
6. Falsy-Werte in Python
"""

# 1. Grundlagen des Datentyps `bool`
# Boolesche Werte können entweder `True` oder `False` sein.

# 2. Erzeugung von Booleschen Werten
# Boolesche Werte entstehen häufig durch Vergleichsoperationen.
number = 10

# 3. Vergleichsoperatoren
# Vergleichsoperatoren erzeugen Boolesche Werte.
a, b = 5, 10

# 4. Logische Operationen
# Python unterstützt die logischen Operatoren `and`, `or` und `not`.
x, y = True, False

# 5. Konvertierung in und von `bool`
# Mit `bool()` können andere Datentypen in Boolesche Werte konvertiert werden.
# Werte, die als "leer" oder "null" betrachtet werden, ergeben `False`.

# 6. Falsy-Werte in Python
# Python betrachtet die folgenden Werte als `False` (falsy):
# - Numerische Nullwerte: 0, 0.0, 0j (komplexe Null)
# - Leere Container: [], (), {}, set(), ""
# - Der Wert `None`
# - Der Boolesche Wert `False`

# Beispiele für falsy-Werte:
print("Bool von 0:", bool(0))  # False
print("Bool von 0.0:", bool(0.0))  # False
print("Bool von leerem Tuple:", bool(()))  # False
print("Bool von leerer Liste:", bool([]))  # False
print("Bool von leerem Dictionary:", bool({}))  # False
print("Bool von None:", bool(None))  # False
