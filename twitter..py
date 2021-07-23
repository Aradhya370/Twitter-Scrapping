import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
import numpy as np
import re
import pandas as pd

consumer_key = "zvghpJLaBrHdUqloJDlcV7rum"
consumer_sec = "BKvbGtBlMBUPn9ONG1x7LrYkLclA2sRXT5G4KuGZiPgGlnNq2R"
access_token = "1383703955218132994-lz4OavJh4DLABqVo4SBnjzqSWw72vE"
access_token_sec = "oj254ngv1FjYnVveQOL1SQuRxOtR88xkROqaXSm8zalPQ"
# create an authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_sec)
# set the access token and access token secret
auth.set_access_token(access_token, access_token_sec)
# create an API object
api_connect = tweepy.API(auth)
text1 = input("enter the subject")
tweet_data = api_connect.search(text1, count=100)
df = pd.DataFrame([tweet.text for tweet in tweet_data], columns=['Tweets'])


def cleantxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text


df['Tweets'] = df['Tweets'].apply(cleantxt)


# function to get subjectivity
def getsubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

9
# function to get polarity
def getpolarity(text):
    return TextBlob(text).sentiment.polarity


df['Subjectivity'] = df['Tweets'].apply(getsubjectivity)
df['Polarity'] = df['Tweets'].apply(getpolarity)


# function to get analysis
def getAnalysis(x):
    if (x < 0):
        return 'Negative'
    elif (x == 0):
        return 'Neutral'
    elif (x > 0):
        return 'Positive'


df['Analysis'] = df['Polarity'].apply(getAnalysis)
print(df)
# plot the graph between Subjectivity and polarity
plt.figure(figsize=(8, 6))
for i in range(0, df.shape[0]):
   plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')
plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()

df['Analysis'].value_counts()
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind='bar')
plt.show()