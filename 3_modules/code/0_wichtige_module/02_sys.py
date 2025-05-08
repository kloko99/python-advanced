"""
Das Thema dieser Datei ist das `sys`-Modul in Python.

- Das `sys`-Modul bietet Zugriff auf Funktionen und Parameter, die sich auf den
  Python-Interpreter und die Laufzeitumgebung beziehen.
- Es ermöglicht das Arbeiten mit Kommandozeilenargumenten, das Anpassen
  des Suchpfads für Module, die Steuerung der Standard-Ein- und Ausgabe
  sowie das Beenden des Programms.
"""

# Importieren des sys-Moduls
import sys

# 1. Kommandozeilenargumente
# `sys.argv` ist eine Liste, die die Kommandozeilenargumente enthält.
# Das erste Element ist der Name des Skripts.

# Aufgabe:
# Erstelle ein Skript, das die Argumente verarbeitet und z. B. eine Nachricht ausgibt.

# 2. Python-Version
# Gibt die aktuelle Version des Python-Interpreters zurück.

# 3. Beenden des Programms
# sys.exit("Beenden mit Nachricht")  # Beendet das Programm mit einer Nachricht.
# Hinweis: Kommentiert, um die weitere Ausführung dieses Skripts nicht zu verhindern.


# 5. Modul-Suchpfad
# `sys.path` ist eine Liste, die die Verzeichnisse enthält, in denen Python nach Modulen sucht.
# Aufgabe:
# Füge ein Verzeichnis hinzu und importiere ein Modul daraus.
# Beispiel: sys.path.append("/pfad/zu/meinem/modul")

# 6. Informationen zur Plattform
# Gibt die Plattform zurück, auf der Python läuft (z. B. 'win32', 'linux', 'darwin').

# 7. Maximale Rekursionstiefe
# Setzen einer neuen Rekursionstiefe (mit Vorsicht zu verwenden!)


# 8. Speicherinformationen
# `sys.getsizeof` gibt die Größe eines Objekts in Bytes zurück.
