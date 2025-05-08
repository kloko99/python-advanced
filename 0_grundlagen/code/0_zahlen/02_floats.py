"""
Fließkommazahlen in Python: Stellen, Präzision und Probleme

Fließkommazahlen werden in Python mit dem Typ `float` dargestellt. Dieser
ermöglicht die Darstellung von Dezimalzahlen und unterstützt auch die
wissenschaftliche Notation. Allerdings gibt es wichtige Aspekte und
Einschränkungen, die beachtet werden sollten.
Er enstpricht dem C Datentyp double (64 bit), und ist in IEEE 754 spezifiziert.

Themenübersicht:
1. Eigenschaften von Fließkommazahlen
2. Probleme mit der Präzision
3. Rundung und Formatierung
4. Wissenschaftliche Notation
5. Typkonvertierungen: int, float, str
"""

# 1. Eigenschaften von Fließkommazahlen
# Fließkommazahlen werden mit einer begrenzten Präzision gespeichert.

# 2. Probleme mit der Präzision
# Manche Zahlen können nicht exakt als Binärwerte dargestellt werden.
# Beispiel für ein Problem der Präzision:

# 3. Rundung und Formatierung
# Python bietet Funktionen, um Fließkommazahlen zu runden oder zu
# formatieren.
# Beispiel: Runden auf zwei Dezimalstellen

# Bankers' Rounding
# Python verwendet standardmäßig "Bankers' Rounding" in der Funktion
# `round()`. Dabei werden Werte genau zwischen zwei Zahlen (z. B. 2.5)
# zur nächsten geraden Zahl gerundet.

# 4. Wissenschaftliche Notation
# Fließkommazahlen können in der wissenschaftlichen Notation dargestellt
# werden.

# 5. Typkonvertierungen: int, float, str
# Umwandlung von int zu float

# Umwandlung von float zu int
# Dabei werden Nachkommastellen abgeschnitten (nicht gerundet).

# Umwandlung von str zu float
# Nur gültig, wenn der String eine gültige Fließkommazahl enthält.

# Fehlerfall bei ungültiger Konvertierung
