#!/usr/bin/python3
import MySQLdb
import sys

my_connection = MySQLdb.connect(
    host = sys.argv[1],
    user = sys.argv[2],
    password = sys.argv[3],
    port = 3306
)

mycursor = my_connection.cursor()
mycursor.execute("SELECT * FROM states ORDER BY id ASC")
states = cursor.fetchall()
for state in states:
    print(state)

print('success')
