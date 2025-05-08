"""
Schwer

Erstelle via Usereingabe zwei Vektoren gleicher Länge
und führe im Anschluss eine Vektoraddition aus.

Wie addiert man Vektoren?
https://de.serlo.org/mathe/1759/vektoren-addieren-und-subtrahieren

Die Vektoren sind einfache Python-Listen und der zu
verwendende Datentyp der Vektorwerte ist Integer.

Um eine Vektor-Addition durchzuführen, müssen die Vektoren
die gleiche Länge haben. 

Schreibe ein Programm, welches die Vektoren auf gleiche 
L#nge prüft und dann einen neuen Vektor erzeugt. Wir gehen bei der Eingabe von
validen Daten aus (also User gibt Integer ein und keine BUchstaben u.ä.)

Nutze dazu split(","), for-loop, append

Beispiel:
Bitte gebe die Werte für den Vektor 1 an: 1,2,3
Bitte gebe die Werte für den Vektor 2 an: 2,3,4
der neue Vektor ist: [3, 5, 7]

Empfehlung Vorgehensweise:
1) Vektordaten vom User erhalten, zum Beispiel als kommaspaprierter String
2) Split durchführen und die Liste mit Zahl-Strings konvertieren nach int
3) das für den 2. Vektor wiederholen
4) Prüfen, ob beide Vektoren (Listen) gleich lang sind 
5) Falls ja, die Vektoraddition elementweise durchführen.
"""

vector_1_str = input("Bitte gebe die Werte für den Vektor 1 an: ").split(",")
vector_2_str = input("Bitte gebe die Werte für den Vektor 2 an: ").split(",")

# 2, 3) jetzt konvertieren nach Listen von int

# 4) Prüfen, ob Listen gleich lang sind


# 5) Vektoraddition durchführen

# 6) Neuen Vektor ausgeben
