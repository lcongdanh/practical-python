# report.py
#
# Exercise 2.4
import csv

def read_prices(filename):
    '''Read the stock prices from prices.csv return a dict'''
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        stock_prices = {}
        for line in lines:
            try:
                stock_prices[line[0]] = float(line[1])
            except:
                print("Something was wrong with the file that you're reading")
                print('The lines:',line)
    return stock_prices

def read_portfolio(filename):
    '''Read the portfolio from the file and return a list'''
    with open(filename, 'rt') as file:
        lines = csv.reader(file)
        next(lines)
        portfolio = []
        for line in lines:
            holding = {}
            try:
                holding['name'] = line[0]
                holding['shares'] = int(line[1])
                holding['price'] = float(line[2])
            except:
                print('Something wrong with the file')
                print('The line is', line)
            portfolio.append(holding)
    return portfolio


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

def make_report(portfolio: list, prices: dict):
    '''take lists of portfolio dicts and dict of prices, return a list of tuples of stock report'''
    stock_report = []
    for stock in portfolio:
        for key in prices:
            holding = []
            try:
                if stock['name'] == key:
                    holding.append(stock['name'])
                    holding.append(stock['shares'])
                    holding.append(stock['price'])
                    price_change = round((prices[key] - stock['price']),2)
                    holding.append(price_change)
                    stock_report.append(tuple(holding))
                    break
            except:
                print('Something was wrong in key', key, prices[key])
                    
    return stock_report

def print_report(report: list):
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$"+str(price):>10s} {change:>10.2f}')
    print('\n')

portfolio = read_portfolio('Data/portfolio.csv')
current_price = read_prices('Data/prices.csv')

print(portfolio,'\n')
print(current_price,'\n')

""" portfolio_price = compute_portfolio_price(portfolio)
print('The portfolio price:', portfolio_price)

current_value = compute_portfolio_current_value(portfolio, current_price)
print('The current value of the portfolio:', current_value) """

""" gain_lost = current_value - portfolio_price
if gain_lost > 0:
    print('The portfolio has gain:', gain_lost)
else:
    print('The portfolio has lost', round(abs(gain_lost),2)) """

report = make_report(portfolio, current_price)

headers = ('Name', 'Shares', 'Price', 'Change')
seperate_string = '---------- ---------- ---------- -----------'
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(seperate_string)
print_report(report)
