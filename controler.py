import sqlite3 as sql

def crateDB():
    conn = sql.connect("plants.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("plants.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE plants (
        id integer,
        name text,

        )"""
    )


if __name__ == "__main__":
    crateDB()