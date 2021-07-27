import tweepy
import data
import time

auth = tweepy.OAuthHandler(data.consumer_key, data.consumer_secret_key)
auth.set_access_token(data.access_token, data.access_token_secret)

api = tweepy.API(auth)

hashtag = ['100DaysOfCode']
tweetnumber = 10

def searchbot():
    tweets = tweepy.Cursor(api.search, hashtag[0]).items(tweetnumber)
    for tweet in tweets:
        try:
            api.retweet(tweet.id)
            api.create_favorite(tweet.id)
            time.sleep(2)
            print('Done')
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

while True:
    searchbot()
    time.sleep(1000)