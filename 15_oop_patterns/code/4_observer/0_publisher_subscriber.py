from abc import ABC, abstractmethod


# Observer-Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperatur: float):
        pass


# Konkrete Observer
class KonsoleAnzeige(Observer):
    def update(self, temperatur):
        print(f"[Konsole] Temperatur: {temperatur:.1f}°C")


class AlarmSystem(Observer):
    def update(self, temperatur):
        if temperatur > 30:
            print("[ALARM] Temperatur zu hoch!")


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


# Nutzung
station = Wetterstation()
station.registriere(KonsoleAnzeige())
station.registriere(AlarmSystem())

# station.setze_temperatur(22.5)
station.setze_temperatur(35.0)
