"""
Ab Python 3.10 kann anstelle des fehlenden Switch-Cases
das Structural Pattern Matching verwendet werden.
Pattern Matching ist allerdings sehr viel mächtiger als das herkömmliche
Switch-Case.

Schema:
match expression:
    case pattern1: # do something
    case pattern2: # do something else
"""

# Oldschool: Bedingte Verarbeitung mit if/elif/else
weekday = 1
if weekday == 1:
    weekday_name = "Monday"
elif weekday == 2:
    weekday_name = "Tuesday"
else:
    weekday_name = "undefined"

print(weekday_name)

# Pattern Matching: Vereinfachung durch match/case

# Pattern Matching mit Listen
name = "Captain Jean Luc"


# Pattern Matching mit benutzerdefinierten Zeichenfolgen
input_string = "+ 3 3"

# Pattern Matching mit Dictionaries
orders = [
    {"type": "book", "title": "1984", "author": "George Orwell"},
    {"type": "electronics", "product": "smartphone", "brand": "Acme"},
    {"type": "grocery", "items": ["milk", "bread"], "quantities": [3, 4]},
]
