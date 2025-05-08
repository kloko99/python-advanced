"""
Wichtige Dictionary-Methoden in Python

Dictionaries sind eine flexible Datenstruktur in Python und bieten eine Vielzahl
von Methoden, um Schlüssel-Wert-Paare hinzuzufügen, zu entfernen, zu durchsuchen
und zu manipulieren.

Themenübersicht:
1. Zugriffsmethoden: `get()`,
2. Aktualisierung und Zusammenführung: `update()`
3. Entfernen von Einträgen: `pop()`, `popitem()`, `clear()`
4. Schlüssel und Werte: `keys()`, `values()`, `items()`
5. Kopieren und Standardwerte: `copy()`, `fromkeys()`
"""

# 1. Zugriffsmethoden
user = {"name": "Alice", "age": 30}

# `get()`: Gibt den Wert für einen Schlüssel zurück, ohne einen Fehler auszulösen,
# wenn der Schlüssel nicht existiert.

# 2. Aktualisierung und Zusammenführung
# `update()`: Aktualisiert das Dictionary mit Werten aus einem anderen
# Dictionary oder iterierbaren Schlüssel-Wert-Paaren.

# 3. Entfernen von Einträgen
# `pop()`: Entfernt einen Eintrag und gibt den Wert zurück. Löst einen Fehler
# aus, wenn der Schlüssel nicht existiert, es sei denn, ein Standardwert wird angegeben.

# `popitem()`: Entfernt und gibt das letzte Schlüssel-Wert-Paar zurück.

# `clear()`: Entfernt alle Schlüssel-Wert-Paare aus dem Dictionary.

# 4. Schlüssel und Werte

# `keys()`: Gibt eine Ansicht aller Schlüssel zurück.

# `values()`: Gibt eine Ansicht aller Werte zurück.

# `items()`: Gibt eine Ansicht aller Schlüssel-Wert-Paare zurück.

# 5. Kopieren und Standardwerte
# `copy()`: Erstellt eine flache Kopie des Dictionaries.

# `fromkeys()`: Erstellt ein neues Dictionary mit den angegebenen Schlüsseln
# und einem Standardwert.
