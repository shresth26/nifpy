# Nifty_API


## Methods

- [get_live_price](#get_live_price)
- [get_summary](#get_summary)
- [get_data](#)
- [get_closing_price](#)
- [get_balance_sheet](#get_balance_sheet)
- [get_cash_flow](#get_cash_flow)
- [get_income_statement](#get_income_statement)

#### Indexes

- [get_nifty](#)
- [get_sensex](#)
- [get_nifty_next50](#)
- [get_nifty_bank](#)
- [get_nifty_auto](#)
- [get_nifty_financial](#)
- [get_nifty_fmcg](#)
- [get_nifty_it](#)
- [get_nifty_media](#)
- [get_nifty_metal](#)
- [get_nifty_pharma](#)
- [get_nifty_psubank](#)
- [get_nifty_privatebank](#)
- [get_nifty_realty](#)

### get_live_price
``` python 
import nifpy
price = get_live_price(ticker)
print(price)

""" 

This function returns the live/latest price for the symbol that has been passed as the parameter

Parameters
-------------------------------
ticker : Contains the symbol/ticker for which the live price will be returned

"""

#Example
price = get_live_price('ITC.NS')
```

### get_summary
``` python 
import nifpy
summary = get_summary(symbol)
print(summary)

""" 

This function returns the summary of various attributes of the symbol/ticker that has been passed as the parameter

Parameters
-------------------------------
tickers : Contains the symbol/ticker for which the summary of various attributes will be returned

Returns
-------------------------------
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

#Example
summary = get_summary('MARUTI.NS')
```

### get_balance_sheet
``` python 
from nifpy import financials
balance_sheet = get_balance_sheet(symbol)
print(balance_sheet)

""" 
Used to obtain the balance sheet of the specified ticker

Parameters
-------------------------------
symbol : It is used to specify the symbol/ticker for   which the balance sheet has to be fetched

Returns
--------------------------------
A dataframe that contains the balance sheet othe company

"""

#Example
balance_sheet = get_balance_sheet('RELIANCE.NS')
```

### get_cash_flow
``` python 
from nifpy import financials
cash_flow = get_cash_flow(symbol)
print(cash_flow)

""" 

Used to obtain the cash flow statement of the specified ticker

Parameters
-------------------------------
symbol : It is used to specify the symbol/ticker for which the cash flow has to be fetched

Returns
--------------------------------
A dataframe that contains the cash flow statement of the company
    
"""

#Example
cash_flow = get_cash_flow('HCLTECH.NS')
```

### get_income_statement
``` python 
from nifpy import financials
inc_statement = get_income_statement(symbol)
print(inc_statement)

""" 

Used to obtain the income statement of the specified ticker

Parameters
-------------------------------
symbol : It is used to specify the symbol/ticker for which the income statement has to be fetched

Returns
--------------------------------
A dataframe that contains the income statement of the company
    
"""

#Example
inc_statement = get_income_statement('TITAN.NS')
```