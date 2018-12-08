# SQLite Functions

"""Using the COUNT() function, calculate the total number of orders for each make and model."""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = { 'Mustang count' : "SELECT count(make) FROM orders WHERE model = 'Mustang'",
            'Mondeo count' : "SELECT count(make) FROM orders WHERE model = 'Mondeo'",
            'Model-T count' : "SELECT count(make) FROM orders WHERE model = 'Model-T'",
            'Accord count' : "SELECT count(make) FROM orders WHERE model = 'Accord'",
            'RAV4 count' : "SELECT count(make) FROM orders WHERE model = 'RAV4'"
            }

    # run each sql query item in the dictionary
    for keys, values in sql.items():

        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print(keys + ":", result[0])
