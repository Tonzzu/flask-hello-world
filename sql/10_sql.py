
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    brands = [
            ("Ford", "Mustang", 1),
            ("Ford", "Mondeo", 101),
            ("Ford", "Model-T", 0),
            ("Honda", "Accord", 40),
            ("Honda", "RAV4", 5)
            ]

    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", brands)
