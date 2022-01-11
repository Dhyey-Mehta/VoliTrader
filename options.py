import yfinance as yf
import pandas as pd
from datetime import datetime

# getOptionInfo: Returns relevant information on various options using yahoo finance
def getOptionInfo(ticker:str)->dict:
    # Makes API call
    stock = yf.Ticker(ticker)
    info = stock.info
    options_exp = stock.options[2] # Arbitrarily takes third availible expiry date

    # Fetching options data
    optionsChain = stock.option_chain(options_exp)
    calls = optionsChain[0]
    puts = optionsChain[1]

    # Info of option + underlying security 
    assetPrice = info["regularMarketPrice"]
    timetoExp = ((datetime.strptime(options_exp, r"%Y-%m-%d") - datetime.today()).days) / 365
    
    # Out of the money calls
    callsOTM = calls[calls["inTheMoney"]==False]

    # Since close to the money calls are more sensitive to implied volatility changes,
    # the algorithm selects an option with a strike price close to current market price
    option = callsOTM.iloc[[2]]

    strikePrice = option.iloc[0]["strike"]
    optionPrice = (option.iloc[0]["ask"] + option.iloc[0]["bid"])/2
    contractSymbol = option.iloc[0]["contractSymbol"]

    toReturn = {"contractSymbol":contractSymbol,
                "assetPrice":assetPrice,
                "optionPrice":optionPrice,
                "strikePrice":strikePrice,
                "timetoExp":timetoExp}
    
    return toReturn


print(getOptionInfo('^SPX'))