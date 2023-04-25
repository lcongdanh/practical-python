# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    print(f'File name: {filename}')
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        header = next(lines)
        total = 0.0
        for lineno, line in enumerate(lines, start = 1):
            stock = dict(zip(header,line))
            try:
                share = int(stock['shares'])
                price = float(stock['price'])
                total += + share * price
            except ValueError:
                print(f'Line: {lineno}: Bad line: {line}')

    return total

filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)