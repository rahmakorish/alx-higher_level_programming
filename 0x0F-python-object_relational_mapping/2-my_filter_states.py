#!/usr/bin/python3
"""module"""


import sys
import MySQLdb

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    
    cur = mydb.cursor()
    namevalue = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY id;".format(namevalue))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    mydb.close()
