# Adapter Pattern in Python

## Was ist das Adapter Pattern?

Das **Adapter Pattern** wandelt die Schnittstelle eines Objekts 
in eine andere um – sodass es in einem Kontext verwendet werden kann, 
wo es sonst inkompatibel wäre.

---

## Sinn und Zweck

- **Schnittstellen anpassen**, ohne den Originalcode zu ändern
- **Alte Klassen in neue APIs integrieren**
- Verschiedene Systeme miteinander **kompatibel machen**

---

## Beispiel: Fremde API anpassen

```python
# Fremde Klasse (z. B. von Drittanbieter)
class OldPrinter:
    def print_text(self, text):
        print(f"[OLD] {text}")


class IPrinter(ABC):
    @abstractmethod
    def print(self, msg):
        pass

# Adapter
class PrinterAdapter(IPrinter):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def print(self, msg):
        self.adaptee.print_text(msg)

# Nutzung
printer = PrinterAdapter(OldPrinter())
printer.print("Hallo Welt")  # [OLD] Hallo Welt
```

---

## Varianten

- **Klassenadapter**: durch Mehrfachvererbung (nicht idiomatisch in Python)
- **Objektadapter** (wie oben): verwendet Komposition – bevorzugt in Python

---

## Python-typisch mit Duck Typing

Manchmal braucht man keinen formellen Adapter, weil Python auf **Verhalten** prüft, nicht auf Typen. Dennoch ist ein Adapter sinnvoll, wenn:

- Methoden umbenannt werden müssen
- Logik transformiert werden soll
- saubere Trennung gewünscht ist

## Fazit

Das Adapter Pattern hilft, **bestehende Objekte kompatibel** zu neuen Anforderungen zu machen – ohne sie zu ändern. Besonders nützlich bei Legacy-Code oder Drittanbieter-APIs.

