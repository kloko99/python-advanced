""" """

import sqlite3

DB_NAME = "job.db"

# Datenbank Verbindung herstellen
conn = sqlite3.connect(DB_NAME)

# Cursor erstellen um mit der DB zu kommuniizeren
cursor = conn.cursor()


def create_table(cursor, conn):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        pay INTEGER
        )
    """
    )
    conn.commit()


def insert_user(cursor, conn, id, firstname, lastname, pay):
    cursor.execute(
        """
        INSERT INTO user 
        (id, first_name, last_name, pay)
        VALUES
        (?, ?, ?, ?);
    """,
        (id, firstname, lastname, pay),
    )
    conn.commit()


insert_user(cursor, conn, 23, "Bob", "Geldorf", 2022)
conn.close()
