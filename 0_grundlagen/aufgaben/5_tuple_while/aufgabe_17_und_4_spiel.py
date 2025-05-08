"""
schwer

Black Jack (17 und 4)

Vereinfachte Version von 17 und 4, in der der Spieler nur gegen sich selbst
spielt.
Spieler zieht solange Karten, bis er entscheidet, das Spiel zu beenden oder sein Kartenwert > 21 ist.
Wenn der Gesamtwert seiner Karten <= 21 und > 17, hat der Spieler gewonnen.
Anderenfalls hat er verloren.

1. Erstelle dazu ein Karten-Deck (Kreuzprdukt aus values und colors)
2. Nutzde die shuffle - Methode aus dem random Modul, um das dEck zu mischen
3. Das Spiel beginnt, es werden initial zwei Karten gezogen.

Kartenwerte
2, 3, 4, 5, 6, 7, 8, 9, 10
Bube, Dame, König: 10
Ass 11

shuffle methode aus dem random Modul
es werden 4 Kartensätze in einem Spiel genutzt



Beispiel 1:
---------------
Du hast folgende Karte gezogen: Kreuz Fünf
Du hast folgende Karte gezogen: Herz Drei
Aktuelle Punkte: 8
Willst du eine weitere Karte ziehen? J/N: J
Du hast folgende Karte gezogen: Herz Acht
Aktuelle Punkte: 16
Willst du eine weitere Karte ziehen? J/N: J
Du hast folgende Karte gezogen: Karo Bube
Aktuelle Punkte: 26
Du hast verloren!
Game Over

Beispiel 2:
-----------------
Du hast folgende Karte gezogen: Pik Zwei
Du hast folgende Karte gezogen: Pik Acht
Aktuelle Punkte: 10
Willst du eine weitere Karte ziehen? J/N: J
Du hast folgende Karte gezogen: Karo Sieben
Aktuelle Punkte: 17
Willst du eine weitere Karte ziehen? J/N: N
Du hast verloren, GAME OVER!


"""
import random


values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
colors = ["Pik", "Herz", "Kreuz", "Karo"]
