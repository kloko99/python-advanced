"""
Thema: namedtuple – Alternative zu @dataclass(frozen=True)

Wenn man eine einfache, unveränderliche Datenstruktur benötigt,
kann `collections.namedtuple` eine kompakte Alternative zur
`@dataclass(frozen=True)` sein.

Ein `namedtuple`:
- ist eine speichereffiziente Unterklasse von `tuple`
- ist **unveränderlich**
- erlaubt Zugriff über Feldnamen wie bei einer Klasse
- ist vergleichbar und hashbar

Beispiel:

    from collections import namedtuple

    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    print(p.x)       # ✅ 1
    print(p == (1,2))  # ✅ True
    p.x = 10         # ❌ AttributeError (unveränderlich)

Unterschiede zur frozen dataclass:
- `namedtuple` ist kompakter, aber weniger flexibel
- keine Typannotationen, keine `__post_init__`
- keine Feldoptionen wie `default`, `compare=False` usw.

Fazit:
- Ideal für kleine, schnelle, immutable Objekte
- Wenn mehr Logik, Validierung oder Feldauswahl nötig ist,
  ist `@dataclass(frozen=True)` die bessere Wahl
"""
