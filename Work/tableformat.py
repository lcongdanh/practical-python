
class TextTableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter():
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter():
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>', end='')
        print()

    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<th>{r}</th>', end = '')
        print('</tr>', end='')
        print()


def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unkown format {fmt}')
    
    return formatter
