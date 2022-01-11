import yfinance as yf
import pandas as pd

table = yf.Ticker("^SPX").option_chain('2022-01-21')

