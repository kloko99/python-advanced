"""
Thema: order=True in @dataclass – Vergleichbare Objekte erstellen

Mit dem Parameter `order=True` kann eine Datenklasse automatisch
Vergleichsmethoden erhalten. Dadurch werden Objekte dieser Klasse
nach ihren Feldern **in der Reihenfolge ihrer Definition** vergleichbar.

Folgende Vergleichsmethoden werden dann generiert:
- __lt__ (kleiner als)
- __le__ (kleiner gleich)
- __gt__ (größer als)
- __ge__ (größer gleich)

Voraussetzung:
- Die Felder der Klasse selbst müssen vergleichbar sein (z. B. int, str).

Reihenfolge:
- Der Vergleich erfolgt feldweise von oben nach unten – also in der
  Reihenfolge der Felddefinition.
- Möchte man bestimmte Felder **höher gewichten**, stellt man sie weiter
  oben in der Klasse ein.

Felder ausschließen:
- Einzelne Felder können mit `field(compare=False)` **vom Vergleich
  ausgeschlossen** werden.

Beispiel:

    from dataclasses import dataclass, field

    @dataclass(order=True)
    class Product:
        price: float
        name: str = field(compare=False)

    p1 = Product(10.0, "Buch")
    p2 = Product(15.0, "Stift")
    print(p1 < p2)  # ✅ True, nur price wird verglichen

Wichtig:
- `order=True` setzt voraus, dass auch `eq=True` aktiv ist (Standard).
- Vergleichbarkeit macht Klassen sortierbar und einsatzbereit in Sets,
  Listen, Priority Queues usw.
"""
