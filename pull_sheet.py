import csv
import gspread
from sys import argv

def write_worksheet(worksheet, f):
    with open(f, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(worksheet.get_all_values())

def main():
    URL = argv[1]
    TARGET = argv[2]

    print('Authenticating')
    gc = gspread.service_account('service-token.json')
    
    print('Opening sheet')
    sheet = gc.open_by_url(URL)
    worksheets = sheet.worksheets()

    print(f'Found {len(worksheets)} worksheets')
    
    for worksheet in worksheets:
        title = worksheet.get('A1')[0][0]
        if title.endswith('.bytes'):
            title = title.replace('.bytes', '.csv')
            print(f'Writing {title}')
            write_worksheet(worksheet, f'{TARGET}/{title}')

    print('Done')

if __name__ == '__main__':
    main()
