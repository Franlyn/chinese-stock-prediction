#This project is used to project Chinese Stock Market.

#Language & Tools: Python, mySQL

#Files:
getstocks.py: used to get the code for all stocks I need
db_stock.py: create mysql database for all stocks


#Selection Method:
Take the most recent two days' data of a stock, i.e.: today & yesterday.
The stock should satisfies the following requirements:
* The stock sank more than 2% yesterday
* Today's opening price is lower than yeaterday's closing price
* Today's closing price is lower than yesterday's opening price
Note: Chinese stocks are different from the North American stocks. I gained the information from friends and the Internet. A stock that satisfies the above requirements isn't guaranteed to be worth buying.
