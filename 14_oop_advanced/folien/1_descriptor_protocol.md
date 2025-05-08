# Einführung in das Descriptor Protocol in Python

## Was ist ein Descriptor?

Ein **Descriptor** ist ein Objekt, das eines (oder mehrere) der folgenden Methoden implementiert:

- `__get__(self, instance, owner)`
- `__set__(self, instance, value)`
- `__delete__(self, instance)`

Descriptors steuern, **wie Attribute gelesen, geschrieben oder gelöscht werden**
– z. B. bei `@property`, `staticmethod` und `classmethod`.

---

## Beispiel 1: Eigener Descriptor mit primitivem Logging

```python
class RevealAccess:
    def __init__(self, name):
        self.name = name
        self._value = None

    def __get__(self, instance, owner):
        print(f"Zugriff auf {self.name}")
        return self._value

    def __set__(self, instance, value):
        print(f"Setze {self.name} auf {value}")
        self._value = value

class MyClass:
    x = RevealAccess("x")

obj = MyClass()
obj.x = 42    # Setze x auf 42
print(obj.x)  # Zugriff auf x → 42
```

---

## Arten von Descriptors

- **Daten-Descriptor**: hat `__get__` **und** `__set__`
- **Nicht-Daten-Descriptor**: nur `__get__`

Nicht-Daten-Descriptors werden von Instanz-Attributen überschrieben. Daten-Descriptors nicht.

---

## Beispiel 2: Validierung von Werten

```python
class PositiveNumber:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} muss positiv sein")
        instance.__dict__[self.name] = value

class Konto:
    saldo = PositiveNumber("saldo")

    def __init__(self, startwert):
        self.saldo = startwert

k = Konto(100)
print(k.saldo)  # 100
k.saldo = 50    # ok
k.saldo = -10   # ValueError!
```

Hinweis: Statt `_values[instance]` könnte man auch `WeakKeyDictionary` verwenden, um Speicherlecks zu vermeiden.

---

## Anwendung

- Validierung von Attributen
- Caching / Lazy Evaluation
- Zugriff kontrollieren oder protokollieren

---

## Fazit
Descriptors geben dir die volle Kontrolle über Attributzugriffe auf Klassenebene. Sie sind ein **mächtiges Werkzeug für wiederverwendbare Logik**, z. B. Validierung, Berechnung oder Zugriffsschutz.

Für einfache Fälle sind `@property`, `@staticmethod` und `@classmethod` oft ausreichend. Descriptors sind jedoch nützlich, wenn du **komplexere Logik** benötigst oder **wiederverwendbare Attribute** erstellen möchtest.

Die Bibliothek `Pydantic` verwendet Descriptors, um Datenvalidierung und -serialisierung zu ermöglichen. Auch in `Django` werden Descriptors für Model-Attribute verwendet.
