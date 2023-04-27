# report.py
#
# Exercise 2.4
import csv
import sys
from fileparse import parse_csv
from stock import Stock


def read_portfolio(filename):
    '''Read the portfolio from the file and return a list of dict'''
    with open(filename) as lines:
        stocks = parse_csv(lines, types = [str, int, float])

    stock_instances = []
    for s in stocks:
        holding = Stock(s['name'], s['shares'], s['price'])
        stock_instances.append(holding)

    return stock_instances


def read_prices(filename):
    '''Read the stock prices from prices.csv return a dict'''
    with open(filename) as lines:
        return parse_csv(lines, types = [str, float], has_headers = False) # return a list of tuple

def compute_portfolio_price(portfolio: list):
    total_price = 0.0
    for stock in portfolio:
        total_price += stock['shares'] * stock['price']
    return total_price

def compute_portfolio_current_value(portfolio: list, current_price: dict):
    '''inputs: pices dict and portfolio dict, return the portfolio value'''
    total_value = 0.0
    for stock in portfolio:
        for key in current_price:
            if stock['name'] == key:
                total_value += stock['shares'] * current_price[key]
                break
    return total_value

def make_report(portfolio: list, prices: list):
    '''take a lists of objects and a dict of prices, return a list of tuples'''
    stock_report = []
    for stock in portfolio:
        for stock_price in prices:
            holding = []
            if stock.name == stock_price[0]:
                holding.append(stock.name)
                holding.append(stock.shares)
                holding.append(stock.price)
                price_change = round((stock_price[1] - stock.price), 2)
                holding.append(price_change)
                stock_report.append(tuple(holding))
                    
    return stock_report

def print_report(report: list):
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$"+str(price):>10s} {change:>10.2f}')


def main():
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'report file')
    
    portfolio_file = sys.argv[1]
    prices_file = sys.argv[2]

    portfolio = read_portfolio(portfolio_file)     # 'Data/portfolio.csv'
    current_price = read_prices(prices_file)       # 'Data/prices.csv'
    report = make_report(portfolio, current_price)

    headers = ('Name', 'Shares', 'Price', 'Change')
    seperate_string = '---------- ---------- ---------- -----------'

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(seperate_string)
    print_report(report)

if __name__ == '__main__':
    main()
