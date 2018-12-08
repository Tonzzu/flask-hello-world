# Import sqlite3 and random library
import sqlite3
import random

# create database connection
with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database if table exists
    c.execute("DROP TABLE if exists numbers")

    # create database table
    c.execute("CREATE TABLE numbers(num int)")

    #insert each number to tthe database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))
