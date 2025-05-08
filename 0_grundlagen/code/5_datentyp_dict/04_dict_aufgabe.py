"""
(LEICHT)
Gegeben sind zwei Listen:


geraete = ["Kühlschrank", "Fernseher", "Waschmaschine", "Laptop"]
stromverbrauch = ["1.2", "0.3", "2.0", "0.05"]  # Angaben in kWh

Erstelle ein Dict, wobei der Key der Gerätename ist und der Value der entsprechende Verbrauch.
Konvertiere die Werte aus stromverbrauch dazu vorab in floats.

Das neue Dict soll nur Geräte beinhalten, deren Stromverbrauch >= 0.2 kWh

Ergebnis:
{
'Fernseher': 0.3,
 'Kühlschrank': 1.2,
 'Waschmaschine': 2.0
 }

"""

geraete = ["Kühlschrank", "Fernseher", "Waschmaschine", "Laptop"]
stromverbrauch = ["1.2", "0.3", "2.0", "0.05"]  # Angaben in kWh
