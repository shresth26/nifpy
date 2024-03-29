import pandas as pd
import yfinance as web
import numpy as np
from .constants import *


def get_closing_data(tickers, start=TODAY - PREV, end=TODAY) -> pd.DataFrame:
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

        Returns
        --------------------------------

        A pandas dataframe that contains the closing price of all symbols passed as the
        parameter to the function.

    """

    tickers = [ticker + '.NS' for ticker in tickers]
    Closing = pd.DataFrame()
    for i in range(len(tickers)):
        try:
            temp = web.download(tickers[i], start=start, end=end)
            temp.dropna(inplace=True)
            Closing[tickers[i]] = temp['Close']
        except:
            print("No info is available for this particular stock " + tickers[i])
    return Closing


def get_stock_data(ticker, start=TODAY - PREV, end=TODAY) -> pd.DataFrame:
    """

        This function returns the various attributes of a ticker such as the High, Low,
        Open, Close, Volume and Adjusted Close

        Parameters
        --------------------------------

        ticker : Contains the symbol/ticker for which various attributes will be returned

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

    if '.NS' not in ticker:
        ticker = ticker + '.NS'
    temp = web.download(ticker, start=start, end=end)
    return temp


def live_price(ticker) -> float:
    """

        This function returns the live/latest price for the symbol that has been passed as the
        parameter.

        Parameters
        --------------------------------
        ticker : Contains the symbol/ticker for which the live price will be returned

    """

    if '.NS' not in ticker:
        ticker = ticker + '.NS'
    temp = web.download(ticker, TODAY - PREV)['Close']
    return np.round(temp[-1], 2)


def stock_summary(ticker) -> pd.DataFrame:
    """

        This function returns the summary of various attributes of the symbol/ticker that
        has been passed as the parameter.

        Parameters
        --------------------------------

        ticker : Contains the symbol/ticker for which the summary of various attributes
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

    link = pd.read_html('https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker)
    link1 = pd.concat([link[0], link[1]], ignore_index=True)
    link1.columns = ['Attribute', 'Value']
    return link1
