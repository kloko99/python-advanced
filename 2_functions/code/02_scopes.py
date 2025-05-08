"""
Funktionen und Scopes in Python

Der Scope (Gültigkeitsbereich) bestimmt, wo Variablen definiert und verwendet
werden können. Python unterscheidet zwischen lokalem, globalem und
nicht-lokalem Scope. Das Verständnis von Scopes ist wichtig, um Funktionen
effektiv zu nutzen und Fehler durch unerwartete Variablenänderungen zu
vermeiden.

Themenübersicht:
1. Lokaler Scope
2. Globaler Scope
3. Die `global`-Anweisung
"""

# 1. Lokaler Scope
# Variablen, die innerhalb einer Funktion definiert werden, sind lokal
# und außerhalb der Funktion nicht sichtbar.


# print(local_var)  # Fehler: local_var ist außerhalb nicht definiert

# 2. Globaler Scope
# Variablen, die außerhalb von Funktionen definiert werden, sind global
# und können überall im Code verwendet werden.


# 3. Die `global`-Anweisung
# Mit der `global`-Anweisung kann innerhalb einer Funktion eine globale
# Variable verändert werden.


# 1.  Aufgabe
# Erstelle eine Funktion filter_integer_data, die eine Liste
# als Parameter entgegennimmt und jedes Element prüft, ob es vom
# Typ integer ist. Der Rückgabewert der Liste ist eine Liste mit)
# Integerwerten.
# Nutze zum Prüfen des Typs die Funktion type() oder isinstance()
#
# result = filter_integer_data(["a", 3, 1, 3.3])
# Result: [3, 1]
