# pcost.py
#
# Exercise 1.27
import csv
from report import read_portfolio

def portfolio_cost(filename):
    stocks = read_portfolio(filename)
    total = 0.0
    for lineno, stock in enumerate(stocks, start = 1):
        try:
            share = stock['shares']
            price = stock['price']
            total += + share * price
        except ValueError:
            print(f'Line: {lineno}: Bad line: {stock}')

    return total

filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)