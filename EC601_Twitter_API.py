import tweepy
import json
import sys

# input the keys and secret to acquire permission of API
consumerKey = "5cQw8mSauZEG5A4Frn2uMQrnk"
consumerSecret = "Ig1myJTZOR5VF2HMezfVd2n33ZfhSIWbYUpuBfiBfSEuvwto1y"
accessToken = "1441983537008152581-tPEF6LEkZIuSfEKSc9AhBVs8tj023Y"
accessTokenSecret = "f65k2QiGQEBOvHIbVIAfU0MjTZJfLg2FMVHZcKkQqhi1M"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

KEY = input(" Input KEYWORDS that you want to find: ")
NUM = int(input("Input the NUMBER that you need : "))

LIST = []  # creat a new list to save data

search = tweepy.Cursor(api.search_tweets, KEY).items(NUM)  # use the API of search

for alltweets in search:
    LIST.append(alltweets.text)

print("This is what you want to find :", LIST)