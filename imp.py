import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime
import numpy as np

TODAY = datetime.date.today()
PREV = datetime.timedelta(90)

BASE_URL = 'https://en.wikipedia.org/wiki/NIFTY_50'
def get_tickers(table_num, row):
    tickers = pd.read_html(BASE_URL)[table_num]
    itr = tickers['vteNifty 200 companies.1'][row]
    itr1 = itr.replace(' ',',')
    itr2 = itr1.split(',')
    itr2 = [i + ".NS" for i in itr2]
    return itr2

def get_sensex():
    return get_tickers(-4, 3)

def get_nifty_next50():
    return get_tickers(-4, 4)

def get_nifty_bank():
    return get_tickers(-4, 5)

def get_nifty_auto():
    return get_tickers(-4, 6)

def get_nifty_financial():
    return get_tickers(-4, 7)

def get_nifty_fmcg():
    return get_tickers(-4, 8)

def get_nifty_it():
    return get_tickers(-4, 9)

def get_nifty_media():
    return get_tickers(-4, 10)

def get_nifty_metal():
    return get_tickers(-4, 11)

def get_nifty_pharma():
    return get_tickers(-4, 12)

def get_nifty_psubank():
    return get_tickers(-4,13)

def get_nifty_privatebank():
    return get_tickers(-4, 14)

def get_nifty_realty():     
    return get_tickers(-4, 15)

def get_nifty():
    ticker = pd.read_html(BASE_URL)[1]
    nifty = [x for x in ticker.Symbol]
    return nifty

# rek = get_nifty()
# print(rek)

def get_closing_price(tickers):
    Closing = pd.DataFrame()
    for i in range(len(tickers)):
      try:
        temp = web.get_data_yahoo(tickers[i], TODAY - PREV)
        temp.dropna(inplace=True)
        Closing[tickers[i]] = temp['Close']
      except:
        print("No info is available for this particular stock " + tickers[i])
    return Closing

# res = get_closing(get_nifty_it())
# print(res)

def get_price(ticker, prev = TODAY - PREV, today = TODAY):
    temp = web.get_data_yahoo(ticker, start=prev, end=today)
    return temp


def get_live_price(ticker):
    temp = web.get_data_yahoo(ticker, TODAY - PREV)['Adj Close']
    print(np.round(temp[-1],2))

def get_summary(symbol):
    link = pd.read_html('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)
    link1 = pd.concat([link[0], link[1]],ignore_index=True)
    link1.columns = ['Attribute', 'Value']
    print(link1)

get_live_price('GRASIM.NS')


# get_summary('RELIANCE.NS')