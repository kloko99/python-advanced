"""
Aufgabe Summen pro Kategorie mit itertools

CSV‑Datei expenses.csv:

    date,description,category,amount
    2025‑05‑01,Coffee,Food,3.20
    2025‑05‑01,Sandwich,Food,4.80
    2025‑05‑02,Bus ticket,Transport,2.80
    …

Schreibe die Funktion totals(path: str) → dict[str, float], die

1. die Datei zeilenweise (csv.reader) einliest,
2. die Einträge **vor** dem Gruppieren nach category sortiert,
3. mithilfe von itertools.groupby jede Gruppe summiert,
4. ein Dict {Kategorie: Gesamtausgaben} zurückgibt.

Hinweis‑Snippet für Schritt 3:

    import itertools
    rows = sorted(rows, key=lambda r: r["category"].lower())
    result = {cat: sum(float(r["amount"]) for r in grp)
              for cat, grp in itertools.groupby(
                      rows, key=lambda r: r["category"].lower())}

Benutze nur die Standard‑Bibliothek.

Lösung:
{'food': 16.0, 'leisure': 10.0, 'transport': 18.3}
"""

import itertools
import csv
from pathlib import Path
