""" 
Exception Hierachy
"""
d = {
    "a": 3,
    "b": 4,
}

try:
    print(d["c"])
except LookupError as e:
    print(e, type(e))


# Aufgabe: Schreibe Funktion is_float(n)
# Überprüfen, ob n als Float parsebar ist n=1.1, n=ab
def is_float(n: int):
    try:
        float(n)
        return True
    except (TypeError, ValueError) as e:
        return False

result = is_float("21.3")