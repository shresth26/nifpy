import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime
import numpy as np

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

res = get_nifty_auto()
print(res)
