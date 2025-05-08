"""
Thema: __init_subclass__ – automatische Prüfung bei Vererbung

Die Methode __init_subclass__ ist ein spezieller Hook in Python, der
automatisch aufgerufen wird, **wenn eine Klasse von einer anderen Klasse
erbt**.

Damit lassen sich z. B. Prüfungen oder Vorgaben in einer Basisklasse
definieren, die jede Unterklasse automatisch erfüllen muss – ohne dass
eine separate Metaklasse nötig ist.

Typische Einsatzgebiete:
- Validierung von Attributen (z. B. Pflichtattribute wie _filename)
- Registrieren von Subklassen
- Konfiguration und Logging beim Vererben

Vorteile gegenüber Metaklassen:
- Leichter einzusetzen
- Besser lesbar
- Keine Kollision mit anderen Metaklassen in Frameworks

__init_subclass__ wird mit cls als erstem Argument aufgerufen:
    def __init_subclass__(cls, **kwargs):
        ...

So kann jede Subklasse direkt beim Definieren geprüft oder verändert
werden.
"""


class TradingStrategy:
    pass
