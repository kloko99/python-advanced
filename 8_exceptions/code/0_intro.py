"""
Ausnahme-Behandlung

3 Arten von Fehler:
- Logikfehler (kann man nichts machen)
- Syntax Error (kann man nichts machen)
- Runtime-Error (Behandlen mit try-Except)
"""

d = {
    "a": 3,
    "b": 4,
}

# LOOK BEFORE you leap
if "c" in d:
    print(d["c"])
else:
    print("Key ist nicht enthalten")


# Pythonische Weg
try:
    print(d["c"])
except:  # Vorsicht, BARE EXCEPT!
    print("Key ist nicht enthalten")


# Ausnahme spezifizieren!
try:
    (2, 3).append(3)
    print(d[[1, 2]])  # LIste als Key produziert TypeError
    print(d["c"])
except (KeyError, ZeroDivisionError) as e:
    # e ist das Fehlerobjekt
    print(f"Fehler: {type(e)}")
except TypeError as e:
    print(f"Fehler: {type(e)}")
except Exception as e:
    print("eine allgemeine Exception")
    print(e, type(e))