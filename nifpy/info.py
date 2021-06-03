import pandas as pd
import pandas_datareader as web
import datetime
import numpy as np

TODAY = datetime.date.today()
PREV = datetime.timedelta(90)

""" 

    To get the name of symbol/ticker of the stocks for which you want information you can
    look it up on https://finance.yahoo.com/ and from there you can pass the scrip name
    in the parameter where required. 

"""

""" 

    BASE_URL is the url that would be used to obtain different indexes that trade on 
    the Indian stock market. The data is fetched through Wikipedia directly. 

"""

BASE_URL = 'https://en.wikipedia.org/wiki/NIFTY_50'


def _get_tickers(table_num, row):

    """
        get_tickers function is used to get the name of different indexes along with their constituents and
        this data is fetched from Wikipedia directly.

        Parameters
        --------------------------------

        table_num : It is used to get the specific table number on which we 
                    will perform our operation and this can be identified by using pd.read_html

        row : It is used to obtain different indexes present in the table.

        Returns
        --------------------------------

        A list that contains the name of symbols that trade on that particular index.

    """


    tickers = pd.read_html(BASE_URL)[table_num]
    itr = tickers['vteNifty 200 companies.1'][row]
    itr1 = itr.replace(' ',',')
    itr2 = itr1.split(',')
    itr2 = [i + ".NS" for i in itr2]
    return itr2

def get_nifty():
    ticker = pd.read_html(BASE_URL)[1]
    nifty = [x for x in ticker.Symbol]
    return nifty

def get_sensex():
    return _get_tickers(-4, 3)

def get_nifty_next50():
    return _get_tickers(-4, 4)

def get_nifty_bank():
    return _get_tickers(-4, 5)

def get_nifty_auto():
    return _get_tickers(-4, 6)

def get_nifty_financial():
    return _get_tickers(-4, 7)

def get_nifty_fmcg():
    return _get_tickers(-4, 8)

def get_nifty_it():
    return _get_tickers(-4, 9)

def get_nifty_media():
    return _get_tickers(-4, 10)

def get_nifty_metal():
    return _get_tickers(-4, 11)

def get_nifty_pharma():
    return _get_tickers(-4, 12)

def get_nifty_psubank():
    return _get_tickers(-4,13)

def get_nifty_privatebank():
    return _get_tickers(-4, 14)

def get_nifty_realty():     
    return _get_tickers(-4, 15)


def get_closing_price(tickers, start = TODAY - PREV, end = TODAY):

    """ 

        This function returns the Closing price of a list of tickers mentioned in the parameter.
        Functions that are defined above can be directly passed to get the closing price of 
        each ticker in the index

        Parameters
        --------------------------------

        tickers : Contains a list of symbols for which the closing price will be returned

        start :   Contains the starting date from which closing price is required
                  Format: 'dd/mm/yyyy' as in '25/04/2021' 
                  Default: Three months from today's date

        end :     Contains the end date till which closing price is required
                  Format: 'dd/mm/yyyy' as in '27/04/2021' 
                  Default: Today's date

        Other than a custom list some other parameters that can be passed directly are:

        - get_sensex()
        - get_nifty_next50()
        - get_nifty_bank()
        - get_nifty_auto()
        - get_nifty_financial()
        - get_nifty_fmcg()
        - get_nifty_it()
        - get_nifty_media()
        - get_nifty_metal()
        - get_nifty_pharma()
        - get_nifty_psubank()
        - get_nifty_privatebank()
        - get_nifty_realty()
        - get_nifty()

        Returns
        --------------------------------

        A pandas dataframe that contains the closing price of all symbols passed as the 
        parameter to the function.

    """
    
    Closing = pd.DataFrame()
    for i in range(len(tickers)):
      try:
        temp = web.get_data_yahoo(tickers[i], start = start, end = end)
        temp.dropna(inplace=True)
        Closing[tickers[i]] = temp['Close']
      except:
        print("No info is available for this particular stock " + tickers[i])
    return Closing

