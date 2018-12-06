# INSERT command

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('New York City', \
                'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', \
                'CA', 80000)")

# commit the changes
conn.commit()

#close the database connection
conn.close()


#--- SAME CODE AS ABOVE, BUT WITH 'with' STATEMENT---#
'''

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', \
                'NY', 8400000)")
    c.execute("INSERT INTO population VALUES('San Francisco', \
                'CA', 800000)")

'''
