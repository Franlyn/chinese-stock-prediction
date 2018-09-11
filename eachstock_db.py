'''
Store the opening prices & closing prices for each stock
'''

import mysql.connector, time, warnings
import tushare

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

# get today's date
def getDate():
    date = time.strftime('%Y%m%d', time.localtime(time.time()))
    return date

# create table for each stock with prefix 000 or 002 if not existed
# insert data from start date to end date
def buildDB(start, end):
    # config keys
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

    # get all stocks
    try:
        all_stocks = tushare.get_stock_basics()
        codes = all_stocks.index
    except Exception as e:
        print("Failed to get stock information: " + str(e))

    # Loop through all stocks, create table for each stock
    for i in range(0, len(all_stocks)):
        # only create tables for stocks with prefix 000 or 002
        prefix = (codes[i])[:3]
        if prefix != "000" and prefix != "002":
            continue
        print("Current code is " + codes[i])
        
        try:
            cursor.execute('CREATE TABLE IF NOT EXISTS stock_' + codes[i] + 
                ' (DATE VARCHAR(45), OPEN VARCHAR(45), CLOSE VARCHAR(45), P_CHANGE VARCHAR(45), HIGH VARCHAR(45), LOW VARCHAR(45), VOLUME VARCHAR(45))')
            print("Table stock_" + codes[i] + " successfully created.")
        except Exception as e:
            print(e)

        # get all historical data from start date to end date of each stock
        data = tushare.get_hist_data(codes[i], start, end)

        # insert data from start date to end date of each stock to its table, if not exists
        try:
            for each in range(0, len(data)):
                # get the date
                # ref: https://www.tutorialspoint.com/python/time_strptime.htm
                dateGet = time.strptime(data.index[each], "%Y-%m-%d")

                cursor.execute('INSERT IGNORE INTO stock_' + codes[i] +
                   ' (DATE, OPEN, CLOSE, P_CHANGE, HIGH, LOW, VOLUME) VALUES (%s, %s, %s, %s, %s, %s, %s)' % 
                   (time.strftime('%Y%m%d', dateGet), data.open[each], data.close[each], data.p_change[each], data.high[each], data.low[each], data.volume[each]))
        except Exception as e:
            print("Stock: " + codes[i] + ". " + str(e))

    cnx.close()
    cursor.close()


if __name__=="__main__":
    startDate = '2018-06-01'
    endDate = '2018-06-05'
    buildDB(startDate, endDate)