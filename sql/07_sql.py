# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use for loop tp iterate through the database, printing the results line by line
    for row in c.execute("SELECT firstname, lastname from employees"):
        print(row)
