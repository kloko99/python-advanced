"""
Dieses Skript stellt die klassische Programmieraufgabe "Flood Fill" vor –
eine rekursive oder iterative Technik, um zusammenhängende Bereiche in
z. B. 2D-Matrizen (Bilder, Spielfelder) mit einer neuen Farbe zu füllen.

Der Flood-Fill-Algorithmus funktioniert ähnlich wie der Farbeimer in
Bildbearbeitungsprogrammen: Von einem Startpunkt aus wird jede benachbarte
Zelle überprüft, ob sie die gleiche Ausgangsfarbe hat – falls ja, wird
sie gefüllt und ihre Nachbarn werden ebenfalls geprüft.

Typische Anwendungen:
- Bildbearbeitung
- Spiellogik (z. B. Gebietsübernahme)
- Clusterdetektion in Matrizen oder Graphen

Diese Aufgabe wird oft rekursiv gelöst, lässt sich aber auch iterativ
umsetzen (z. B. mit einem Stack oder einer Queue).

Die folgende Funktion ist ein Gerüst für Flood Fill. Ergänze sie so,
dass sie alle angrenzenden Zellen mit gleicher Farbe ändert.

Hinweis: row = Zeile, col = Spalte (matrix[row][col])
"""


def flood_fill(matrix, row, col, target_color, replacement_color):
    """
    matrix: 2D-Liste von Zeichen oder Zahlen
    row, col: Startkoordinaten (Zeile, Spalte)
    target_color: Farbe, die ersetzt werden soll
    replacement_color: Neue Farbe
    """
    pass  # TODO: Implementiere Flood Fill hier


# Beispiel: 2D-Feld (z. B. Spielfeld oder Bildbereich)
feld = [
    ["A", "A", "B", "B"],
    ["A", "A", "B", "B"],
    ["B", "B", "B", "B"],
    ["B", "B", "C", "C"],
]

# Ziel: Alle zusammenhängenden 'A' ab (0,0) in 'X' ändern
# Erwartet: Obere linke Ecke wird zu 'X'

# flood_fill(feld, 0, 0, 'A', 'X')

# Ausgabe nachher anzeigen
# for zeile in feld:
#     print(zeile)
