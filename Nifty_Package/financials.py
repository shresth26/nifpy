from datetime import datetime
import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
import bs4

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Pragma': 'no-cache',
    'Referrer': 'https://google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

def calculate_financials(symbol, statement):
    headers = []
    temp_list = []
    label_list = []
    final = []
    index = 0
    url = 'https://finance.yahoo.com/quote/' + symbol + '/' + statement + '?p=' + symbol
    page = requests.get(url, headers)
    soup = bs4.BeautifulSoup(page.content,'html.parser')
    features = soup.findAll('div', class_ = 'D(tbr)')
    for item in features[0].find_all('div', class_='D(ib)'):
        headers.append(item.text)
    while index <= len(features) - 1:
      temp = features[index].findAll('div', class_='D(tbc)')
      for line in temp:
        temp_list.append(line.text)
      final.append(temp_list)
      temp_list = []
      index+=1

    df = pd.DataFrame(final[1:])
    df.columns = headers

    return df

def get_balance_sheet(symbol):
    bal_sheet = calculate_financials(symbol, 'balance-sheet')
    return bal_sheet

def get_cash_flow(symbol):
    cash_flow = calculate_financials(symbol, 'cash-flow')
    return cash_flow

def get_income_statement(symbol):
    cash_flow = calculate_financials(symbol, 'financials')
    return cash_flow

get_balance_sheet('RELIANCE.NS')
