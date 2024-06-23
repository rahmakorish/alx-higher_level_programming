#!/usr/bin/python3
"""python file"""


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
    cur.execute("SELECT * FROM cities ORDER BY id ASC;")
    citylist = cur.fetchall()
    for city in citylist:
        print(city)
    cur.close()
    mydb.close()
