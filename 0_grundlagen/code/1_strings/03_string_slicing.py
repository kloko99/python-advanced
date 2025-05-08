"""
String Slicing in Python

String Slicing erlaubt es, Teilstrings (Substrings) aus einem String zu
extrahieren.
Mit Hilfe von Start-, End- und Schrittwerten kann flexibel auf bestimmte
Abschnitte eines Strings zugegriffen werden.

Themenübersicht:
1. Grundlagen des Slicings
2. Negative Indizes
3. Slicing mit Schrittwerten
4. Nützliche Anwendungen



Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String
"""

# 1. Grundlagen des Slicings
# Slicing wird mit der Syntax `string[start:end]` durchgeführt.
text = "Python Programmierung"

# Extrahieren eines Teilstrings

# Wenn der Start- oder Endwert weggelassen wird, wird der Anfang bzw.
# das Ende des Strings verwendet.

# 2. Negative Indizes
# Mit negativen Indizes kann vom Ende des Strings aus zugegriffen werden.

# Slicing mit negativen Indizes

# 3. Slicing mit Schrittwerten
# Die Syntax `string[start:end:step]` ermöglicht das Überspringen von
# Zeichen im String.

# 4. Nützliche Anwendungen
# - Extrahieren eines Präfixes oder Suffixes
# - Rückwärtslesen eines Strings
# - Teile von Strings verarbeiten oder analysieren

data = "12345-67890"


# # Übung
# # Schneide jeweils alle A aus den Strings
# AAAAB => AAAA
# BBAAABBB => AAA
# AAAABBBB => AAAA
# ABBBBB => A
string = "AAAAB"

string = "BBAAABBB"

string = "AAAABBBB"

string = "BBAABBBB"

string = "ABBBBB"
