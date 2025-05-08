"""
Dieses Modul gibt eine Einführung in die Verwendung der Loguru-Bibliothek,
einem modernen und einfach zu verwendenden Logging-Tool für Python.

`loguru` ersetzt das umständlichere `logging`-Modul durch:
- sofortige Benutzung (kein Setup nötig)
- strukturierte Logs mit Farben, Zeit, Leveln
- einfache Dateiausgabe, Rotation und Filter
- automatische Exception-Logger

Installation:
    pip install loguru

Dieses Beispiel zeigt das Logging in Konsole, in Dateien, mit Levelsteuerung
und Fehlerbehandlung.
"""

from loguru import logger

# ---------------------------------------------
# Einfaches Logging mit verschiedenen Levels
# ---------------------------------------------
logger.debug("Das ist ein Debug-Log")
logger.info("Info: alles läuft")
logger.warning("Warnung: etwas ist suboptimal")
logger.error("Fehler: Ausnahme aufgetreten")
logger.critical("Kritisch: Systemproblem")

# ---------------------------------------------
# Ausgabe in Datei mit Rotation ab 500 KB
# ---------------------------------------------
logger.add(
    "logfile.log", format="{time} {level} {message}", rotation="500 KB", level="INFO"
)
logger.info("Diese Nachricht geht in die Datei")

# ---------------------------------------------
# Logging mit Format und Filter
# ---------------------------------------------
logger.add("app.log", format="{time} {level} {message}", level="INFO")
logger.info("Wird geloggt, da Filter passt")


# ---------------------------------------------
# Exceptions automatisch loggen
# ---------------------------------------------
@logger.catch
def div_by_zero():
    1 / 0


div_by_zero()  # auskommentiert für Sicherheit
