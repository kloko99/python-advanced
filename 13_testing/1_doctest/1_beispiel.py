"""
Beispiel für die Verwendung von doctest anhand
einer Transponierungsmatrix.
"""

import doctest


def transpose(matrix: list) -> list:
    """.....docstring mit doctest hier."""
    mT = [row for row in zip(*matrix)]
    return mT


m = [[1, 2], [3, 4]]
m = transpose(m)

if __name__ == "__main__":
    # schlägt fehl, wenn Fehler im Code
    doctest.testmod()
