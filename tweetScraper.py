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

def remove_non_ascii(text):
    return ''.join(i if ord(i)<128 else ' ' for i in text)


class MyStreamListener(tp.StreamListener):

    def on_status(self, status):
        if time() - start_time <120:
            with open("data.csv", 'a') as data:
                dataWriter = csv.writer(data)
                dataWriter.writerow([remove_non_ascii(str(status.user.time_zone)), remove_non_ascii(status.text)])
            print(status.user.time_zone," ", status.text)
            return True
        else:
            return False

    def on_error(self, status_code):
        print("ERROR: " + str(status_code))
        return True

    def on_timeout(self):
        print("Timeout...")
        return True

myStreamListener = MyStreamListener()

myStream = tp.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(languages=['en'], track=['a'])

