import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
import plotly.figure_factory as ff
import datetime
from urllib.parse import urlencode
from pandas_datareader import data as pdr

TODAY = datetime.date.today()
PREV = datetime.timedelta(600)


def moving_avg(scrip, num_days):

    """ 
        Parameters
        -------------------------------
        scrip : Used to specify the symbol/ticker for which the moving average has to be plotted
        num_days : Number of days for which moving average has to be plotted. Commonly used values
                    are 14, 20, 50, 100, 200 
        
        Returns
        --------------------------------
        Plot consisting of moving average along with the closing price
    """

    company = pdr.get_data_yahoo(scrip, start = TODAY-PREV, end = TODAY)
    company['MA-' + str(num_days)] = company['Close'].rolling(num_days).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = company.index, y = company['MA-' + str(num_days)], name = str(num_days) + "Day MA",line = dict(color='orange', width = 1.2)))
    fig.add_trace(go.Scatter(x = company.index, y = company['Close'], name = "Closing Price",line = dict(color='green', width = 1.2)))
    fig.update_xaxes(
        rangeslider_visible=True)
    fig.show()


def bollinger_bands(scrip):
    """ 
        Parameters
        -------------------------------
        scrip : Used to specify the symbol/ticker for which Bollinger Bands has to be plotted 
        
        Returns
        --------------------------------
        Plot consisting of Bollinger Bands for ticker
    """

    company = pdr.get_data_yahoo(scrip, start = TODAY-PREV, end = TODAY)
    company['20 day Close MA'] = company['Close'].rolling(20).mean()
    company['Upper'] = company['20 day Close MA'] + (2 * company['Close'].rolling(20).std())
    company['Lower'] = company['20 day Close MA'] - (2 * company['Close'].rolling(20).std())

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = company.index, y = company['20 day Close MA'],
                  name = "20 Day MA",line = dict(color='rgb(117, 112, 179)', width = 1.2)))
    fig.add_trace(go.Scatter(x = company.index, y = company['Upper'],
                             name = "Upper Limit",line = dict(color='rgb(166, 86, 40)', width = 1.2)))
    fig.add_trace(go.Scatter(x = company.index, y = company['Lower'],
                             name = "Lower Limit",line = dict(color='#FD3216', width = 1.2)))
    fig.add_trace(go.Scatter(x = company.index, y = company['Close'],
                             name = "Closing Price",line = dict(color='rgb(27, 158, 119)', width = 1.2)))#'#19D3F3'
    fig.show()

def get_chart(scrip, kind = 'line',start = TODAY-PREV, end = TODAY):

    """ 
        Parameters
        -------------------------------
        scrip : Used to specify the symbol/ticker for which historical chart has to be plotted

        kind : The type of chart - 'line' or 'area'
        
        start :   Contains the starting date
                  Format: 'dd/mm/yyyy' as in '25/04/2020' 
                  Default: 600 days from today's date

        end :     Contains the end date
                  Format: 'dd/mm/yyyy' as in '27/05/2021' 
                  Default: Today's date

        Returns
        --------------------------------
        Historical chart based on time frame
    """

    company = pdr.get_data_yahoo(scrip, start = start, end = end)
    if kind.lower() == 'line':
        fig = px.line(company, y = 'Close', x = company.index,range_x=[start,end])
        fig.update_xaxes(rangeslider_visible=True)
        fig.show()
    elif kind.lower() == 'area':
        fig = px.area(company, y = 'Close', x = company.index,range_x=[start,end])
        fig.update_xaxes(rangeslider_visible=True)
        fig.show()


# TO-DO
"""
Incorporate weighted and exponential moving average for the moving average function
"""

"""UPDATE FOR THE NEXT VERSION
    ADD timestamps such as 1m, 2m, 6m, ytd in Bollinger bands
"""