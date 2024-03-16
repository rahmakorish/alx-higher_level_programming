#!/usr/bin/python3
"""this module filter atates"""


import sys
import MySQLdb

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        username=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host=3306
    )
    cur = mydb.cursor()
    cur.execute("Select * FROM states WHERE name LIKE 'N%';")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    mydb.close()