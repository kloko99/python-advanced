"""
Bei CPU-intensiven Threads arbeitet Python
dank GIL (Global Interpreter Lock) nur jweils auf einem Thread.
Echtes Multithreading ist hier (noch) nicht möglich. Das wrd sich in einer
zukünftigen Versoin von Python ändern.

Beispiel zeigt, das die Aufgabe mit und ohne Threads gleich lang dauert.
"""

import time
import threading


def cpu_bound_task():
    c = 0
    for i in range(20**6):
        c += i


# MIT THREADS (laufen nebenläufig. Allerdings sperrt die GIL immer einen Thread)
start = time.perf_counter()
t1 = threading.Thread(target=cpu_bound_task)
t2 = threading.Thread(target=cpu_bound_task)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.perf_counter()
print(f"Task mit Threads hat {end - start: .2f} Sekunden gedauert.")


# OHNE THREADS (Jobs starten hintereinander)
start = time.perf_counter()
cpu_bound_task()
cpu_bound_task()
end = time.perf_counter()
print(f"Task ohne Threads hat {end - start: .2f} Sekunden gedauert.")
