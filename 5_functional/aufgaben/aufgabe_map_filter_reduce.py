"""
(SCHWER)
Gegeben ist folgendes Programm in klassischer Python-Schreibweise:

people = [
    {"name": "Foo", "height": 160},
    {"name": "Bar", "height": 180},
    {"name": "Baz", "height": 80},
    {"name": "Grumpy", "height": 80},
    {"name": "Waldo"},
]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print(average_height)

Formuliere das Programm mit den Pythonfunktionen map, filter und reduce
Hilfreich könnte das Modul operator sein, in dem sich die Python-Operatoren befinden

import operator

operator.add(3, 5) # 8
"""
from functools import reduce
import operator

people = [
    {"name": "Foo", "height": 160},
    {"name": "Bar", "height": 180},
    {"name": "Baz", "height": 80},
    {"name": "Grumpy", "height": 80},
    {"name": "Waldo"},
]

x = operator.add(3, 5)
print(x)
