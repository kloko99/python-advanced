"""
(leicht)
Gegben ist ein Dict mit Städtenamen und den dazugehörigen Einwohner:

population = {
    'Berlin': 3748148,
    'Hamburg': 1822445,
    'München': 1471508,
    'Cologne': 1085664,
    'Frankfurt': 753056
}

1.) Erstelle eine neues Dict, welches die Einwohner in Millionen abbildet 


{'Berlin': 3.748148, 'Hamburg': 1.822445, 'München': 1.471508, 'Cologne': 1.085664, 'Frankfurt': 0.753056}

2.) Gebe das neue Dict aus und formatiere auf eine Nachkommastelle.

Berlin hat 3.7 Mil. Einwohner
Hamburg hat 1.8 Mil. Einwohner
München hat 1.5 Mil. Einwohner
Cologne hat 1.1 Mil. Einwohner
Frankfurt hat 0.8 Mil. Einwohner

"""

populations = {
    'Berlin': 3748148,
    'Hamburg': 1822445,
    'München': 1471508,
    'Cologne': 1085664,
    'Frankfurt': 753056
}

populations_mil = {}

