import os
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
def GetConnection():
    print ("opening db connection")
    return pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')


def SelectQuery():
    try:
    # Run a query
        connection = GetConnection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Artist;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        # Close the connection, regardless of whether or not the above was successful
        connection.close
        print ("### Select Query Completed and db connecton closed")


def SelectQueryWithCursor():
    try:
    # Run a query
        connection = GetConnection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM Genre;"
            cursor.execute(sql)
            for row in cursor:
                print(row)
    finally:
        # Close the connection, regardless of whether or not the above was successful
        connection.close
        print ("### Select Query with Cursor Completed and db connecton closed")

SelectQuery()
SelectQueryWithCursor()