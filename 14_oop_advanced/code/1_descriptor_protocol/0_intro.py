"""
Thema: Das Descriptor-Protokoll in Python

Das Descriptor-Protokoll ermöglicht es, das Verhalten von Attributzugriffen
in Klassen zu steuern. Ein Objekt wird dann als „Descriptor“ bezeichnet,
wenn es eine oder mehrere der folgenden Methoden implementiert:

- __get__(self, instance, owner): Wird beim Lesen des Attributs aufgerufen.
- __set__(self, instance, value): Wird beim Setzen des Attributs aufgerufen.
- __delete__(self, instance): Wird beim Löschen des Attributs aufgerufen.

Es gibt zwei Arten von Deskriptoren:
- **Daten-Deskriptoren**: implementieren mindestens __get__ und __set__.
- **Nicht-Daten-Deskriptoren**: implementieren nur __get__.

Deskriptoren sind die Grundlage vieler eingebauter Python-Konzepte wie:
- @property
- Methoden
- Klassenmethoden und statische Methoden
- Validierungs- und Zugriffskontrollmechanismen (z. B. in ORMs)

Das Descriptor-Protokoll ist besonders nützlich, wenn man wiederverwendbares
Verhalten für Attribute definieren möchte.
"""
