import mysql.connector
import tushare

# Get a list of all stocks with tushare module
try:
	all_stocks = tushare.get_stock_basics()
except e:
	print("Failed to get stock information: " + e)

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

cnx.close()
