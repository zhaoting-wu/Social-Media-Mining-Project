from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv

# Go to http://apps.twitter.com and create an app.
#  The consumer key and secret will be generated for you after
consumer_key='vHUK0M1Y41WN6U9cMab55mp2K'
consumer_secret='7e8LzkfHM4u881MAppqeTzT6OUCUVOf8rsh7vquRKTExcOTt8M'
# After the step above, you will be redirected to your app's page.
#  Create an access token under the the "Your access token" section
access_token='1446514944-cRo3Zdc2JJnL7CG9qIyDvbIQhqv8BbyjohFNdJG'
access_token_secret='k32ta8P2OPb5lpE9Hl4CQ6IWXxu3RaIkl4DVczTRDqV81'
class StdOutListener(StreamListener):
    """ 
    A listener handles tweets that are received from the stream.     
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        with open('rawData.csv', 'a') as f:
            f.write(data)
        #global text
        #text.write(data)
        #print(type(data))
        #print shape(data)
        return True
    def on_error(self, status):
        print(status)
if __name__ == '__main__':
    #global text
    #text = open('text.txt', 'w')
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['flu','cough'], languages=['en'])
    #text.close()