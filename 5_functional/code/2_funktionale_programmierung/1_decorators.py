"""
Ein Decorator (dt. Dekorierer) ist ein Konstrukt in Python, mit dem
Funktionen oder Methoden um zusätzliche Funktionalität erweitert werden
können, ohne ihren eigentlichen Code zu verändern.

Ein Decorator ist eine Funktion, die eine andere Funktion als Argument
nimmt und eine neue Funktion zurückgibt.

Einsatzmöglichkeiten:
- Logging
- Zeitmessung
- Zugriffskontrolle
- Vor- und Nachbedingungen

Syntax:
@decorator_name
def funktion():
    ...

Dies ist gleichbedeutend mit:
funktion = decorator_name(funktion)

Dieses Skript zeigt den grundlegenden Aufbau eines einfachen Decorators.
"""
from typing import Callable

def simple(fn: Callable):
    def wrapper():
        print("vor dem Funktionsaufruf")
        fn()
        print("nach dem Funktionsruf")
    return wrapper 


@simple
def begruessung():
    print("HALLO!!!!!")


begruessung()

##########
# Verdoppler 
def double(fn: Callable) -> Callable:
    def wrapper() -> int:
        result = fn() * 2
        return result
    return wrapper


@double
def value():
    return 5

# value = double(value) => unter der Haube passeriert das
# das @-Symbol ist syntatic sugar 
print("result von value():", value())