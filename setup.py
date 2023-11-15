from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nifpy',
    version = '1.4.0',
    author = 'Shresth Singh',
    author_email = 'singhshresth26@gmail.com',
    description = 
                  """
                        Easy to use python package that can be used to fetch live price, closing price, stock summary, 
                        index list and fundamentals such as income statement, cash flow statement
                        and balance sheet for stocks that trade on the National Stock Exchange(NSE).
                        Package has been updated and now supports crypto currency.
                  """,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/shresth26/nifpy',
    license = 'MIT',
    packages = ['nifpy'],
    keywords = ['stocks', 'nifty', 'financials','algo trading','nse','crypto','cryptocurrency','sensex'],
zip_safe = False)
