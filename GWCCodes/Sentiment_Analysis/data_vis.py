import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Continue program below
#json object or tweets are stored in tweetData


#iterate list of tweets
    #for each tweet access text
    #print polarity
polarityList = []

for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    polarityList.append(tweetblob.polarity)

print(polarityList)

tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
