"""(MITTEL)
Schreibe ein Python-Programm, das Folgendes leistet:

Erfassung von Messwerten: Das Programm soll den Benutzer auffordern, Messwerte für den Stickstoffgehalt in der Pflanzenerde einzugeben. Der Benutzer kann mehrere Messwerte eingeben, bis er entscheidet, die Eingabe mit dem Wort "ende" zu beenden.

Plausibilitätsprüfung: Jeder eingegebene Wert soll auf Plausibilität geprüft werden. Gültige Messwerte liegen zwischen 0% und 100%. Werte außerhalb dieses Bereichs sollen mit einer Warnung zurückgewiesen werden.

Berechnung und Ausgabe von Statistiken: Nach Beendigung der Eingabe soll das Programm den Durchschnitt der gültigen Messwerte berechnen und ausgeben. Zusätzlich soll angegeben werden, ob der Durchschnittswert im optimalen Bereich für Stickstoff liegt. Für diese Aufgabe nehmen wir an, dass der optimale Bereich zwischen 20% und 40% liegt.

Beispiel:
-------------
Willkommen beim Stickstoff-Messgerät 2000
Kakulieren Sie den Stickstoff ihrer Zimmerpflanze!
Geben Sie den Stickstoffgehalt in Prozent ein (oder 'ende' zum Beenden): 22.2
Geben Sie den Stickstoffgehalt in Prozent ein (oder 'ende' zum Beenden): 24.1
Geben Sie den Stickstoffgehalt in Prozent ein (oder 'ende' zum Beenden): 38.3
Geben Sie den Stickstoffgehalt in Prozent ein (oder 'ende' zum Beenden): 11.3 
Geben Sie den Stickstoffgehalt in Prozent ein (oder 'ende' zum Beenden): ende
Durchschnittlicher Stickstoffgehalt: 23.974999999999998%
Der Durchschnittswert liegt im optimalen Bereich.

Nutze dazu einen while-Loop, if-else, input, break

"""

