# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file_name, selects = None, types = None, has_headers = True, delimiter = ','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(file_name) as f:
        rows = csv.reader(f, delimiter = delimiter)
        records = []
        if has_headers:
            # Read the file readers
            headers = next(rows)
            if selects:
                indices = [headers.index(colname) for colname in selects]       # Get the indices of the column you need
                headers = selects
            else:
                indices = []

            for row in rows:
                    if not row:     # SKip rows with no data
                        continue

                    if indices:
                        row = [row[index] for index in indices]      # Just take the elements we need and discard the rest from a row
                        row = [func(val) for func, val in zip(types, row)]

                    record = dict(zip(headers, row))
                    records.append(record)
        else:
            for row in rows:
                if not row:     # SKip rows with no data
                    continue
                
                row = [func(val) for func, val in zip(types, row)]

                print("the row", row)

                record = tuple(row)
                records.append(record)         
    return records