"""
Implementiere den Floodfill Algorithmus,
fill4 (4-connected)
https://en.wikipedia.org/wiki/Flood_fill

before:

m = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

after start at (1 / 6) with fill color 2:
x = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 2, 2, 1],
    [1, 0, 0, 0, 1, 2, 2, 2, 1],
    [1, 0, 0, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 2, 2, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 1, 0, 0, 1],
    [1, 2, 2, 2, 1, 0, 0, 0, 1],
    [1, 2, 2, 2, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]]

"""

from pprint import pprint
from typing import Literal

color = Literal[0, 1, 2]
Matrix = list[list[color]]
beige: color = 2
black: color = 1
white: color = 0


m = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def fill4(m: Matrix, x: int, y: int, old: color, new: color):
    """Implemenation of Floodfill Algorithm.

    Args:
        m: Matrix: 2 dim numerical matrix as Canvas
        x: X-Coordiate of start pixel
        y: y-Cooordinate of start pixel
        old: old color which has to be replaced
        new: new replacing color

    Returns:
        None
    """
    ...


def main():
    fill4(m, x=4, y=4, old=white, new=beige)
    pprint(m)
