"""
Vergleich normale Klasse vs Dataclass
"""

from dataclasses import dataclass, asdict


class RegularCard:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit


queen_of_hearts = RegularCard(rank="Q", suit="Hearts")
queen_of_hearts2 = RegularCard(rank="Q", suit="Hearts")

print(queen_of_hearts == queen_of_hearts2)

###############################################################
# Bei DAtenclassen ist __repr__ schon vorimplemtiert


@dataclass
class DataclassCard:
    rank: str
    suit: str


q1 = DataclassCard(rank="Q", suit="Hearts")
q2 = DataclassCard(rank="Q", suit="Hearts")

print(q1)  # DataclassCard(rank='Q', suit='Hearts')
print(q1 == q2)


# Datenclass Objekt als Dict exportieren
q1_dict = asdict(q1)
print(q1_dict)  # {'rank': 'Q', 'suit': 'Hearts'}
