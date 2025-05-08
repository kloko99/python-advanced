"""
Aufgabe – Decorator @timed(repeat=1)

• Misst die Ausführungszeit der Funktion `repeat`‑mal.
• Gibt den Rückgabewert unverändert zurück.
• Druckt: "<name> took X.XXX s (avg of N)".


Vorgaben:  import functools, time, statistics
Nutze functools.wraps, um den Namen der Funktion zu erhalten..

Beispiel:

    @timed(repeat=3)
    def slow(x):
        time.sleep(x)
        return x

    slow(0.1)   # → 0.1  und Meldung auf Stdout
"""
import time
import statistics
from typing import Callable


def timed(repeat=1) -> Callable:
    def decorator(fn) -> Callable:
        def wrapper(*args, **kwargs) -> int:
            times = []
            for _ in range(repeat):
                start = time.perf_counter()
                result = fn(*args, **kwargs)
                end = time.perf_counter()
                times.append(end - start)
            avg = statistics.mean(times)
            print(f"{repeat} mal dauerte durchschnittlich {avg:.2f}")
            return result
        return wrapper 
    return decorator


@timed(repeat=3)
def slow(x):
    time.sleep(x)
    return x


result = slow(0.5)
print("Result final:", result)