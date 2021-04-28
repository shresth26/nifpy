from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nifpy',
    version = '0.0.1',
    author = 'Shresth Singh',
    author_email = 'singhshresth26@gmail.com',
    description = 
                  """
                        Fetch several attributes such as closing price, live price, stock summary, 
                        index list and fundamentals such as income statement, cash flow statement
                        and balance sheet.
                  """,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license = 'MIT',
    packages = ['nifpy'],
    keywords = ['stocks', 'nifty', 'financials','algo trading'],
zip_safe = False)
