import tweepy
import data


auth = tweepy.OAuthHandler(data.consumer_key, data.consumer_secret_key)
auth.set_access_token(data.access_token, data.access_token_secret)

api = tweepy.API(auth)
api.update_status('@JasonTheCoder Congratulations!!!')
