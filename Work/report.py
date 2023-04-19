# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for line in lines:
            holding = {
                'name': line[0],
                'shares': int(line[1]),
                'price': float(line[2])
            }
            portfolio.append(holding)
    return portfolio