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
    state_name = sys.argv[4]
    mycursor = my_connection.cursor()
    mycursor.execute("SELECT * FROM cities ORDER BY cities.id ASC;")
    states = mycursor.fetchall()
    for state in states:
        print(state)
    mycursor.close()
    my_connection.close()
