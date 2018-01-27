import tweepy as tp
from time import time
import csv


consumer_key = "EqgbbGiU0DqxEawMOFIYXG9SQ"
consumer_secret = "9TWLaawIUJ8NGiXbTRcf6ablz6EDECbDatzag0ld5WnBg2W7Rj"
access_token = "957345473576275968-ugTVpRBp4vSgAJj9nJTrYVS2S6E6UlV"
access_token_secret = "3vQQasBocZAMaqdrtzmlWCQfMh62N2T9E3a2zmz4PF7Qu"

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth)

start_time = time()


class MyStreamListener(tp.StreamListener):
    def on_status(self, status):
        if time() - start_time <60:
            print(status.user.location, status.text)
            return True
        else:
            return False

    # def on_data(self, raw_data):
    #     print(raw_data)
    #     return True
    def on_error(self, status_code):
        print("ERROR: " + str(status_code))
        return False

 



myStreamListener = MyStreamListener()

myStream = tp.Stream(auth=api.auth, listener=MyStreamListener())

myStream.filter(languages=['en'], track=['a'])
