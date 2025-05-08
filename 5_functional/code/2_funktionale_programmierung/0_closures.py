"""
Eine Closure ist ein Konzept aus der funktionalen Programmierung.
Wenn eine Funktion, die freie Variablen verwendet, den Scope verlässt,
in dem diese vereinbart sind (meistens, weil sie selbst von einer Funktion
zurückgegeben wird), und wird dieser Scope abgeräumt, so wären diese
freien Variablen ab diesem Zeitpunkt undefiniert.

Um dem zu begegnen, setzt der Compiler bei der Rückgabe eine neue Struktur
zusammen. Sie besteht aus dieser Funktion und sämtlichen von ihr
verwendeten freien Variablen. Diese Struktur heißt Closure.

Ein Closure entsteht, wenn:
1. Eine Funktion innerhalb einer anderen definiert ist,
2. Die innere Funktion eine Variable der äußeren Funktion verwendet,
3. Die äußere Funktion eine Referenz auf die innere Funktion zurückgibt.

Closures ermöglichen das Erzeugen spezialisierter Funktionen zur
Laufzeit und werden oft für Konfiguration, Kapselung und in
funktionalen Programmiertechniken verwendet.

"""
from typing import Callable


def fn(x: int) -> Callable:
    def g():
        print(x)
    return g

gg = fn(42)
print(type(gg))
gg()


# Beispiel 1: Einfache Closure zur Erzeugung einer Multiplikationsfunktion
def create_multiplier(value) -> Callable:
    def multiply(x) -> int:
        return value * x 
    return multiply # hier Funktionsreferenz zurückgeben

mal_drei = create_multiplier(3)
print(mal_drei(4))
