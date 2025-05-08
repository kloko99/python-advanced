"""
Thema: Vererbung in der Praxis – Parser-Struktur für Dateiformate

In vielen Anwendungen müssen unterschiedliche Dateiformate analysiert
werden (z. B. JSON, CSV, XML). Dabei folgt die Verarbeitung oft einem
ähnlichen Schema: Datei einlesen, parsen, in ein gemeinsames Format
überführen.

Durch Vererbung kann man eine gemeinsame Basisklasse Parser definieren,
die das Grundgerüst vorgibt, und spezifische Parserklassen für jedes
Format ableiten.
"""

from pathlib import Path
import json
import csv

DATA_DIR = Path(__file__).parent


class Parser:
    """Basisklasse, die grundlegende funktionen bereitstellt."""
    def __init__(self, path):
        self.path = path

    def parse(self):
        raise NotImplementedError("Basisparser kann nichts parsen.")

    def __str__(self):
        return f"{self.__class__.__name__} / {self.path}"


class JsonParser(Parser):
    """Spezialfall eines Parsers."""

    def parse(self):
        """Öffne Json-Datei und lese aus."""
        with open(DATA_DIR / self.path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
        return data


json_parser = JsonParser(path="daten.json")
daten = json_parser.parse()
print(daten)
print(json_parser)