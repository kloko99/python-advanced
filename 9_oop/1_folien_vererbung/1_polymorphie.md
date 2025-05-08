# Polymorphie in Python

Polymorphie ist ein wichtiges Konzept in der objektorientierten Programmierung,
das es einem Objekt ermöglicht, sich auf unterschiedliche Weisen zu verhalten,
abhängig von seinem konkreten Typ oder seiner Klasse.

## Operatoren-Überladung

Python können Sie Polymorphie unter anderem durch die Überladung von Operatoren realisieren, was als Operator Overloading bekannt ist.

Python ermöglicht die Definition oder Anpassung des Verhaltens von Operatoren für benutzerdefinierte Objekte mithilfe von speziellen Methoden, die als "magische" oder "Dunder"-Methoden bezeichnet werden (z.B. __add__, __sub__, __mul__, usw.).

Hier ist ein Beispiel, wie Sie Operator Overloading in Python nutzen können, um das Verhalten von zwei Objekten einer benutzerdefinierten Klasse bei der Verwendung des Additionssymbols (+) zu definieren:

### Beispiel: Operator Overloading für eine Klasse `Vektor`

```python
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Definiert, was passiert, wenn zwei Vektor-Objekte addiert werden
        return Vektor(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Vektoren erstellen
v1 = Vektor(2, 3)
v2 = Vektor(4, 5)

# Vektoren mit dem '+' Operator addieren
result = v1 + v2

print("Ergebnis der Vektoraddition:", result)
```

In diesem Beispiel:

- Die Klasse `Vektor` repräsentiert einen mathematischen Vektor im 2D-Raum mit den Komponenten `x` und `y`.
- Die Methode `__add__` wird definiert, um das Verhalten des `+` Operators anzupassen, so dass, wenn zwei `Vektor` Objekte addiert werden, ein neues `Vektor` Objekt zurückgegeben wird, dessen Komponenten die summierten Werte der entsprechenden Komponenten der beiden addierten Vektoren sind.
- Die Methode `__str__` wird überschrieben, um eine benutzerfreundliche String-Repräsentation des Vektors zu ermöglichen.

Dieses Beispiel zeigt, wie Operator Overloading in Python verwendet werden kann, um das Verhalten von spezifischen Operatoren wie `+` für benutzerdefinierte Klassen zu definieren und so eine polymorphe Interaktion zu ermöglichen. Solche Techniken erhöhen die Flexibilität und Lesbarkeit des Codes, indem sie es ermöglichen, intuitive Operationen für Objekte zu definieren, die diese Operationen logisch unterstützen sollten.

## Methodenüberschreibung

Eine gängige Methode zur Implementierung von Polymorphie in Python besteht
darin, Methoden in der Basisklasse zu definieren und diese Methoden in den
abgeleiteten Klassen zu überschreiben. Dies ermöglicht es den abgeleiteten
Klassen, die Methode auf ihre eigene Weise zu implementieren.

Eine Methode ist polymorph, wenn sie in verschiedenen, abgeleiteten Klassen
die gleiche Signatur hat, jedoch erneut implementiert ist.

Beispiel:

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

In diesem Beispiel definiert die Basisklasse `Shape` die Methode `area()`, die
von den abgeleiteten Klassen `Circle` und `Rectangle` überschrieben wird. Jede
abgeleitete Klasse berechnet die Fläche auf unterschiedliche Weisen, da sie
unterschiedliche Formen repräsentieren.

## Verwendung von Polymorphie

Polymorphie tritt in Erscheinung, wenn Sie Instanzen dieser Klassen verwenden.
Sie können dieselben Methodennamen verwenden, unabhängig vom konkreten Typ des
Objekts, und je nach tatsächlichem Typ des Objekts wird die entsprechende
Methode aufgerufen.

Beispiel:

```python
# Erzeugen von Instanzen der abgeleiteten Klassen
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Verwenden der Polymorphie
shapes = [circle, rectangle]

for shape in shapes:
    print(f"Fläche: {shape.area()}")
```

In diesem Code haben wir eine Liste von `Shape`-Objekten, die sowohl `Circle`-
als auch `Rectangle`-Instanzen enthält. Wenn Sie die `area()`-Methode auf
diesen Objekten aufrufen, verhält sie sich polymorph, da sie je nach
tatsächlichem Typ des Objekts unterschiedliche Implementierungen aufruft.

Polymorphie ermöglicht die Erstellung von flexiblen und wiederverwendbaren Code in der objektorientierten Programmierung und ist ein Schlüsselkonzept in Python und anderen objektorientierten Programmiersprachen.
