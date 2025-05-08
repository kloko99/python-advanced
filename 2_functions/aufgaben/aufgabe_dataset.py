"""
1.  (SCHWER)
Erstelle eine Funktion filter_integer_data, die eine Liste
als Parameter entgegennimmt und jedes Element prüft, ob es vom 
Typ integer ist. Der Rückgabewert der Liste ist eine Liste mit 
Integerwerten. Nutze zum Prüfen des Typs die Funktion type() oder isinstance()

result = filter_integer_data(["a", 3, 1, 3.3])
Result: [3, 1]

2. (MITTEL)
Erstelle eine Funktion check_values, die eine Liste mit float-Werten und einen
tupel übergeben bekommt. Die Funktion prüft, ob alle Elemente
im geschlossenen Interval [a, b] liegen. Der Rückgabewert ist ein boolean.
Erinnerung: geschlossenes Interval bedeutet, das alle Werte inklusive der
Grenzwerte zwischen zwei bestimmten Zahlen einschließt

def check_values(values, interval):
    ...

values = [2, 2.2, 4, 2.3, 0.1]
interval = (1, 5.3)
result = check_values(values, interval)
Result: False  # Nicht alle Werte von values liegen im Interval [1, 5.3]
"""
