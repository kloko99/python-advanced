"""
Lese die Datei diabetes2.csv mit Hilfe der csv-Library ein.
Auf Basis dieser Datei soll eine neue Datei erstellt werden, die nur
die Spalten BMI, age und outcome berücksichtigt.
Ferner sollen nur Einträge berücksichtigt werden
mit outcome = 1

Schreibe die Daten kommasepariert in eine neue Datei:
diabetes_positive_outcome.csv

Außerdem interessieren uns folgende Werte, die am Ende des Schreibvorgangs
noch ausgegeben werden sollen:

Für alle Einträge mit outcome=1
Mittelwert BMI
Mittelwert Alter
Median BMI
Median Alter
Max BMI, Min BMI
MAX BloodPRESSURE

für Median und Mittelwert nutze das statistics Modul
import statistics
median = statistics.median([2, 3, 4, 5])
mean = statistics.mean([2, 3, 4, 5])

für min/max nutze die Builtin-Funktionen min([1, 2, 3])
und max([3, 2, 1])

"""
