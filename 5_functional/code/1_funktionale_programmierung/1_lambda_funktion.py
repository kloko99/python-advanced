"""
Lambda-Ausdrücke in Python sind anonyme Funktionen – das heißt,
sie haben keinen Namen. Sie werden mit dem Schlüsselwort `lambda`
definiert und dienen der kompakten Darstellung einfacher Funktionen.

Syntax: lambda argumente: ausdruck

Lambda-Funktionen können beliebig viele Argumente enthalten, aber nur
einen einzigen Ausdruck, dessen Ergebnis automatisch zurückgegeben wird.
Sie sind besonders nützlich, wenn man eine Funktion nur kurzzeitig
und einmalig benötigt, ohne ihr einen Namen zu geben.

Dieses Skript erklärt die Syntax und zeigt grundlegende Beispiele,
ohne den Einsatz in anderen Funktionen wie `map()` oder `sorted()`.
"""
fn = lambda x, y: x * y   # Lambda Funktion wurde Variable fn zugewiesen

# gleichbedeutend
def g(x, y):
    return x * y


print(type(fn), fn)

# Lambda-Funktion mit einem Argument: Quadrieren einer Zahl
quadrat = lambda x: x**2

# Lambda-Funktion ohne Argumente: Gibt einen festen Wert zurück
leere = lambda: 42


# Lambda-Funktion mit Bedingung: Größeres von zwei Werten
maximum = lambda x, y: x if x > y else y
print(maximum(3, 4))
