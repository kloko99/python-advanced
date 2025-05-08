# Einführung in Python-Metaklassen

## Was ist eine Metaklasse?

In Python ist **alles ein Objekt** – auch Klassen. Und die **Klasse einer Klasse** ist eine **Metaklasse**. Während eine Klasse Instanzen erzeugt, erzeugt eine Metaklasse Klassen.

```python
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
```

## Warum Metaklassen?

Metaklassen erlauben es dir, **die Klassenerstellung zu beeinflussen** – z. B. zur Validierung, Modifikation oder automatischen Registrierung von Klassen.

## Eine einfache Metaklasse

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Erzeuge Klasse: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```

Ausgabe:
```
Erzeuge Klasse: MyClass
```

## Was kann man damit machen?

- Klassen automatisch registrieren
- Methoden oder Attribute erzwingen
- Verhalten basierend auf Klassennamen ändern

## Praxisbeispiel: Auto-Registrierung

```python
registry = {}

class AutoRegister(type):
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        registry[name] = new_cls
        return new_cls

class PluginBase(metaclass=AutoRegister):
    pass

class MyPlugin(PluginBase):
    pass

print(registry)  # {'PluginBase': <class ...>, 'MyPlugin': <class ...>}
```

## Fazit

Metaklassen sind mächtig, aber selten nötig. Verwende sie nur, wenn du wirklich das Verhalten von Klassen selbst beeinflussen willst. Meist reichen Funktionen, Decorators oder Mixins aus.

Eine gute Alternative zu Metaklassen ist der `__init_subclass__-Hook`

