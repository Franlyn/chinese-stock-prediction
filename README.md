This project is used to project Chinese Stock Market.

Files:
getstocks.py: used to get the code for all stocks I need
db_stock.py: create mysql database for all stocks

'''
Selection Method:
Take the most recent two days' data of a stock, i.e.: today & yesterday.
The stock should satisfies the following requirements:
1. The stock sank more than 2% yesterday
2. Today's opening price is lower than yeaterday's closing price
3. Today's closing price is lower than yesterday's opening price
'''