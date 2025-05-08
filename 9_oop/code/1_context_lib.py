""" 
Context Manager Lib ermöglicht das einfache Erstellen eines Kontext-Managers.
"""
import time 
import contextlib
import sqlite3


@contextlib.contextmanager
def timer():

    # das findet vor dem Kontext statt
    start = time.perf_counter()
    yield  # hier findet der Kontext statt 

    # das findet beim Verlassen des Kontext statt
    end = time.perf_counter()
    print("Laufzeit: {:.2f}".format(end - start))


with timer():
    # ab jetzt wird gemessen
    x = 0
    for i in range(10**8):
        pass

    # hier ist die Messung zu ende und der Kontext wird verlassen


# Beispiel Datenbank-Manager:
@contextlib.contextmanager
def create_database_connection():
    db_connection = sqlite3.connect("./db/data.db")
    try:
        yield db_connection
    finally:
        db_connection.close()


with create_database_connection() as db:
    cursor = db.cursor()

