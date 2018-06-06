from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
#TextBlob iteself gives you the sentiment polarity from -1 to 1 with -1 being negative, 0 is neutral and 1 being positive


def percentage(part, whole):
    return 100 * float(part) / float(whole)


consumerKey = 'xsaoUwHoyqgkU4mWNl42UxzL4'
consumerSecret = 'ckUYqvErRcZoRZQNqNlW5WrvTnrrQ57n1MAzWxyaSM0kRHxJ5w'
accessToken = '2954792182-HPM3ilDe9kaYHDWsh5a54mImcwe0VcXz8p4Vp7c'
accessTokenSecret = 'QcXGLl6oUKxtStCYkbhLtjSChYoGZFhbxqLRfludbcI1s'

# Connection with the API
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# input for term to be searched and how many tweets to search
searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

# searching for tweets
tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)
positive = 0
negative = 0
neutral = 0
polarity = 0 #polarity is the average sentiment of all tweets

for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity #adding up polarities to find the average later

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)



#format each of the variables to 2 decimal places
positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

labels = ['Positive ['+str(positive)+'%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on '+searchTerm+' by analyzing '+str(noOfSearchTerms)+' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
