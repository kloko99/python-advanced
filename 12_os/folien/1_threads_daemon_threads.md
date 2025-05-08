# Daemon-Threads in Python

In diesem Tutorial lernst du, was Daemon-Threads in Python sind, wie sie sich von normalen Threads unterscheiden, wie man sie einsetzt und welche Besonderheiten zu beachten sind.

## Was ist ein Daemon-Thread in Python?

Ein **Daemon-Thread** ist ein Hintergrund-Thread, der das Beenden des Python-Programms nicht verhindert. Im Gegensatz dazu sind normale (Nicht-Daemon-)Threads **Foreground-Threads**, die das Programm am Laufen halten, bis sie beendet sind. Der entscheidende Punkt ist: *Das gesamte Python-Programm beendet sich, sobald nur noch Daemon-Threads aktiv sind.* Normale Threads hingegen sorgen dafür, dass das Programm so lange weiterläuft, bis auch sie abgeschlossen sind.

Wichtige Unterschiede zwischen **Daemon-Threads** und **normalen Threads**:

- **Lebensdauer:** Ein Daemon-Thread wird automatisch gestoppt, sobald der Hauptthread (und alle anderen Nicht-Daemon-Threads) beendet ist. Normale Threads lassen das Programm weiterlaufen, bis sie fertig sind.
- **Standardverhalten:** Standardmäßig sind Threads in Python **nicht** als Daemon markiert. Man muss Daemon-Threads also explizit kennzeichnen.
- **Einsatzgebiet:** Daemon-Threads eignen sich für **nicht kritische** Hintergrundaufgaben (z.B. Logging, Monitoring), die keinen Einfluss auf die Hauptlogik haben.

## Beispiel 1: Einfache Statusmeldung

```python
import threading
import time

def log_status():
    while True:
        print("Logger: System läuft noch...")
        time.sleep(2)

# Daemon-Thread erstellen und als Daemon markieren
daemon_thread = threading.Thread(target=log_status, daemon=True)
daemon_thread.start()

print("Haupt-Thread: Starte Hauptaufgabe...")
time.sleep(5)
print("Haupt-Thread: Erledigt.")
```

**Erwartetes Verhalten:** Das Programm endet nach 5 Sekunden, obwohl der Daemon-Thread eine Endlosschleife hat. Der Hintergrundthread wird automatisch gestoppt.

## Beispiel 2: Regelmäßige Dateiprüfung im Hintergrund

```python
import threading
import time
import os

def check_file():
    while True:
        if os.path.exists("/tmp/trigger.txt"):
            print("Datei gefunden! Aktion auslösen...")
        else:
            print("Warte auf Datei...")
        time.sleep(3)

watcher = threading.Thread(target=check_file, daemon=True)
watcher.start()

print("Haupt-Thread: Arbeite 10 Sekunden lang...")
time.sleep(10)
print("Haupt-Thread: Fertig.")
```

**Hinweis:** Die Datei "/tmp/trigger.txt" kann man während der Laufzeit manuell anlegen, um die Reaktion zu testen.

## Starten und Beenden

1. **Thread-Objekt anlegen:** z.B. `t = threading.Thread(target=func, daemon=True)`  
2. **Daemon-Flag setzen:** entweder im Konstruktor oder per `t.daemon = True` vor `t.start()`  
3. **Thread starten:** `t.start()`

Sobald der Hauptthread beendet ist, werden alle Daemon-Threads automatisch beendet.

## Wichtige Hinweise

- **Abruptes Stoppen:** Daemon-Threads werden ohne Vorwarnung gestoppt. `try/finally`-Blöcke oder Aufräumarbeiten werden dabei ignoriert.
- **Keine garantierte Fertigstellung:** Daemon-Threads sind nicht geeignet für Aufgaben, die sicher abgeschlossen werden müssen (z.B. Datei schreiben).
- **Für nicht-kritische Aufgaben nutzen:** Ideal für Logging, periodische Checks, Monitoring etc.
- **Für kontrollierbare Beendigung:** Nutze normale Threads mit Abbruch-Logik (z.B. mittels `threading.Event`).

## Fazit

Daemon-Threads eignen sich hervorragend für einfache Hintergrundaufgaben, die das Programm nicht blockieren sollen. Sie müssen jedoch mit Vorsicht verwendet werden, da sie beim Programmende sofort beendet werden und dabei keine Aufräumarbeiten mehr durchführen können.

