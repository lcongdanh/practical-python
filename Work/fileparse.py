# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file, select = None, types = None, has_headers = True, delimiter = ',', silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError("select requires column headers")
    
    rows = csv.reader(file, delimiter = delimiter)

    # Reader file headers if any
    headers = next(rows) if has_headers else []

    # If specific columns were selected, make indices for filering and set output columns
    if select:
        indices = [headers.index(colname) for colname in select]       # Get the indices of the column you need
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reasons {e}")
                continue
        
        # Make a dictionary or tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
        
    return records