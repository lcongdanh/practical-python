from follow import follow
import report
import csv
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price','change'])
    return rows

def print_report(dicts, formatter):
    formatter.headings(['Name','Price','Change'])
    for dict in dicts:
        rowdata = [dict['name'], f'{dict["price"]:0.2f}', f'{dict["change"]:0.2f}']
        formatter.row(rowdata)

def ticker(portfoliodata, logfile, fmt):
    portfolio = report.read_portfolio(portfoliodata)
    rows = parse_stock_data(follow(logfile))

    rows = (row for row in rows if row['name'] in portfolio)

    formatter = tableformat.create_formatter(fmt)
    print_report(rows, formatter)

""" if __name__ == '__main__':
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row) """