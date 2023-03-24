import yfinance as yf
import pandas as pd

tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0].Symbol
tickers = tickers.to_list()

print(tickers)
