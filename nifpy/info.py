import constants
import pandas as pd
import yfinance as web
import datetime
import numpy as np

TODAY = datetime.date.today()
PREV = datetime.timedelta(90)

#modify this in new feature
# def get_nifty():
#     ticker = pd.read_html(constants.BASE_URL)[2]
#     print(ticker)
#     return ticker

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
        temp = web.download(tickers[i], start = start, end = end)
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

    temp = web.download(ticker, start=start, end=end)
    return temp

def get_live_price(ticker):

    """ 

        This function returns the live/latest price for the symbol that has been passed as the
        parameter.

        Parameters
        --------------------------------
        ticker : Contains the symbol/ticker for which the live price will be returned

    """

    temp = web.download(ticker, TODAY - PREV)['Close']
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
