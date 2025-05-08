"""
Protokolle:
pythonische Art, Interfaces umzusetzen.
Allerdings nur für die statische CodeAnalyse mit mypy oder pyright.
"""

from typing import Protocol
from collections.abc import Sequence


class Reader(Protocol):
    def read(self): ...


class Flyer(Protocol):
    """Flyer Prtocol sagt aus, dass fly und walk implementiert sein muss."""

    def fly(self): ...

    def walk(self): ...


class SuperHero:
    def fly(self):
        print("Hero can fly")

    def walk(self):
        print("Hero can walk,")


class BoardGame:
    def make_fly(self, player: Flyer):
        """Erwartet ein Objekt, dass das Flyer-Protokoll unterstützt."""
        print(player.fly())
        print(player.walk())


b = BoardGame()
b.make_fly(SuperHero())


def get_list(values: Sequence):
    """Erwartet eine Sequenz: liste, tuple, deque..."""
    pass


get_list([2, 3])
get_list("hallo")
