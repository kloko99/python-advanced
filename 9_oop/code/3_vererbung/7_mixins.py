"""
Thema: Mixins in Python – Mehrfachvererbung gezielt nutzen

Ein Mixin ist eine Klasse, die **zusätzliche Funktionalität** liefert,
aber **nicht eigenständig instanziiert** wird. Sie wird verwendet, um
Fähigkeiten per Mehrfachvererbung modular zu anderen Klassen hinzuzufügen.

Eigenschaften von Mixins:
- Kein eigener Konstruktor (normalerweise kein __init__)
- Klein, fokussiert und wiederverwendbar
- Wird zusammen mit einer Hauptklasse geerbt

Typische Anwendungsbeispiele:
- LoggingMixin → bietet Logging-Funktion
- JsonSerializableMixin → bietet to_json()-Methode
- TimestampMixin → fügt Erstellungszeitpunkt hinzu

Mixins fördern saubere, modulare Architekturen – besonders in komplexeren
Systemen wie Web-Frameworks oder Datenmodellen.
"""

class CSVExporter:
    """Ist nicht dazu gedacht, als eigene Instanz genutzt werden.
    Sondern nur als Mixin."""
    def csv_export(self):
        """Simuliere CSV-Export."""
        print(self.data)


class JSONExporter:
    def json_export(self):
        """Simuliere JSON-Export."""
        print(self.data)


class DataManager(CSVExporter, JSONExporter):
    """Sammelt Daten für den Einkauf."""

    def __init__(self) -> None:
        self.data = []

    def collect_data(self, data):
        """Methode um Daten zur Sammlung hinzufügen."""
        self.data.extend(data)
    
    def view(self):
        print(self.data)

    

d = DataManager()
d.collect_data([1, 2, 3, 45])
d.csv_export()  # CSV Export