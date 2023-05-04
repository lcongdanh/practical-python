# pcost.py
#
# Exercise 1.27
import csv
import report
import sys

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main():
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'pcost file')
    
    portfolio_file = sys.argv[1]        # Get the file path
    cost = portfolio_cost(portfolio_file)
    print('Total cost:', cost)

if __name__ == '__main__':
    main()