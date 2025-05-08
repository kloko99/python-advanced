"""
Thema: super() in Vererbung und Mehrfachvererbung

Die Funktion super() erlaubt den Zugriff auf Methoden der Oberklasse
in einer geerbten Klasse. Sie wird verwendet, um z. B. die __init__-
Methode der Basisklasse aufzurufen und dabei Mehrfachvererbung korrekt
zu unterstützen.

Bei einfacher Vererbung:
- super() ruft die Methode der direkten Oberklasse auf.

Bei Mehrfachvererbung:
- super() folgt der Method Resolution Order (MRO), die durch
  Python automatisch berechnet wird (C3-Linearization).

Dadurch wird sichergestellt, dass jede Klasse in der Vererbungskette
genau einmal aufgerufen wird – vorausgesetzt alle Klassen nutzen
super() korrekt und rufen es weiter.

"""
