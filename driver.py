import pandas as pd
tickers = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[-1]

def get_ticker()


def get_nifty_it():
    tickers = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[-4]
    itr = tickers['vteNifty 200 companies.1'][9]
    itr1 = itr.replace(' ',',')
    itr2 = itr1.split(',')
    itr2 = [i + ".NS" for i in itr2]
    return itr2

res = get_nifty_it()
print(res)