# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file_name, select = None, types = None, has_headers = True, delimiter = ',', silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(file_name) as f:
        rows = csv.reader(f, delimiter = delimiter)
        records = []
        if has_headers:
            # Read the file readers
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]       # Get the indices of the column you need
                headers = select
            else:
                indices = []

            for rowno, row in enumerate(rows, 1):
                    if not row:     # SKip rows with no data
                        continue

                    if indices:
                        row = [row[index] for index in indices]      # Just take the elements we need and discard the rest from a row
                    
                    try:
                        if types:
                            row = [func(val) for func, val in zip(types, row)]

                        record = dict(zip(headers, row))
                        records.append(record)
                    except ValueError as e:
                        if silence_errors:
                            pass
                        else:
                            print(f"Row {rowno}: Couldn't convert {row}")
                            print(f"Row {rowno}: Reasons {e}")
        else:
            for row in rows:
                if not row:     # SKip rows with no data
                    continue
                
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                record = tuple(row)
                records.append(record)         
    return records