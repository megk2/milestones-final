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

#getting min and max
    print("MAX")
    cursor.execute("SELECT Buyer_id, iventory_amt FROM buyers WHERE iventory_amt = (SELECT max(iventory_amt) from buyers)")
    result = cursor.fetchall()

    for i in result:
        print(i)

    print("MIN")
    cursor.execute("SELECT Buyer_id, iventory_amt FROM buyers WHERE iventory_amt = (SELECT MIN(iventory_amt) from buyers)")
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

        #some code modified from mguthman report1 form first try at this project

