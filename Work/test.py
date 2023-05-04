""" import report
from tableformat import create_formatter, print_table


portfolio = report.read_portfolio('Data/portfolio.csv')
formatter = create_formatter('txt')
print_table(portfolio, ['name','shares', 'price'], formatter) """


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares



class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass