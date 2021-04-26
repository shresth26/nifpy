from setuptools import setup

setup(
    name='nifpy',
    version = '0.1',
    author = 'Shresth Singh',
    author_email = 'singhshresth26@gmail.com',
    description = 
                  """
                        Fetch several attributes such as closing price, live price, stock summary, 
                        index list and fundamentals such as income statement, cash flow statement
                        and balance sheet.
                  """,

    license = 'MIT',
    packages = ['nifpy'],
    keywords = ['stocks', 'nifty', 'financials','algo trading'],
zip_safe = False)