# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv


def read_portfolio(filename): 
    '''Read the portfolio from the file and return a list of dict'''
    portfolio = parse_csv(filename, types = [str, int, float])
    return portfolio

def read_prices(filename):
    '''Read the stock prices from prices.csv return a dict'''
    stock_prices = parse_csv(filename, types = [str, float], has_headers=False) # return a list of tuple
    return stock_prices

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
    '''take lists of portfolio dicts and dict of prices, return a list of tuples of stock report'''
    stock_report = []
    for stock in portfolio:
        for stock_price in prices:
            holding = []
            if stock['name'] == stock_price[0]:
                holding.append(stock['name'])
                holding.append(stock['shares'])
                holding.append(stock['price'])
                price_change = round((stock_price[1] - stock['price']), 2)
                holding.append(price_change)
                stock_report.append(tuple(holding))
                    
    return stock_report

def print_report(report: list):
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$"+str(price):>10s} {change:>10.2f}')
    print('\n')

portfolio = read_portfolio('Data/portfolio.csv')
current_price = read_prices('Data/prices.csv')
report = make_report(portfolio, current_price)


headers = ('Name', 'Shares', 'Price', 'Change')
seperate_string = '---------- ---------- ---------- -----------'


""" print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(seperate_string)
print_report(report) """
