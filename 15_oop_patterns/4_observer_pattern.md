# Observer Pattern in Python

## Was ist das Observer Pattern?

Ein **Subject** (Beobachtetes Objekt) informiert automatisch alle 
registrierten **Observer** (Beobachter), wenn sich sein Zustand ändert.

---

## Ziel

- **Lose Kopplung** zwischen Sender und Empfängern
- **Mehrere Listener**, die auf Änderungen reagieren
- Reaktiv statt imperativ

---

## Beispiel: Wetterstation → Anzeige-Module

```python
from abc import ABC, abstractmethod

# Observer-Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperatur: float):
        pass

# Subject
class Wetterstation:
    def __init__(self):
        self._beobachter = []
        self._temperatur = 0.0

    def registriere(self, observer: Observer):
        self._beobachter.append(observer)

    def entferne(self, observer: Observer):
        self._beobachter.remove(observer)

    def _benachrichtige(self):
        for o in self._beobachter:
            o.update(self._temperatur)

    def setze_temperatur(self, wert: float):
        self._temperatur = wert
        self._benachrichtige()

# Konkrete Observer
class KonsoleAnzeige(Observer):
    def update(self, temperatur):
        print(f"[Konsole] Temperatur: {temperatur:.1f}°C")

class AlarmSystem(Observer):
    def update(self, temperatur):
        if temperatur > 30:
            print("[ALARM] Temperatur zu hoch!")

# Nutzung
station = Wetterstation()
station.registriere(KonsoleAnzeige())
station.registriere(AlarmSystem())

station.setze_temperatur(22.5)
station.setze_temperatur(35.0)
```

---

## Vorteile

- Subsysteme bleiben unabhängig
- Beliebig viele Listener möglich
- Dynamische Reaktion auf Ereignisse

---

## Typische Anwendungen

- GUI-Elemente (z. B. Buttons, Events)
- Event-Systeme / Signals (z. B. Django Signals, PyQt Signals)
- Datenänderungen in Modellen

---

## Fazit

Das Observer Pattern ist ideal für **Event-gesteuerte Architekturen**. Besonders nützlich, wenn mehrere Komponenten auf denselben Zustand reagieren müssen.
```

Willst du auch ein Beispiel mit `async`, GUI (z. B. PySide), oder `property` als Trigger?
