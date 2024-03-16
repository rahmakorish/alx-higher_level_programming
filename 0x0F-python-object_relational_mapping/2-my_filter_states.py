#!/usr/bin/python3
"""module"""


import sys
import MySQLdb

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name = {} ORDER BY \
                states.id;".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    mydb.close()
