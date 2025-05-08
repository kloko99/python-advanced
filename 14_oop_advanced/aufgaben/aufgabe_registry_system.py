"""
Aufgabe: Automatische Registrierung von Konfigurationsklassen

Implementiere eine Metaklasse, die beim Erzeugen einer Klasse prüft,
ob die Attribute 'name', 'version' und 'settings' vorhanden sind und
die Typen korrekt sind. Die Klassen sollen automatisch in einer
Registry gespeichert werden, ohne dass der Nutzer explizit Code zur
Registrierung schreiben muss. Die Basisklasse 'BaseConfig' kapselt
die Metaklasse und bietet Zugriff auf alle registrierten Klassen
über 'BaseConfig.all()' und 'BaseConfig.get(name)'.

name: str
version: str
settings: dict
"""


class ConfigMeta(type):
    def __init__(cls, name, bases, dct):
        # Wenn die ConfigMeta-Klasse noch keine _registry hat,
        # muss diese als leeres Dict angelegt werden
        # if not hasattr(cls, "_registry"):
        # cls._registry = {}

        # Wenn es sich nicht um die BaseConfig handelt,
        # Prüfung der Attribute vornehmen, falls nicht vorhanden,
        # TypeError werfen
        # elif cls.__name__ != "BaseConfig":
        #    required_fields = ['name', 'version', 'settings']
        #    for field in required_fields:

        # Datentypen der Felder müssen aufgeprüft werden
        # if not isinstance(cls.name, str):
        #     raise TypeError("'name' muss ein str sein.")

        # Wenn Prüfung erfolgreich, Registrierung bei der Basisklasse
        # cls._registry[cls.name] = cls

        # Superklasse initialisieren
        # super().__init__(name, bases, dct)


class ConfigMeta(type):
    def __init__(cls, name, bases, dct):
        # Basisklasse initialisieren, aber nicht registrieren
        if not hasattr(cls, "_registry"):
            cls._registry = {}

        elif cls.__name__ != "BaseConfig":
            required_fields = ['name', 'version', 'settings']
            for field in required_fields:
                if not hasattr(cls, field):
                    raise TypeError(f"{cls.__name__} muss das Attribut '{
                                    field}' definieren.")

            if not isinstance(cls.name, str):
                raise TypeError("'name' muss ein str sein.")
            if not isinstance(cls.version, str):
                raise TypeError("'version' muss ein str sein.")
            if not isinstance(cls.settings, dict):
                raise TypeError("'settings' muss ein dict sein.")

            # Registrierung bei der Basisklasse
            cls._registry[cls.name] = cls

        super().__init__(name, bases, dct)


class BaseConfig(metaclass=ConfigMeta):
    @classmethod
    def all(cls):
        return list(cls._registry.values())

    @classmethod
    def get(cls, name):
        return cls._registry.get(name)


class LoggingConfig(BaseConfig):
    name = "logging"
    version = "2.1"
    settings = {"level": "debug", "output": "stdout"}


class CacheConfig(BaseConfig):
    name = "cache"
    version = "1.0"
    settings = {"size": 128, "eviction": "LRU"}


for config_cls in BaseConfig.all():
    print(config_cls.name, config_cls.settings)

cache = BaseConfig.get("cache")
print(cache.version)