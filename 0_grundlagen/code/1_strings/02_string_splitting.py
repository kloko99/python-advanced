"""
String Splitting in Python

Das Zerlegen von Strings (String Splitting) ist eine häufige Aufgabe in der
Datenverarbeitung. Python bietet verschiedene Methoden, um Strings anhand
von Trennzeichen oder festgelegten Mustern zu zerlegen.

Themenübersicht:
1. Die Methode `split()`
2. Zerlegen mit benutzerdefinierten Trennzeichen
3. Zerlegen mit maximaler Anzahl von Teilen
4. Zerlegen in Zeilen mit `splitlines()`
5. Erweiterte Splitting-Optionen mit dem Modul `re`
"""

import re

# 1. Die Methode `split()`
# `split()` zerlegt einen String standardmäßig anhand von Leerzeichen.

text = "Dies ist ein Beispieltext"
# Ausgabe: ['Dies', 'ist', 'ein', 'Beispieltext']

# 2. Zerlegen mit benutzerdefinierten Trennzeichen
# Ein Trennzeichen kann als Argument an `split()` übergeben werden.
csv_text = "Name,Alter,Beruf"

# 3. Zerlegen mit maximaler Anzahl von Teilen
# Mit dem zweiten Argument von `split()` kann die maximale Anzahl der
# Zerlegungen festgelegt werden.

# 4. Zerlegen in Zeilen mit `splitlines()`
# `splitlines()` zerlegt einen String anhand von Zeilenumbrüchen.
multiline_text = "Zeile 1\nZeile 2\r\nZeile 3"

# 5. Erweiterte Splitting-Optionen mit dem Modul `re` (Regex)
# Das Modul `re` erlaubt komplexe Muster für das Zerlegen von Strings.
complex_text = "Wort1;Wort2|Wort3,Wort4"
# Ausgabe: ['Wort1', 'Wort2', 'Wort3', 'Wort4']
