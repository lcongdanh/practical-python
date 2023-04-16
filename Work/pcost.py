# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    total = 0
    for line in f:
        share = int(line.split(',')[1])
        price = float(line.split(',')[2].rstrip('\n'))
        total = total + share * price
    print('The total price is', round(total,2))