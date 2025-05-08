"""
Aufgabe (MITTEL), nutze map und filter
1. Rechne Temperaturliste von Celsius in Fahrenheit um
2. Filtere Einträge > THRESHOLD_FAHRENHEIT
3. Gebe den tiefsten Wert in Grad Fahrenheit sowie Grad Celsius an
"""

THRESHOLD_FAHRENHEIT = 77

def celsius_to_fahrenheit(celsius):
    """REchne Grad Celsius nach Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Beispiel Sensordaten (Temperaturwerte in Celsius)
sensor_data_celsius = [22, 24, 26, 28, 32, 35, 40, 18, 15, 42, 27, 30]

filtered_data= list(filter(lambda x: x > THRESHOLD_FAHRENHEIT, 
                      map(celsius_to_fahrenheit, sensor_data_celsius)))

lowest_value = min(filtered_data)
print(f"Der tiefste Wert ist: {lowest_value}° Fahrenheit, {fahrenheit_to_celsius(lowest_value)}° Celsius")
