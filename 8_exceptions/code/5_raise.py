""" 
Einen Fehler erheben, Beispiel simpler Taschenrechner
"""
def summe(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float:
    return a / b


OPERATIONS = {
    "+": summe, 
    "*": multiply,
    "/": division
}

def controller(operator: str, a: float, b: float) -> float:
    """Steuerungs-Funktion des Taschenrechners."""

    try:
        op = OPERATIONS[operator]
    except KeyError as e:
        raise NotImplementedError("Dieses Operator ist nicht implementiert")

    return op(a, b)


# User gibt ein: + 3 3
while True:
    try:
        operator, a, b = input(">").split()   # + 3 3
        a = float(a)
        b = float(b)
        result = controller(operator, a, b)
        print(result)
    except ZeroDivisionError as e:
        print("Division durch 0 nicht möglich.")
    except NotImplementedError as e:
        print("Fehlerhafter Operator")
