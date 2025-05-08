"""
Die Funktionen `all()` und `any()` sind eingebaute Funktionen in Python
zur Auswertung von Wahrheitswerten in iterierbaren Objekten (z. B. Listen,
Tupel oder Generatoren).

- `all(iterierbar)` gibt True zurück, wenn **alle** Elemente True sind.
- `any(iterierbar)` gibt True zurück, wenn **mindestens eines** True ist.

Beide Funktionen arbeiten effizient mit Generator Expressions, da die
Auswertung bei Bedarf abbricht (Short-Circuit Evaluation).

Dieses Skript zeigt die Grundlagen und reale Anwendungsbeispiele für
`all()` und `any()`.
"""

# all(): Sind alle Bedingungen erfüllt?
werte = [1, 2, 0, ""]
if all(werte):
    print("alle Werte in werte sind wahr")
else:
    print("In werte befindet sich ein unwahrer Wert")



# any(): Ist mindestens eine Bedingung erfüllt?
werte = [1, 2, 0, ""]
if any(werte):
    print("Zumindest ein WErt ist wahr")
else:
    print("alle Werte sind unwahr")


# Aufgabe: Gegeben ist eine Liste von Logeinträgen (True/False),
# prüfe mit all(), ob **alle** Systeme online sind
system_status = [True, True, True, False]
print("Alle Systeme online:", all(system_status))


# Aufgabe: Gegeben ist eine Liste von Kommentaren, prüfe mit any(),
# ob mindestens ein Kommentar ein bestimmtes Schlüsselwort enthält
kommentare = ["gut", "läuft stabil", "fehler", "ok"]
schluesselwort = "fehler"
beinhaltet_fehler = any(schluesselwort in k for k in kommentare)
print("Fehler gefunden:", beinhaltet_fehler)
