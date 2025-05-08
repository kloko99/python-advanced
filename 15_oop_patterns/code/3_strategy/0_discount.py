"""
# Strategy Pattern

Strategie ist im Bereich der Softwareentwicklung ein Entwurfsmuster und gehört
zur Kategorie der Verhaltensmuster. Die Strategie definiert eine Familie
austauschbarer Algorithmen. Es ist eines der sogenannten GoF-Muster.

Die Klasse Strategie definiert nur eine Schnittstelle (interface)
für alle unterstützten Algorithmen. Die Implementierung der eigentlichen
Algorithmen finden sich erst in den Ableitungen wieder (konkrete Strategie).


Als Beispiel kann ein Discountberechnungsprogramm dienen, das die
Berechnung der Discounts möglichst in Strategie-Objekte auslagern sollte,
um einfach saisonabhängig konfigurierbar zu sein.
"""

import abc
import enum


class Discounts(enum.Enum):
    DEFAULT = 1.0
    SUMMER = 0.1
    WINTER = 0.14
