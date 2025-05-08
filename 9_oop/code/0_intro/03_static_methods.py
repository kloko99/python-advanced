"""
Thema: Statische Methoden in Python – @staticmethod

Statische Methoden gehören zur Klasse, nicht zur Instanz. Sie werden
mit dem Decorator @staticmethod gekennzeichnet und benötigen weder
self noch cls als ersten Parameter.

Sie können wie normale Funktionen definiert werden, sind aber zur
besseren Strukturierung an die Klasse gebunden – z. B. für Hilfsfunktionen,
die logisch zur Klasse gehören, aber keinen Zugriff auf Instanz- oder
Klassendaten benötigen.

Aufruf: direkt über Klasse oder Instanz möglich (Klasse.methode()).
"""
class TemperaturRechner:
    """Utility Klasse für Temperaturumrechnungen."""

    @staticmethod
    def celsius_to_fahrenheit(grad: float):
        pass


# statische Methoden
TemperaturRechner.celsius_to_fahrenheit(34.2)