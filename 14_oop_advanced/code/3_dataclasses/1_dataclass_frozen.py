"""
Thema: frozen=True in @dataclass – Unveränderliche Objekte erzeugen

Mit dem Parameter `frozen=True` bei der Dekoration einer Datenklasse
(`@dataclass`) wird die Klasse **unveränderlich** (engl. *immutable*).

Das bedeutet:
- Nach der Instanziierung können keine Attribute mehr verändert werden.
- Jeder Versuch, ein Attribut neu zu setzen oder zu überschreiben,
  führt zu einem `FrozenInstanceError`.

Beispiel:

    @dataclass(frozen=True)
    class Point:
        x: int
        y: int

    p = Point(1, 2)
    p.x = 10  # ❌ ergibt FrozenInstanceError

Dies ist besonders nützlich:
- wenn Objekte als Dictionary-Keys oder in Sets verwendet werden sollen
- zur Fehlervermeidung bei versehentlichen Änderungen
- bei funktionalem Programmierstil

Hinweis: frozen=True erzeugt automatisch eine `__hash__`-Methode,
wenn möglich – z. B. wenn alle Felder selbst hashbar sind.
"""

from dataclasses import dataclass, asdict, field


RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


@dataclass(frozen=True)
class DataclassCard:
    rank: str
    suit: str


@dataclass(frozen=True)
class ImmutableDeck:
    cards: list[DataclassCard] = field(default_factory=list)


def make_french_deck() -> list[DataclassCard]:
    """Generiere French Deck als Liste von DataclassCards."""
    return [DataclassCard(r, s) for s in SUITS for r in RANKS]


# Kartensatz erstellen
deck = ImmutableDeck(make_french_deck())
deck.cards.append(DataclassCard("32", "♡"))

print(deck)

# Tupel-Element an Index 1 ist eine Liste und damit veränderlich
x = (2, [3, 2])
print(type(x))
x[1].append(42)
print(x)
