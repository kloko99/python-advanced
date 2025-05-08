"""
Aufgabe: Eigenschaftsvalidierung über Deskriptoren

In einem Konfigurationssystem sollen bestimmte Felder automatisch
validiert werden, z. B. dass eine Zahl positiv ist oder ein String
nicht leer.

Deine Aufgabe:
1. Implementiere einen Descriptor namens 'PositiveIntegerField',
   der sicherstellt, dass nur positive ganze Zahlen zugewiesen werden.
2. Erstelle eine Klasse 'JobConfig' mit folgenden Feldern:
   - 'retries': PositiveIntegerField
   - 'timeout': PositiveIntegerField
3. Stelle sicher, dass beim Zuweisen eines ungültigen Werts
   (z. B. -1 oder None) ein ValueError ausgelöst wird.

Hinweis:
Der Descriptor muss __get__, __set__ und __set_name__ korrekt
implementieren.
"""


class PositiveIntegerField:
    """Implemtiere das Descriptor-Protokoll für positive ganze Zahlen."""
    pass


class JobConfig:
    """Hat 2 Klassen-attribute, die mit dem Descriptor erstellt werden.

    retries = PositiveIntegerField()
    timeout = PositiveIntegerField()

    """
    # retries =  ...
    # timeout = ...

    def __init__("..."):
        pass


# Awendung
job = JobConfig(retries=3, timeout=10)
print(job.retries)   # → 3

job.retries = 5
print(job.retries)   # → 5

job.timeout = -1     # → ValueError: Wert muss eine positive ganze Zahl sein.
