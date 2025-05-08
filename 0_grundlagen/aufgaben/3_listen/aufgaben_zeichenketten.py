"""
mittel

Eine als String (Text) dargestellte Binärzahl (0 und 1) soll dahingehend geprüft werden, ob sie maximal eine Folge von Einsen enthält. Die Länge der Folge ist beliebig, sie kann also auch nur einem Element bestehen.
Dabei kann die Binärzahl auch vorangestellte Nullen enthalten. Tip: Nutze die Funktion find.

Falls zwei Folgen von Einsen entdeckt werden, ist die Ausgabe: falsch.

Beispiele:
b = "00"
Lösung: wahr => 00 (0 Folgen)

b = "1100"
Lösung: wahr => 1100 (1 Folge)

b = "1010"
Lösung: falsch => 1010 (2 Folgen)

b = "00111000"
Lösung: wahr => 00111000 (1 Folge)

b = "10000001"
Lösung: falsch => 10000001 (2 Folgen)

b = "1100011001"
Lösung: falsch => 1100011001 (3 Folgen)

die Binärzahl soll als input übergeben werden.
"""

b = "0110100"  # falsch
# b = "1010"      # falsch
# b = "0011000"   # wahr
# b = "10000001"   # falsch
# b = "1100011001" # falsch
# b = "10"         # wahr
# b = "01"         # wahr
# b = "101"        # falsch
