# Chinese Stocks Prediction
The project gets data on all Chinese stocks, and uses a selecting method (described below) to select the stocks that have a bigger chance to grow in the next few days.

## Language & Tools:
Python, mySQL
Modulos: mysql.connector, tushare, time

## Files:
getstocks.py: used to get data for all stocks and insert into the sql table.
eachstock_db.py: create table for each stock.
updateStock.py: insert data of stocks into the tables created by eachstock.db every day.
selection.py: Go through the data, find the stocks that satisfied the requirements mentioned below. If more than 30% of the stocks are selected, return None.


## Stocks Selecting Method:
Take the most recent two days' data of a stock, i.e.: today & yesterday.
The stock should satisfies the following requirements:
* The stock sank more than 2% yesterday
* Today's opening price is lower than yeaterday's closing price
* Today's closing price is lower than yesterday's opening price
Note: Chinese stocks are different from the North American stocks. I gained the information from friends and the Internet. A stock that satisfies the above requirements isn't guaranteed to be worth buying.
