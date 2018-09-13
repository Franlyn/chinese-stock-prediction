'''
    Select the stocks that satisfy the following requirement
        * The stock sank more than 2% yesterday
        * Today's opening price is lower than yeaterday's closing price
        * Today's closing price is lower than yesterday's opening price
'''
import mysql.connector, time, warnings
import tushare
from datetime import date, timedelta

# get today's date - diff
#   i.e.: If diff is 1, then return yesterday's date
def getDate(diff):
    requireDate = date.today() - timedelta(diff)
    return requireDate.strftime('%Y%m%d')
    

# find the stocks and write to the log
def findStock():
    # create the log file
    today = getDate(0)
    try:
        filename = today + "_FOUND.log"
        f = open(filename, "w+")
    except Exception as e:
        print("Fail to create file: " + str(e))

    # get yesterday's date
    yesterday = getDate(1)

    # connect to database
    config = {
        'user' : 'root',
        'password' : 'password',        # will be changed later
        'host' : '127.0.0.1',
        'database' : 'stocks',
        'raise_on_warnings' : True
    }

    # connect to mysql database
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
    except Exception as e:
        print("Connection to mysql database failed: " + str(e))
        exit(0)

    # get code from all stocks
    cursor.execute("SELECT code, name FROM stocktable")
    stocks = cursor.fetchall()

    # looping through all stock tables, select the ones that satisfy the thoery
    # write to log file
    for i in range(0, len(stocks)):
        prefix = (stocks[i][0])[:3]
        print(prefix)

        if prefix != "000" and prefix != "002":
            continue

        # use the selection method to select stocks
        try:
            # cursor
            print("do something")
        except Exception as e:
            f.write("stock has no data")




if __name__=="__main__":
    findStock()