def get_data(ticker, start = TODAY - PREV, end = TODAY):

    """ 

        This function returns the various attributes of a ticker such as the High, Low, 
        Open, Close, Volume and Adjusted Close 

        Parameters
        --------------------------------

        tickers : Contains the symbol/ticker for which various attributes will be returned

        start :   Contains the starting date
                  Format: 'dd/mm/yyyy' as in '25/04/2021' 
                  Default: Three months from today's date

        end :     Contains the end date
                  Format: 'dd/mm/yyyy' as in '27/04/2021' 
                  Default: Today's date

        Returns
        --------------------------------

        A pandas dataframe that contains various attributes of a ticker such as the High, Low, 
        Open, Close, Volume and Adjusted Close 

    """

    temp = web.get_data_yahoo(ticker, start=start, end=end)
    return temp

def get_live_price(ticker):

    """ 

        This function returns the live/latest price for the symbol that has been passed as the
        parameter.

        Parameters
        --------------------------------
        ticker : Contains the symbol/ticker for which the live price will be returned

    """

    temp = web.get_data_yahoo(ticker, TODAY - PREV)['Close']
    return np.round(temp[-1],2)

def get_summary(symbol):

    """ 

        This function returns the summary of various attributes of the symbol/ticker that 
        has been passed as the parameter.

        Parameters
        --------------------------------

        tickers : Contains the symbol/ticker for which the summary of various attributes
                  will be returned

        Returns
        --------------------------------

        A pandas dataframe that contains various attributes of a ticker such as the:
        - Previous Close
        - Open
        - Bid
        - Ask
        - Day's Range
        - 52 Week Range
        - Volume
        - Average Volume
        - Market Cap
        - Beta
        - P/E Ratio
        - EPS
        - Earnings Date
        - Forward Dividend and Yield
        - Ex-Dividend Date
        - 1 Year Target Estimate
             
    """
    
    link = pd.read_html('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)
    link1 = pd.concat([link[0], link[1]],ignore_index=True)
    link1.columns = ['Attribute', 'Value']
    return link1

def get_summary(symbol):

    """ 

        This function returns the summary of various attributes of the symbol/ticker that 
        has been passed as the parameter.

        Parameters
        --------------------------------

        tickers : Contains the symbol/ticker for which the summary of various attributes
                  will be returned

        Returns
        --------------------------------

        A pandas dataframe that contains various attributes of a ticker such as the:
        - Previous Close
        - Open
        - Bid
        - Ask
        - Day's Range
        - 52 Week Range
        - Volume
        - Average Volume
        - Market Cap
        - Beta
        - P/E Ratio
        - EPS
        - Earnings Date
        - Forward Dividend and Yield
        - Ex-Dividend Date
        - 1 Year Target Estimate
             
    """
    
    link = pd.read_html('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)
    link1 = pd.concat([link[0], link[1]],ignore_index=True)
    link1.columns = ['Attribute', 'Value']
    return link1


def get_crypto_data(symbol):

    """ 

        This function returns the various attributes of a crypto ticker such as the High, Low, 
        Open, Close, Volume and Adjusted Close.
        This is limited to the previous 100 days historical data for the coin

        Parameters
        --------------------------------

        symbol : Contains the symbol/ticker for which various attributes will be returned
        Example: crypto = get_crypto_data('BTC-USD)

        Returns
        --------------------------------

        A pandas dataframe that contains various attributes of a crypto coin such as the High, Low, 
        Open, Close, Volume and Adjusted Close 

    """

    table1 = pd.read_html('https://finance.yahoo.com/quote/' + symbol + '/history?period1=1410912000&period2=1622678400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true')
    crypto_data = table1[0][:-1]
    crypto_data['Date']= pd.to_datetime(crypto_data['Date'])
    crypto_data = crypto_data.set_index('Date')
    return crypto_data
