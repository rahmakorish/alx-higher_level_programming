import MySQLdb
import mysql.connector

my_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

mycursor = my_connection.cursor()

print('success')