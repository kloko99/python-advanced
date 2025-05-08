"""
Die erste Metaclass. Metaklassen erzeugen Klassen in Python.

BaseEngine wird durch MyMeta erzeugt.
V8Engine erbt von BaseEngine.
Die Metaklasse MyMeta prüft beim ERzeugen der KLassen, ob das spec_file 
definiert ist (Ausnahme ist die BaseEngine-Klasse).
Falls V8Engine keine Klassenvariable spec_file hat, wird ein Fehler geworfen.

"""
class MyMeta(type):
    """Eine erste Metaklasse."""
    def __new__(cls, classname, bases, attrs, **kwargs):
        """ 
        type(classname, bases, attrs)
        """
        if classname == "BaseEngine":
            return super().__new__(cls, classname, bases, attrs)

        if "spec_file" not in attrs:
            raise ValueError("Das spec file muss in der Klasse definiert sein!")

        return super().__new__(cls, classname, bases, attrs)


class BaseEngine(metaclass=MyMeta):
    """Basisklasse für Motoren."""
    pass


class V8Engine(BaseEngine):
    """V8 Motor. Ein Motor muss die Klassenvariable spec_file definieren."""

    spec_file = "v8spec.txt"

    def __init__(self):
        pass


v8 = V8Engine()