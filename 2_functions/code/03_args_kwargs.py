"""
Das Thema dieser Datei ist `*args`, `**kwargs` und Default-Parameter.
- `*args` erlaubt eine unbestimmte Anzahl an positionsbasierten Argumenten.
- `**kwargs` erlaubt eine unbestimmte Anzahl an keywordbasierten Argumenten.
- Default-Parameter können standardisierte Werte festlegen, die verwendet
  werden, wenn kein Argument übergeben wird.
"""

# Definition einer Funktion mit `*args`

# Beispielaufruf der Funktion

# Definition einer Funktion mit `**kwargs`

# Beispielaufruf der Funktion


# Kombination von `*args`, `**kwargs` und Default-Parametern


def introduce_person():
    """Stellt eine Person mit Begrüßung, Namen und Attributen vor."""


# Beispielaufruf der Funktion
introduce_person("Hi", "Max", "Muster", age=25, city="München")


# Definition einer Funktion mit mehreren Default-Parametern


def configure_device():
    """Konfiguriert ein Gerät mit einem Modus und einer Leistung."""


# Beispielaufruf der Funktion
configure_device("Sensor X")
configure_device("Sensor Y", mode="manual", power=75)
