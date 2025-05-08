# Zugriffsmodifier private, public, protected

In Java und C++ etwa werden sogenannte ``Access-Modifier`` genutzt,
um den Zugriff auf Variablen und Methoden einzuschränken.
Der Sinn dahinter ist es, Objekte so weit wie möglich
einzukapseln und zu verhindern, dass aus Versehen
Attribute verändert werden, die nicht verändert werden
sollten

## Public, private, protected 
Man unterscheidet hier zwischen ``public, private und protected`` Attributen.
``Public`` bedeutet, dass der Zugriff und das Verändern eines Attributs von außen möglich ist, ``privat`` hingegen, dass der Zugriff nur von innterhalb der Klasse erlaubt ist. ``Protected`` ist ein Sonderfall und ählich wie private, erlaubt aber auch ein Ändern des Attributes in geerbten Klassen.

    public int x = 3;
    private float value = 3.3;

### Mehr zum Thema Access-Modifiers unter Java hier: 
[Access Modifiers](https://www.programiz.com/java-programming/access-modifiers)

## Python (public, non-public)

Dieses Konzept gibt es in Python nicht. In Python sind per default
alle Variablen und Methoden public. Man kann zwar die Sichtbarkeit
einer Varibalen einschränken, in dem man sie mit einem ``__ präfixt``,
aber der Grund ist hier nicht, dieses Attribut privat zu machen, sondern
Namenskollisionen beim Subclassing zu verhindern (``Name Manging``). 

### Mehr zum Thema private Variablen unter Python:
[private Variablen unter Python](https://docs.python.org/3/tutorial/classes.html?highlight=private#private-variables)

class Bill:

    def __init__(self):
        self.x = 3  # eine "public" Variable
        self._msg = ""  # eine "interne" Variable
        self.id_ = ""  # um Namenskollision mit id zu vermeiden
        self.__value = 3.3  # Doppel-Unterstrich als private (name mangling)


## Allgemein
In Python hat der Unterstrich im Zusammenhang mit Variablen verschiedene Bedeutungen:
- single Underscore Präfix: ``_x``, gedacht für interne Zwecke.
- single Underscore Postfix: ``id_``, um Namenskollisionen mit Built-in Typen zu vermeiden.
- Dunder: ``__x__``, magische Variable, wird nur von Python genutzt
- Doppel-Präfix: ``__x``, Name-Mangling, Kollisionen beim Subclassing zu verhindern.

Mehr zu diesem Thema hier:
[Bedeutung von Unterstrichen](https://dbader.org/blog/meaning-of-underscores-in-python)
