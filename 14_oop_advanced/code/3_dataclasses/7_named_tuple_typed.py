"""
Thema: typing.NamedTuple – getypte, unveränderliche Datenstruktur

Die Klasse `typing.NamedTuple` ist eine moderne Variante von
`collections.namedtuple`, die Typhinweise erlaubt und sich
wie eine Kombination aus `tuple` und `@dataclass(frozen=True)` verhält.

Eigenschaften:
- unveränderlich (immutable)
- speichereffizient wie tuple
- typisierbar dank Type Hints
- erzeugt automatisch __init__, __repr__, __eq__, __hash__

Einsatzbereich:
- kleine, strukturierte Datenobjekte
- lesbarer Ersatz für rohe Tupel
- stabile Objekte für Dictionaries, Sets oder als Rückgabewerte

Beispiel: Rechnungsdatensatz mit UUID und Preis
"""

from typing import NamedTuple


class Invoice(NamedTuple):
    uuid: str
    price: float


# --- Beispiel für Liste von NamedTuples ---
invoices = [
    Invoice("INV-001", 99.99),
    Invoice("INV-002", 149.00),
    Invoice("INV-003", 219.50),
]

# Summieren aller Preise
total = sum(inv.price for inv in invoices)
print(f"Gesamtsumme: {total:.2f} €")

print(invoices)

invoice = invoices.pop()
print(invoice[1], invoice.price)

# NameTuple ist auch ein tuple
print(isinstance(invoice, tuple))
