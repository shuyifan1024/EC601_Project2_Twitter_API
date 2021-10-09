import tweepy
import json
import sys

# input the keys and secret to acquire permission of API
consumerKey = "5cQw8mS*********uMQrnk"
consumerSecret = "Ig1myJTZOR5VF**********ZfhSIWbYUpu*******vwto1y"
accessToken = "14419835**********-tPE******************s8tj023Y"
accessTokenSecret = "f65k2Qi*********bVIAfU0*************Qqhi1M"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

KEY = input("Input KEYWORDS that you want to find: ")
NUM = int(input("Input the NUMBER that you need : "))
LIST = []  # creat a new list to save data
# use the API of search
search = tweepy.Cursor(api.search_tweets, KEY).items(NUM)

for alltweets in search:
    LIST.append(alltweets.text)

#output the data
LIST = pd.DataFrame(LIST)
LIST
