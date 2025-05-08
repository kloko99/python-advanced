"""
Aufgabe: JsonSerializableMixin: Serialisierung als Mixin-Funktion

In vielen Anwendungen, z.B. Web-APIs oder Datenmodellen, sollen
Objekte einfach in JSON umgewandelt werden können. Ein Mixin bietet
eine saubere Lösung, um diese Funktionalität modular und wiederverwendbar
einzubinden ohne die Hauptklasse zu verkomplizieren.

### Ziel dieser Aufgabe:
1. Implementiere ein Mixin namens `JsonSerializableMixin`.
2. Dieses Mixin soll die Methode `to_json(self)` bereitstellen, die das
   Objekt als JSON-String zurückgibt (nutze `self.__dict__`).
3. Ergänze außerdem eine Methode `from_json(cls, json_str)`, die
   ein Objekt aus einem JSON-String zurückgibt (nutze `**kwargs`).
4. Erzeuge eine Klasse (`Benutzer`), die das Mixin erben.
5. Teste beide Richtungen: Objekt → JSON → Objekt.

Hinweis: Nutze das Modul `json` für die Umwandlung.
"""

import json


# 1) Erstelle Mixin zur JSON-Serialisierung mit Method to_json und from_json
class JsonSerializableMixin:
    pass


# 2) Hauptklasse Benutzer



if __name__ == "__main__":
    pass
    # Testaufrufe zur Veranschaulichung
    # b = Benutzer("maxmuster", "max@example.com")
    # b_json = b.to_json()
    # print(b_json)  # {"benutzername": "maxmuster", "email": "max@example.com"}

    # b_kopie = Benutzer.from_json(b_json)
    # print(b_kopie.benutzername, b_kopie.email)  # maxmuster max@example.com


