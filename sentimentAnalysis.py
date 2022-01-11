from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# generalSentiment: Finds the general sentiment of a particular set of tweets fetched from the
#   twitter API
def generalSentiment(tweetObj:dict)->float:
    arrayTweets = tweetObj["data"]
    
    # Set up counters for sentiment of tweet set
    numPositive, numNegative, numNeutral = 0, 0, 0

    for tweet in arrayTweets:
        print(analyzer.polarity_scores(tweet["text"]))
        sentiment = analyzer.polarity_scores(tweet["text"])["compound"]
        if (sentiment >= 0.05):
            numPositive += 1
        elif (-0.05 <= sentiment <= 0.05):
            numNeutral += 1
        else:
            numNegative += 1
        
    # Adopting sentiment score from Gabrovšek et al (2016) and adding a Laplace correction
    sentimentScore = (numPositive - numNegative) / (numPositive + numNeutral + numNegative + 3)
    return sentimentScore
