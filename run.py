import os
import pymysql
# Jonathan Kelly Aug 2021 - Code Institute SQL Sample Code.

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')


# Connect to the database
def GetConnection():
    print("opening db connection")
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
        print("### Select Query Completed and db connecton closed")


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
        print("### Select Query with Cursor Completed and db connecton closed")



def AddTable():
    try:
    # Run a query
        connection = GetConnection()
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
    finally:
        # Close the connection, regardless of whether or not the above was successful
        connection.close
        print("### AddTable Completed and db connecton closed")


def InsertQuery():
    connection = GetConnection()
    try:
        with connection.cursor() as cursor:
            row = ("Bob", 21, "1990-02-06 23:04:56")
            cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
    finally:
        connection.close
        print("### Insert Completed and db connecton closed")


def ExecuteManySample():
    connection = GetConnection()
    try:
        with connection.cursor() as cursor:
            rows = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
            cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
            connection.commit()
    finally:
        connection.close
        print("### Exec Many Smaple Completed and db connecton closed")


def UpdateSample():
    connection = GetConnection() 
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
            connection.commit()
    finally:
        connection.close
        print("### Update Sample Completed and db connecton closed")


def AltUpdateSample():
    connection = GetConnection()  
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'bob'))
            connection.commit()
    finally:
        connection.close
        print("### Alt Update Sample Completed and db connecton closed")


def UpdateManySample():
    connection = GetConnection()
    try:
        with connection.cursor() as cursor:
            rows = [(23, 'bob'),
                (24, 'jim'),
                (25, 'fred')]
            cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
            connection.commit()#
    finally:
        connection.close
        print("### Update Many Sample Completed and db connecton closed")


def DeleteSample():
    # dont delete me... dont let me go...
    connection = GetConnection()
    try:
        with connection.cursor() as cursor:
            rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
            connection.commit()
    finally:
        connection.close
        print("### Update Many Sample Completed and db connecton closed")


def DleteMany():
    # dont delete me... dont let me go...
    connection = GetConnection()
    try:
        with connection.cursor() as cursor:
            rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
            connection.commit()
    finally:
        connection.close
        print("### alt Delete Sample Completed and db connecton closed")


def AltDeleteSample():
    # I hate to wake you up to say goodbye!
    connection = GetConnection()  
    try:
        with connection.cursor() as cursor:
            rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['bob', 'jim'])
            connection.commit()
    finally:
        connection.close
        print("### Alt Delete Sample Completed and db connecton closed")


def DeleteWhereIn():
    # dont know when Ill back again.
    connection = GetConnection()  
    try:
        with connection.cursor() as cursor:
            list_of_names = ['fred', 'Fred']
            # Prepare a string with same number of placeholders as in list_of_names
            format_strings = ','.join(['%s'] * len(list_of_names))
            cursor.execute(
                "DELETE FROM Friends WHERE name in ({});".format(format_strings),
                list_of_names)
            connection.commit()
    finally:
        connection.close
        print("### DeDeleteWhereIn Sample Completed and db connecton closed")


SelectQuery()
SelectQueryWithCursor()
AddTable()
InsertQuery()
ExecuteManySample()
UpdateSample()
AltUpdateSample()
UpdateManySample()
DeleteSample()
AltDeleteSample()
DleteMany()
DeleteWhereIn()