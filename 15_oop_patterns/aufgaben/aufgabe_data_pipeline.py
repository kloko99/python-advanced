"""
Du hast einen Datensatz mit Kundendaten und möchtst eine Datenverarbeitungspipeline erstellen, die die folgenden Schritte enthält:

    Daten laden: Lade die Rohdaten aus einer CSV-Datei in eine Liste von Dicts.
    Daten bereinigen: Entferne Datensätze, mit fehlendem Gewicht und BMI
    Daten transformieren: Konvertiere Gewicht nach float und BMI nach int.
    Daten speichern: Speichere die verarbeiteten Daten in einer CSV-Datei

Die Aufgabe ist es, eine Datenverarbeitungspipeline mit dem Builder-Pattern zu erstellen.


Gegebenes Grundgerüst der Pipeline:

class DataProcessingPipeline:
    def __init__(self):
        self.data = None

    def load_data(self, filename):
        # Hier könnte Logik zum Laden der Daten implementiert werden
        self.data = LADEN

        return self

    def clean_data(self):
        # Hier könnte Logik zur Datenbereinigung implementiert werden
        if self.data is not None:
            # Beispiel: Entferne Datensätze mit fehlenden Werten

    def transform_data(self):
        # Hier könnte Logik zur Datenmanipulation implementiert werden


    def save_data(self, output_file):
        # Hier könnte Logik zum Speichern der Daten implementiert werden


    def build(self):
        return self


Aufruf der Pipeline:

pipeline = (
    DataProcessingPipeline()
    .load_data(filename="testdaten.csv")
    .clean_data()
    .transform_data()
    .analyze_data()
    .save_data('processed_data.txt')
    .build()
)



"""
