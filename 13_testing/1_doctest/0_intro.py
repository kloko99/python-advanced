"""
Beispielmodul mit einfacher Summenfunktion und doctest-Beispielen.

Der Zweck von doctest liegt heute vorrangig im dokumentarischen
Nutzen: Die Beispiele im Docstring zeigen, wie die Funktion
verwendet wird, und können automatisch getestet werden.
"""

import doctest


def summe(a: float, b: float) -> float:
    """
    summe von zwei Floats.

    >>> summe(1, 4)
    5

    >>> summe(0, 0)
    0
    """
    return a + b
