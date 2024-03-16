#!/usr/bin/python3
"""python file"""


import MySQLdb
import sys

if __name__ == "__main__":
    my_connection = MySQLdb.connect(
        host="localhost",
        db=sys.argv[3],
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306
    )

    cur = my_connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \
                'N%' ORDER BY states.id;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    my_connection.close()
