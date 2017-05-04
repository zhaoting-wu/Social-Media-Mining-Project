import json
import pandas as pd
import re
import csv
import example

def word_in_text(word, text):
    if text == None:
        return False
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    else:
        return False



if __name__ == '__main__':
    #example.main()
    tweets_data_path = 'rawData.csv'
    tweets_data = []

    tweets_file = open(tweets_data_path, 'r')
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    tweets = pd.DataFrame()


    tweets['created_at'] = map(lambda tweet: tweet['created_at'], tweets_data)
    tweets['id'] = map(lambda tweet: tweet['id'], tweets_data)
    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['source'] = map(lambda tweet: tweet['source'], tweets_data)
    tweets['screen_name'] = map(lambda tweet: tweet['user']['screen_name'], tweets_data)
    tweets['location'] = map(lambda tweet: tweet['user']['location'], tweets_data)
    tweets['followers'] = map(lambda tweet: tweet['user']['followers_count'], tweets_data)
    tweets['friends'] = map(lambda tweet: tweet['user']['friends_count'], tweets_data)
    tweets['time_zone'] = map(lambda tweet: tweet['user']['time_zone'], tweets_data)
    #tweets['full_text'] = map(lambda tweet: tweet['extended_tweet']['full_text'], tweets_data)

    tweets.to_csv('data_frame.csv', sep = '\t', encoding= 'utf-8')

    print tweets

