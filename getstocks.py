'''
Get the name, code, blah of each stock in the Chinese stock market,
	store the data into the sql database
'''

import mysql.connector
import tushare

# connect to mysql database
config = {
	'user' : 'root',
	'password' : 'password',		# will be changed later
	'host' : '127.0.0.1',
	'database' : 'stocks',
	'raise_on_warnings' : True
}

try:
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
except Exception as e:
	print("Connection to mysql database failed: " + str(e))
	exit(0)

print("connected to the database!")

# Get a list of all stocks with tushare module
try:
	all_stocks = tushare.get_stock_basics()
except Exception as e:
	print("Failed to get stock information: " + e)

codes = all_stocks.index
names = all_stocks.name
industries = all_stocks.industry
areas = all_stocks.area

# insert each stock info to the table, i.e.: name, code etc
for i in range(0, len(all_stocks)):
	# insert the entry if it doesn't exist
	cursor.execute('INSERT IGNORE INTO stocktable (code, name, industry, area) VALUES (%s, %s, %s, %s)'
		, (codes[i], names[i], industries[i], areas[i]))

print('stocks information inserted.')

cnx.commit()
cursor.close()

cnx.close()
