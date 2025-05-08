""" 
Finally wird immer ausgeführt,
auch bei nicht abgefangenem Fehler
"""

def say_something():
    try:
        7 / 0
    except TypeError as e:
        print("Typeerror ")
    finally:
        print("Wird in jedem Fall ausgeführt: Aufräumarbeiten")


# say_something()


def return_value(n):
    """Das Return in finally kapert das return in try. 
    Häufige Fehlerquelle.
    """
    try:
        value = 3 / n
        return value
    except:
        print("alles andere Abfangen")
    finally:
        return -1
    

print("Return Value:", return_value(1))