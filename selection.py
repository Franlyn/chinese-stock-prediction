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

    # list of stocks that satisfies the requirements
    satisfied = list()

    # looping through all stock tables, select the ones that satisfy the thoery
    # write to log file
    for i in range(0, len(stocks)):
        prefix = (stocks[i][0])[:3]

        if prefix != "000" and prefix != "002":
            continue

        # use the selection method to select stocks
        try:
            # get data from the stock table
            cursor.execute("SELECT * FROM stock_" + stocks[i][0]
                + " WHERE date = %s OR date = %s ORDER BY date DESC"
                % (today, yesterday))
            curStock = cursor.fetchall()

            if curStock == None or len(curStock) == 0:
                continue
            print(curStock)
            

            # record data
            openT = float(curStock[0][1])
            closeT = float(curStock[0][2])
            p_changeT = float(curStock[0][3])

            openY = float(curStock[1][1])
            closeY = float(curStock[1][2])
            p_changeY = float(curStock[1][3])

            # apply the constraints
            if openY < closeT and closeY > openT and p_changeY < -2 and p_changeT > 9.8:
                f.write("# %s(%s):\nToday(%s): opens at %s, closes at %s;\nYesterday(%s): opens at %s, closes at %s.\n\n"
                    % (stocks[i][1], stocks[1][0], today, openT, closeT, yesterday, openY, closeY))
                satisfied.append(stocks[i]) # append the (code, name) tuple
            
        except Exception as e:
            print("Selection error: " + str(e))

    cnx.close()
    cursor.close()
    f.close()
    return satisfied



if __name__=="__main__":
    findStock()
