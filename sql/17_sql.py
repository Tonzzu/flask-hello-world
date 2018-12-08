
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    #c.execute("""CREATE TABLE orders
            #(make TEXT, model TEXT, order_date DATE)
            #""")
            
    order_info = [
                ("Ford", "Mustang", "2018-01-01"),
                ("Ford", "Mustang", "2018-02-02"),
                ("Ford", "Mustang", "2018-03-03"),
                ("Ford", "Mondeo", "2018-04-04"),
                ("Ford", "Mondeo", "2018-05-05"),
                ("Ford", "Mondeo", "2018-06-06"),
                ("Ford", "Model-T", "1930-29-10"),
                ("Ford", "Model-T", "1930-08-08"),
                ("Ford", "Model-T", "1930-09-09"),
                ("Honda", "Accord", "2018-10-10"),
                ("Honda", "Accord", "2018-11-11"),
                ("Honda", "Accord", "2017-12-12"),
                ("Honda", "RAV4", "2018-07-07"),
                ("Honda", "RAV4", "2018-08-08"),
                ("Honda", "RAV4", "2018-09-09")
                ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", order_info)
    c.execute("SELECT * FROM orders ORDER BY order_date ASC")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
