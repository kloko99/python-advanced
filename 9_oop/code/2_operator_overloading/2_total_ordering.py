"""
Thema: functools.total_ordering – vollständige Vergleichsoperatoren

Mit dem Decorator @total_ordering aus dem Modul functools kann man
alle sechs Vergleichsoperatoren (__lt__, __le__, __gt__, __ge__,
__eq__, __ne__) ableiten, wenn man nur __eq__ und einer der anderen
(__lt__, __le__, __gt__ oder __ge__) implementiert.

Das spart Code und erhöht die Lesbarkeit, besonders bei Klassen mit
klarer Vergleichslogik.
"""

import functools
