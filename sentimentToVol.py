import pandas
import numpy as np
from sklearn import linear_model

# A function to convert sentiment values into a 
#   predicted volatility score
def sentimentToVol(sentimentScore):
    # Use historical sentiment and volatility data to from linear regression
    dataFrame = pandas.read_csv("./data.csv")
    reg = linear_model.LinearRegression()
    reg.fit(dataFrame[["senti"]].values,dataFrame.vol)

    return reg.predict([[sentimentScore]])[0]/100



