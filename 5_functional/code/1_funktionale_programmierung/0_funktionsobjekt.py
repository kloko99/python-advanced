"""
Eine Funktion kann in Python wie jede andere
Variable behandelt werden kann. Funktionen sind sogenannte 'First-Class
Citizens'. Man kann sie einer Variablen zuweisen, als Argument
weitergeben oder als Rückgabewert verwenden.

"""
def fn(n):
    """DAs ist eine Testfunktion."""
    print(n)

fn(3)   # call

print(fn.__doc__)  # Funktionsobjekt
print(dir(fn))

# Aufgabe: Schreibe eine Funktion "n_times", die eine Funktion "double"
# als Argument übergeben bekommt, und sie n-mal auf denselben Wert anwendet.
def double(x: int) -> int:
    """Verdoppelt den Wert."""
    return x * 2


def n_times(fn_double):
    """Wendet die Funktion f n-mal auf den Wert an."""
    print(fn_double(3))

n_times(double)

myprint = print
myprint("hallo myprint")
print(id(myprint) == id(print))  # True


print("typ von fn:", type(fn))
print(fn.__code__.co_varnames)
print(fn.__name__)