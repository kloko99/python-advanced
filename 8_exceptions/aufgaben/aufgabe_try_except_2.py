"""
Schreibe die Funktion word_count(path: str) → int, die

1. die Datei **mit** with open(path) öffnet und ihren gesamten Inhalt
   einliest,
2. die Zahl aller Wörter (Sequenzen aus Buchstaben/Ziffern) zurückgibt,
3. folgende Fehler abfängt:
      • FileNotFoundError → gib „Datei nicht gefunden“ aus und liefere 0
      • UnicodeDecodeError → gib „Datei‑Encoding unbekannt“ aus und liefere 0
4. **finally:** drucke *immer* „Analyse abgeschlossen.“
   (Hier wird nichts geschlossen – das erledigt already der with‑Block.)

Beispiel:

    >>> print(word_count("demo.txt"))
    128
    Analyse abgeschlossen.

    >>> print(word_count("not_found.txt"))
    Datei nicht gefunden


    >>> print(word_count("strange_utf16.txt"))
    Datei-Encoding unbekannt

Die Wörter lassen sich entweder mit str.split() oder
mit re.findall(r"\w+", text) zählen.
"""
