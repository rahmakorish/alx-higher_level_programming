#!/usr/bin/python3
"""module"""


import Sys
import MySQLdb

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        username=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        value=sys.argv[4]
    )
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name =$value ORDER BY state.id;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    mydb.close()
