from datetime import datetime
import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
import bs4

""" 

    To get the name of symbol/ticker of the stocks for which you want information you can
    look it up on https://finance.yahoo.com/ and from there you can pass the scrip name
    in the parameter where required. 

"""

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Pragma': 'no-cache',
    'Referrer': 'https://google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

def _calculate_financials(symbol, statement):

    """

        calculate_financials function is used to fetch and preprocess the financial documents
        from the Yahoo Finance website.

        Parameters
        --------------------------------

        symbol :    It is used to specify the symbol/ticker for which the 
                    financials have to be fetched

        statement : The name of the financial statement that has to be fetched.
                    Categories = [
                                  'balance-sheet' : Fetches the balance sheet,
                                  'cash-flow' :     Fetches the cash flow statement,
                                  'financials' :    Fetches the income statement
                                 ]

        Returns
        --------------------------------
        
        A dataframe that contains the required financial statement.

    """

    headers = []
    temp_list = []
    label_list = []
    final = []
    index = 0
    url = 'https://finance.yahoo.com/quote/' + symbol + '/' + statement + '?p=' + symbol
    page = requests.get(url, headers)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    features = soup.findAll('div', class_='D(tbr)')
    for item in features[0].find_all('div', class_='D(ib)'):
        headers.append(item.text)
    while index <= len(features) - 1:
        temp = features[index].findAll('div', class_='D(tbc)')
        for line in temp:
            temp_list.append(line.text)
        final.append(temp_list)
        temp_list = []
        index += 1

    df = pd.DataFrame(final[1:])
    df.columns = headers

    return df

def get_balance_sheet(symbol):

    """ 

        Used to obtain the balance sheet of the specified ticker

        Parameters
        --------------------------------

        symbol :    It is used to specify the symbol/ticker for which the 
                    balance sheet has to be fetched

        Returns
        --------------------------------
        
        A dataframe that contains the balance sheet of the company
    
    """

    bal_sheet = _calculate_financials(symbol, 'balance-sheet')
    return bal_sheet

def get_cash_flow(symbol):

    """ 

        Used to obtain the cash flow statement of the specified ticker

        Parameters
        --------------------------------

        symbol :    It is used to specify the symbol/ticker for which the 
                    cash flow has to be fetched

        Returns
        --------------------------------
        
        A dataframe that contains the cash flow statement of the company
    
    """

    cash_flow = _calculate_financials(symbol, 'cash-flow')
    return cash_flow

def get_income_statement(symbol):

    """ 

        Used to obtain the income statement of the specified ticker

        Parameters
        --------------------------------

        symbol :    It is used to specify the symbol/ticker for which the 
                    income statement has to be fetched

        Returns
        --------------------------------
        
        A dataframe that contains the income statement of the company
    
    """

    inc_statement = _calculate_financials(symbol, 'financials')
    return inc_statement

