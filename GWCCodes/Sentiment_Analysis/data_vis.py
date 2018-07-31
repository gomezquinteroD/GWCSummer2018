import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
