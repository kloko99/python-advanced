"""
Lese die Datei diabetes2.csv mit Hilfe der csv-Library ein.
Auf Basis dieser Datei soll eine neue Datei erstellt werden, die nur
die Spalten BMI, age und outcome berücksichtigt.
Ferner sollen nur Einträge berücksichtigt werden,
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
import csv
import statistics
from pathlib import Path

DIABETES_FILE = Path(__file__).parent /  "diabetes2.csv"
OUTCOME_FILE = Path(__file__).parent /  "diabetes_positive_outcome.csv"

# Positions in CSV
OUTCOME = 8
BLOOD_PRESSURE = 2
BMI = 5
AGE = 7

# write rows after batch size
BATCH_SIZE = 50

filtered = []
head = ["bmi", "age", "blood_pressure"]
bmi = []
ages = []
blood_pressure = []

with open(DIABETES_FILE) as fin, open(OUTCOME_FILE, "w") as fout:
    reader = csv.reader(fin, delimiter=",")
    writer = csv.writer(fout, delimiter=",")
    writer.writerow(head)

    for row in reader:
        if row[OUTCOME] == "1":
            filtered.append([row[BMI], row[AGE], row[BLOOD_PRESSURE]])
            bmi.append(row[BMI])
            ages.append(row[AGE])
            blood_pressure.append(int(row[BLOOD_PRESSURE]))

        if len(filtered) % BATCH_SIZE == 0:
            writer.writerows(filtered)
            filtered = []

    writer.writerows(filtered)

bmi = [float(i) for i in bmi]
ages = [int(i) for i in ages]

bmi_median = statistics.median(bmi)
bmi_mean = statistics.mean(bmi)
age_median = statistics.median(ages)

print("Result")
print("-" * 50)
print(f"BMI Median: {bmi_median}")
print(f"BMI Mittelwert: {bmi_mean}")
print(f"BMI Max: {max(bmi)}")
print(f"BMI Min: {min(bmi)}")

print(f"Ages Median: {age_median}")
print(f"Ages Max: {max(ages)}")
print(f"Ages Min: {min(ages)}")

print(f"Max Blood Pressure: {max(blood_pressure)}")

