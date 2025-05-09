"""
Multiprocessing: Prozesse parallel starten.
"""

import multiprocessing
import time
import os


def cpu_bound_task():
    print(f"Current process id: {os.getpid()}")
    print(f"Parent process: {os.getppid()}")
    c = 0
    for i in range(20**6):
        c += i


if __name__ == "__main__":
    # Bei Multiprocessing ist dieser Guard __name__ == "__main__" Pflicht

    # Starten zwei unabhängige Prozesse
    start = time.perf_counter()
    t1 = multiprocessing.Process(target=cpu_bound_task)
    t2 = multiprocessing.Process(target=cpu_bound_task)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.perf_counter()
    print(f"Task mit 2 Prozessen hat {end - start: .2f} Sekunden gedauert.")

    # OHNE Multiprocessing
    start = time.perf_counter()
    cpu_bound_task()
    cpu_bound_task()
    end = time.perf_counter()
    print(f"Task ohne Multprocessing hat {end - start: .2f} Sekunden gedauert.")
