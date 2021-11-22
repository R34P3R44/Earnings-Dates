import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

def GetEarningsDates():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    }
    url = 'https://www.marketwatch.com/tools/earningscalendar'
    print('Connecting to marketwatch.com')

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    print('Getting content')

    tabpane = soup.find('div', 'tabpane')
    earning_tables = tabpane.find_all('div', {'id': True})
    print('Searching for data')

