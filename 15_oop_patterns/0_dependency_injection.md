# Einführung in Dependency Injection (DI) in Python

## Was ist Dependency Injection?

**Dependency Injection** bedeutet, dass Objekte ihre Abhängigkeiten **nicht selbst erstellen**, sondern **von außen** erhalten. Ziel: lose Kopplung, bessere Testbarkeit, Austauschbarkeit.

---

## Ohne DI: enge Kopplung

```python
class Service:
    def do_something(self):
        print("Service tut etwas")

class Client:
    def __init__(self):
        self.service = Service()  # direkte Instanzierung → enge Kopplung

    def run(self):
        self.service.do_something()
```

---

## Mit DI: lose Kopplung

```python
class Client:
    def __init__(self, service):
        self.service = service  # Service wird "injiziert"

    def run(self):
        self.service.do_something()

service = Service()
client = Client(service)
client.run()
```

---

## Vorteile

- Einfaches Testen durch Mock-Objekte
- Austauschbarkeit (z. B. andere Implementierung)
- Klare Trennung von Verantwortung

---

## Beispiel: Testbarkeit

```python
class MockService:
    def do_something(self):
        print("MOCK: nichts passiert")

client = Client(MockService())
client.run()  # → MOCK: nichts passiert
```

---

## Varianten der Injection

1. **Constructor Injection** (wie oben)
2. **Setter Injection**

```python
class Client:
    def set_service(self, service):
        self.service = service
```

3. **Property Injection** (wie setter, über Deskriptoren oder Properties)

```python
class Client:
    def __init__(self):
        self._service = None  # wird später injiziert

    @property
    def service(self):
        if self._service is None:
            raise ValueError("Service wurde nicht gesetzt")
        return self._service

    @service.setter
    def service(self, value):
        self._service = value

    def run(self):
        self.service.do_something()

# Nutzung
client = Client()
client.service = Service()  # Property Injection
client.run()
```

## Fazit

Dependency Injection ist ein einfaches, aber mächtiges Prinzip zur Entkopplung von Komponenten. In Python braucht es kein spezielles Framework – nur sauberes Design.
