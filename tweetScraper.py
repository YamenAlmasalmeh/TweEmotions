import tweepy as tp
import textblob as tb
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

with open("PositiveTweets.csv", "w",newline='') as data:
    datawriter = csv.writer(data)
    datawriter.writerow(["Location", "Tweet", "Positivity"])

with open("NegativeTweets.csv", "w", newline='') as data:
    datawriter = csv.writer(data)
    datawriter.writerow(["Location", "Tweet", "Positivity"])

with open("NeutralTweets.csv", "w", newline='') as data:
    datawriter = csv.writer(data)
    datawriter.writerow(["Location", "Tweet", "Positivity"])

def remove_non_ascii(text):
    return ''.join(i if ord(i)<128 else ' ' for i in text)


class MyStreamListener(tp.StreamListener):

    def on_status(self, status):
        if time() - start_time <600:
            if tb.TextBlob(remove_non_ascii(status.text)).sentiment.polarity > 0:
                with open("PositiveTweets.csv", 'a', newline='') as data:
                    dataWriter = csv.writer(data)
                    dataWriter.writerow([remove_non_ascii(str(status.user.location)), remove_non_ascii(status.text), \
                            str(tb.TextBlob(remove_non_ascii(status.text)).sentiment.polarity)])
            elif tb.TextBlob(remove_non_ascii(status.text)).sentiment.polarity < 0:
                with open("NegativeTweets.csv", 'a', newline='') as data:
                    dataWriter = csv.writer(data)
                    dataWriter.writerow([remove_non_ascii(str(status.user.location)), remove_non_ascii(status.text), \
                            str(tb.TextBlob(remove_non_ascii(status.text)).sentiment.polarity)])
            else:
                with open("NeutralTweets.csv", 'a', newline='') as data:
                    dataWriter = csv.writer(data)
                    dataWriter.writerow([remove_non_ascii(str(status.user.location)), remove_non_ascii(status.text), \
                                         str(tb.TextBlob(remove_non_ascii(status.text)).sentiment.polarity)])
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

myStream.filter(languages=["en"],track=['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

