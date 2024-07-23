from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

def check_page():
    url = "https://classes.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1249&subject=MATH&cournum=235"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find_all('table')[1]
    row = table.find_all('tr')[7]
    enrol = row.find_all('td')[7]
    total = row.find_all('td')[6]
    return enrol.text == total.text


def main():
    date = ""
    while True:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'checking... [{date}]')
        if not check_page():
            break
        time.sleep(60)

    print(f"Spot open! - {date}")

if __name__ == '__main__':
    main()