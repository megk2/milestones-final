import mysql.connector
from mysql.connector import errorcode
import datetime



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

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

    year = 2022

    for month in range(1, 13, 1):

         month = datetime.datetime(year, month, 1)
        if month < 6:
            print("\n\n-- DISPLAYING  Departments RECORD FOR  {}--\n".format(month))
            cursor.execute("SELECT SUM(sales_amt) as total FROM Departments where MONTH(sale_date) = {}".format(month))
            count = cursor.fetchall()
            for x in count:
                print(month, x[0])




except mysql.connector.Error as err:
    if err.errno == errorcode.Er_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

finally:
    db.close()

 #some code modified from mguthman report1 from first try at this project



