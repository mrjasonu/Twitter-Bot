import tweepy
import data
import time

auth = tweepy.OAuthHandler(data.consumer_key, data.consumer_secret_key)
auth.set_access_token(data.access_token, data.access_token_secret)

api = tweepy.API(auth)
# api.update_status('@JasonTheCoder Congratulations!!!')


def read_last_seen(FILENAME):
    with open(FILENAME) as file:
        last_seen_id = int((file.read()).strip())
    return last_seen_id

def store_last_seen(FILENAME, last_seen_id):
    with open(FILENAME, 'w') as file:
        file.write(str(last_seen_id))

def reply():
    tweets = api.mentions_timeline(read_last_seen('last_seen.txt'), tweet_mode='extended')  
    for tweet in reversed(tweets):
        if '#ultimatebot' in tweet.full_text.lower():
            print(f'{tweet.id} - {tweet.full_text}')
            api.update_status('@' +tweet.user.screen_name+'Everything works ', tweet.id)
            api.retweet(tweet.id)
            api.create_favorite(tweet.id)
            store_last_seen('last_seen.txt', tweet.id)

while True:
    reply()
    time.sleep(2)