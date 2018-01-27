import tweepy as tp
import requests
import csv

consumer_key = "EqgbbGiU0DqxEawMOFIYXG9SQ"
consumer_secret = "9TWLaawIUJ8NGiXbTRcf6ablz6EDECbDatzag0ld5WnBg2W7Rj"
access_token = "957345473576275968-ugTVpRBp4vSgAJj9nJTrYVS2S6E6UlV"
access_token_secret = "3vQQasBocZAMaqdrtzmlWCQfMh62N2T9E3a2zmz4PF7Qu"

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print (tweet.text)
