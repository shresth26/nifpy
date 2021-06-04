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
    company = pdr.get_data_yahoo(scrip, start = TODAY-PREV, end = TODAY)
    company['MA-' + str(num_days)] = company['Close'].rolling(num_days).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = company.index, y = company['MA-' + str(num_days)], name = str(num_days) + "Day MA",line = dict(color='orange', width = 1.2)))
    fig.add_trace(go.Scatter(x = company.index, y = company['Close'], name = "Closing Price",line = dict(color='green', width = 1.2)))
    fig.update_xaxes(
        rangeslider_visible=True)
    fig.show()

"""UPDATE FOR THE NEXT VERSION
    ADD timestamps such as 1m, 2m, 6m, ytd in Bollinger bands
"""

def bollinger_bands(scrip):
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
    company = pdr.get_data_yahoo(scrip, start = start, end = end)
    if kind == 'line':
        fig = px.line(company, y = 'Close', x = company.index,range_x=[start,end])
        fig.update_xaxes(rangeslider_visible=True)
        fig.show()
    elif kind == 'area':
        fig = px.area(company, y = 'Close', x = company.index,range_x=[start,end])
        fig.update_xaxes(rangeslider_visible=True)
        fig.show()

