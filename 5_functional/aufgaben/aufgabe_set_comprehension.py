"""
Aufgab Set-Comprehension «Hashtags sammeln»

Schreibe die Funktion unique_hashtags(text), die alle unterschiedlichen
Hashtags (#wort) aus einem Text als Set in Kleinbuchstaben zurückgibt –
mithilfe **einer einzigen Set‑Comprehension**.  Ein Hashtag endet am
ersten Nicht‑Buchstaben/Ziffer/Unterstrich.

Beispiel:

    txt = "Lerne #Python! #coding, #python_rocks und mehr."
    print(unique_hashtags(txt))   # {'python', 'coding', 'python_rocks'}

zum Hastags finden bietet sich die Methode findall aus dem re-Modul an
re.findall(r"#(\w+)", text)
"""

import re
