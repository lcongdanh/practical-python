# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        headers = next(lines)
        total = 0
        for line in lines:
            share_raw = line[1]
            price_raw = line[2]
            try:
                share_int = int(share_raw)
                price_float = float(price_raw)
                total = total + share_int * price_float
            except:
                print('Bad line:', line)
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print('I\'ve come here')
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)