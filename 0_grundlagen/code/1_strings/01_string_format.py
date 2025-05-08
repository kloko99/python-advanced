"""
f-Strings und die Methode `format()` in Python

Python bietet leistungsfähige Möglichkeiten zur String-Formatierung. Zwei
häufig verwendete Ansätze sind f-Strings (seit Python 3.6) und die Methode
`format()`. Beide erlauben das Einfügen von Werten in Strings und das
Anpassen des Ausgabeformats.

Themenübersicht:
1. Grundlagen von f-Strings
2. Platzhalter und Formatierung mit `format()`
3. Darstellung von Zahlensystemen
4. Darstellung großer Zahlen mit Tausendertrenner
"""

# 1. Grundlagen von f-Strings
# f-Strings beginnen mit einem `f` oder `F` vor den Anführungszeichen.
# Innerhalb geschweifter Klammern `{}` können Variablen oder Ausdrücke
# direkt eingebettet werden.
name = "Alice"
age = 30

# Sie können auch Ausdrücke oder Funktionen innerhalb der Klammern verwenden.

# Formatierung von Zahlen
pi = 3.14159265359

# 2. Platzhalter und Formatierung mit `format()`
# Die Methode `format()` verwendet geschweifte Klammern `{}` als Platzhalter.
# Werte werden in der Reihenfolge der Argumente eingefügt.

# Positionale Argumente können durch Indizes spezifiziert werden.

# Benannte Argumente können ebenfalls verwendet werden.

# Formatierung von Zahlen

# 3. Darstellung von Zahlensystemen
# Zahlen können als Binär-, Oktal-, oder Hexadezimalwerte dargestellt werden.
number = 255

# Mit `format()`

# 4. Darstellung großer Zahlen mit Tausendertrenner
# Zahlen können mit einem Komma als Tausendertrenner formatiert werden.
large_number = 1234567890

# Mit `format()`

# Anpassung des Dezimaltrenners (z. B. für europäische Formate)
