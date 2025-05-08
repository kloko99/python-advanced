"""
ERstelle ein Programm, das Dateien in verschiedenen Formaten (CSV und JSON) lesen und die Daten daraus extrahieren kann.

Hierfür wird das Factory-Muster verwendet, um den passenden Datei-Reader entsprechend des Dateiformats zu erstellen. Bisher gibt es nur zwei Reader, es könnten aber später noch mehr Reader dazukommmen (zb. API Reader, Text Reader etc.)

Anforderungen:

    Erstelle vier Klassen:
        FileReader (abstrakte Klasse, implementiert abstrakte Methode read())
        CSVReader (erbt von FileReader)
        JSONReader (erbt von FileReader)
        ReaderFactory (erzeugt einen FileReader, zb. CSVReader)

    Die CSVReader-Klasse sollte eine Methode read implementieren, die eine CSV-Datei öffnet, deren Inhalt liest und in Form einer Liste von Dictionaries speichert. Jedes Dictionary entspricht einer Zeile der CSV-Datei, wobei die Spaltennamen als Schlüssel und die Zellwerte als Werte im Dictionary verwendet werden.

    Die JSONReader-Klasse sollte eine Methode read implementieren, die eine JSON-Datei öffnet, deren Inhalt liest und in Form eines Python-Dictionaries speichert.

    Die ReaderFactory-Klasse sollte eine Methode create_reader bereitstellen, die abhängig vom angegebenen Dateiformat ("csv" oder "json") einen entsprechenden Datei-Reader erstellt und zurückgibt. Wenn ein unbekanntes Dateiformat angegeben wird, wird ein NotImplementedError ausgelöst.

    Nutze das Factory-Pattern und ABC für die Aufgabe


    Beispiel:
    factory = ReaderFactory()
    file_type = "csv"
    reader = factory.create_reader(file_type)
    data = reader.read("testdaten.csv")

    Die Klassen müssen nicht FUNKTIONIEREN! Es soll nur die Struktur aufgezeigt werden.
    """
