"""
Parametrisierte Decorators erlauben es, einem Decorator Argumente zu
übergeben. Das ist besonders nützlich, wenn das Verhalten des Decorators
abhängig von konfigurierbaren Werten sein soll – etwa bei Validierungen,
Log-Leveln oder bedingtem Ausführen.

Ein parametrisierter Decorator besteht aus drei verschachtelten Funktionen:
1. Eine äußere Funktion, die die Parameter des Decorators entgegennimmt.
2. Eine innere Decorator-Funktion, die die zu dekorierende Funktion annimmt.
3. Ein Wrapper, der die Logik ausführt.

Dieses Skript zeigt reale Anwendungsbeispiele für Decorators mit Parametern,
zum Beispiel zur Wertevalidierung und Zugriffskontrolle.

PAUSE bis 13:30
"""
from typing import Callable
import functools

def logger(fn):
    def wrapper(*args, **kwargs):
        print("Der Name der Funktion:", fn.__name__)
        print(f"Argumente: {args} {kwargs}")
        result = fn(*args, **kwargs)
        return result
    return wrapper 


# Beispiel 1: Validierung von Zahlenwerten mit einem parameterisierten Decorator
def validate_range(min_value: int, max_value: int) -> Callable:
    """Validator der einen Wert auf eine Range prüft."""
    def inner(fn: Callable) -> Callable:
        @functools.wraps(fn)  # nötig, damit bei quadrat.__name__ auch der richtige Name ausgegeben wird
        def wrapper(x):
            if x < min_value or x > max_value:
                raise ValueError("Der Wert liegt nicht in der Range!")
            return fn(x)
        return wrapper
    return inner


#@logger
@validate_range(1, 10)
def quadrat(x):
    return x * x


# quadrat = logger(quadrat)
print(quadrat(10)) # wrapper(2)
print(quadrat.__name__)  # qudrat, geht nur wegen functools.wraps

