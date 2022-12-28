import mysql.connector
from mysql.connector import errorcode
import datetime
# connecting to database

config = {
    "user": "root",
    "password": "Megroot23",
    "host": "localhost",
    "database": "parchment_press",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    #gets hours worked in last year, actually need to get data from each quarter of last year, reconfig data??

    print("First Quarter")
    cursor.execute("SELECT Employee_name, Employee_time FROM employee WHERE timecard_date between '2022-01-01' and '2022-04-30'")
    result = cursor.fetchall()
    for i in result:
        print(i)

    print("2nd Quarter")
    cursor.execute("SELECT Employee_name, Employee_time FROM employee WHERE timecard_date between '2022-05-01' and '2022-08-30'")
    result = cursor.fetchall()
    for i in result:
        print(i)

    print("3rd Quarter")
    cursor.execute(
        "SELECT Employee_name, Employee_time FROM employee WHERE timecard_date between '2022-09-01' and '2022-11-30'")
    result = cursor.fetchall()
    for i in result:
        print(i)

    print("4th Quarter")
    cursor.execute(
        "SELECT Employee_name, Employee_time FROM employee WHERE timecard_date between '2022-12-01' and '2023-01-01'")
    result = cursor.fetchall()
    for i in result:
        print(i)

except mysql.connector.Error as err:
    if err.errno == errorcode.Er_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()

        #some code modified from mguthman report1 and https://www.sqlservercentral.com/forums/topic/query-records-in-last-12-months

