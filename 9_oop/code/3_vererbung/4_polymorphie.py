"""
Polymorphie ist ein wichtiges Konzept in der objektorientierten Programmierung,
das es einem Objekt ermöglicht, sich auf unterschiedliche Weisen zu verhalten,
abhängig von seinem konkreten Typ oder seiner Klasse.
"""
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def print_shapes(shapes: list[Shape]):
    """alle Shapes haben area() implementiert."""
    for shape in shapes:
        print(shape.area())


if __name__ == "__main__":

    shapes = [
        Circle(3),
        Circle(34),
        Rectangle(2, 3),
        Circle(3)
    ]

print_shapes(shapes)