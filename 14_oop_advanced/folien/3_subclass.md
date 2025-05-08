# Einführung in `__init_subclass__` in Python

## Was ist `__init_subclass__`?

Die Methode `__init_subclass__` wird **automatisch aufgerufen**, 
wenn eine Klasse von einer Basisklasse erbt. Sie ist ideal für:

- Validierungen
- automatische Registrierung
- Voreinstellungen für Subklassen

In Python verfügbar seit Python 3.6

https://peps.python.org/pep-0487/
---

## Beispiel: Logging beim Vererben

```python
class Basis:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Neue Subklasse: {cls.__name__}")

class A(Basis):
    pass

class B(Basis):
    pass

# Ausgabe:
# Neue Subklasse: A
# Neue Subklasse: B
```

---

## Beispiel: Subklassen validieren

```python
class PluginBase:
    required_attributes = ['name']

    def __init_subclass__(cls):
        for attr in cls.required_attributes:
            if not hasattr(cls, attr):
                raise TypeError(f"{cls.__name__} muss Attribut '{attr}' definieren")

class MyPlugin(PluginBase):
    name = "Plugin 1"  # ok

class InvalidPlugin(PluginBase):
    pass  # TypeError!
```

---

## Vorteile gegenüber Metaklassen

- Einfacher zu schreiben
- Kein Wechsel der Metaklasse nötig
- Besser lesbar bei einfachen Hooks

---

## Fazit

`__init_subclass__` ist der **einfache Hook**, um das Verhalten bei Vererbung zu steuern. Ideal für Frameworks, Validierung und Automatisierung – ganz ohne Metaklassen.

