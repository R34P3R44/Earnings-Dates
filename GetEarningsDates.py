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

    dfs = {}
    current_datetime = datetime.datetime.now().strftime('%m-%d-%y %H_%M_%S')
    writer = pd.ExcelWriter('Earnings Calendar.xlsx',
                            engine='xlsxwriter',
                            engine_kwargs={'options': {'strings_to_numbers': False}})

    for earning_table in earning_tables:
        if not 'Sorry, this date currently does not have any earnings announcements scheduled' in earning_table.text:
            earning_date = earning_table['id'].replace('page', '')
            earning_date = earning_date[:3] + '_' + earning_date[3:]
            print(earning_date)
            dfs[earning_date] = pd.read_html(str(earning_table.table))[0]
            dfs[earning_date].to_excel(writer, sheet_name=earning_date, index=False)
    print('Beautifying data')
            
    writer.save()
    print('File exported ;)')
                        
GetEarningsDates()