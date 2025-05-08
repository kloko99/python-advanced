# Implementieren der Collatz-Funktion (MITTEL)
# https://de.wikipedia.org/wiki/Collatz-Problem

"""
Bei dem Problem geht es um Zahlenfolgen, die nach einem einfachen Bildungsgesetz konstruiert werden:

    Beginne mit irgendeiner natürlichen Zahl n > 0.
    Ist n gerade, so nimm als nächstes n / 2 .
    Ist n ungerade, so nimm als nächstes 3 * n + 1.
    Wiederhole die Vorgehensweise mit der erhaltenen Zahl.

So erhält man zum Beispiel für die Startzahl n = 19 die Folge:
19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1,

Die Funktion soll zum Beispiel terminieren (beenden), wenn n == 1.
Die Funktion soll nicht rekursiv implementiert werden.
Die Funktion soll eine Liste zurückgeben
Nutze dazu einen while-Loop
"""
