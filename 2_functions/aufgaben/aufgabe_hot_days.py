"""
HOT DAYS

Schreibe eine Funktion get_hot_work_days(), die aus der Input-Liste weekday_temperatures  eine neue Liste erstellt und diese zurückgibt.
Diese neue Liste soll nur Tage enthalten, die nicht am Wochenende sind und Temperaturen größer gleich 30 Grad Celcius hatten.
Die Einträge in der neuen Liste sollen als Tupel dargestellt werden (Datum, Temperatur)

Ergebnis:
[('2019-07-15', 31), ('2019-07-16', 33), ('2019-07-19', 30), ('2019-07-23', 31)]

Hinweise: diese Aufgabe optional mit list comprehension oder funktional (map,
filter) lösen.
Nutze Typehints!
"""
THRESHOLD = 30

weekday_temperatures = [
    {"day": "Monday", "date": "2019-07-15", "temperature": 31},
    {"day": "Tuesday", "date": "2019-07-16", "temperature": 33},
    {"day": "Wednesday", "date": "2019-07-17", "temperature": 27},
    {"day": "Thursday", "date": "2019-07-18", "temperature": 25},
    {"day": "Friday", "date": "2019-07-19", "temperature": 30},
    {"day": "Saturday", "date": "2019-07-20", "temperature": 31},
    {"day": "Sunday", "date": "2019-07-21", "temperature": 29},
    {"day": "Monday", "date": "2019-07-22", "temperature": 25},
    {"day": "Tuesday", "date": "2019-07-23", "temperature": 31},
    {"day": "Wednesday", "date": "2019-07-24", "temperature": 26},
    {"day": "Thursday", "date": "2019-07-25", "temperature": 23},
    {"day": "Friday", "date": "2019-07-26", "temperature": 22},
    {"day": "Saturday", "date": "2019-07-27", "temperature": 23},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
]
