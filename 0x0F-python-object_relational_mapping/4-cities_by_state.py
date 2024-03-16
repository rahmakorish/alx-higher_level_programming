#!/usr/bin/python3
"""python file"""


import sys
import MySQLdb

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = mydb.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC;")
    citylist = cur.fetchall()
    for city in citylist:
        print(city)
    cur.close()
    mydb.close()
