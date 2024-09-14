
# VoliTrader

## Overview

**VoliTrader** is a sentiment-based trading model designed to generate trades on European-style options by leveraging implied volatility. It predicts current implied volatility using historical volatility and sentiment data. The model prices options accordingly and provides trade suggestions based on the current market price of the options.

## Features

- **Sentiment Analysis with Twitter:** VoliTrader uses Twitter API v2 to collect the top 100 tweets for a specific option. These tweets, gathered between 8 a.m. and 5 p.m. EST, are analyzed using the VADER sentiment analysis tool, which is tailored for social media sentiment detection. The overall sentiment is calculated as a weighted average, with LaPlace smoothing applied to account for small datasets.
  
- **Implied Volatility & Option Pricing:** The model employs the Black-Scholes formula to derive implied volatility for various European-style option contracts. Since the model doesn't apply to American options (which can be exercised before expiry), it focuses on European options, such as index funds. Solving for implied volatility involves using the Newton-Raphson method for numerical approximation, with a default error threshold of 0.0001.

## Disclaimer

**VoliTrader is a proof of concept.** The outputs should be considered informational only and not as financial advice. Use at your own risk, and always conduct your own research before making trades.

## Helpful Resources

- [A Sentiment Analysis Approach to the Prediction of Market Volatility](https://arxiv.org/pdf/2012.05906.pdf)
- [Strategies for Trading Volatility With Options](https://www.investopedia.com/articles/investing/021716/strategies-trading-volatility-options-nflx.asp)
- [Twitter Sentiment Around Earnings Announcements](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0173151)
