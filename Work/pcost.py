# pcost.py
#
# Exercise 1.27
import csv
from report import read_portfolio
import sys

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


def main():
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'pcost file')
    
    portfolio_file = sys.argv[1]
    cost = portfolio_cost(portfolio_file)
    print('Total cost:', cost)

if __name__ == '__main__':
    main()