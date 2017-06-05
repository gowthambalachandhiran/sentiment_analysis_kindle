from tweetpy import *
import re
import json
from pprint import pprint
import unicodecsv
import csv

try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 	'757845079977439232-H3fBRlJeSQ9FO2KuegCXACltg7rZ6V4'
ACCESS_SECRET = 'nVpcbAyN7ZAmjZ3zpZFZAyqWRayRgwd207zKYxjzvbc3U'
CONSUMER_KEY = 'b50Z4BqdjF7QgZdBubFvZdE0f'
CONSUMER_SECRET = 'vk875skjomkWJKOZPNVniO6biW8FzVkV6McRUOdj9GwTRFoPLH'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="#kindle",language="en",replies="all")
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10000000


file = "C:\\Users\\WELCOME\\Desktop\\twitterfeeds_1.csv"
with open(file,"w",encoding='utf-8',newline='') as csvfile:
    fieldnames=['Username','Tweet','Timezone','Timestamp','Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in iterator:
        #pprint(tweet)
        username = tweet['user']['screen_name']
        print (username)
        tweet_text = tweet['text']
        print (tweet_text)
        user_timezone = tweet['user']['time_zone']
        print(user_timezone)
        tweet_timestamp=tweet['created_at']
        print (tweet_timestamp)
        user_location =tweet['user']['location']
        print (user_location)
        #print (tweet)
        tweet_count -= 1
        writer.writerow({'Username':username,'Tweet':tweet_text,'Timezone':user_timezone,'Location':user_location,'Timestamp':tweet_timestamp})


        if tweet_count <= 0:
            break