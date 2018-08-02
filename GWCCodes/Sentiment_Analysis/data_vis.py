import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Continue program below
#json object or tweets are stored in tweetData


#iterate list of tweets
    #for each tweet access text
    #print polarity
polarityList = []
subjectivityList = []
all_the_tweets = ''

for tweet in tweetData:
    words = tweet["text"]
    tweetblob = TextBlob(words)
    polarityList.append(tweetblob.polarity)

    subjectivityList.append(tweetblob.subjectivity)

    all_the_tweets += words

plt.hist(polarityList, bins=[-1.1, -1.0, 0.0, 0.1, 0.2, 0.5, 0.7, 0.9, 1.0, 1.1])
plt.xlabel("Polarity Scale")
plt.ylabel("Number of Tweets")
plt.show()

#print subjectivity and polarity
plt.plot(polarityList, subjectivityList, 'ro')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.title('Tweet Polarity vs Subjectivity')
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()

tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

#wordcloud setup
allBlob = TextBlob(all_the_tweets)
