
import tweepy
from keys import *


auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
#auth.set_access_token(access_token, access_secret)     # actually we don't need this unless we access our personal timeline


api = tweepy.API(auth)

# for status in tweepy.Cursor(api.user_timeline).items(200):
#     print status

trends = api.trends_place(1)
#print trends

hashtags = [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]
for i in range(5):      # seems like I can't get more than 5...
    print hashtags[i]

places = api.geo_search(query="United States", granularity="country")
place_id = places[0].id

for status in tweepy.Cursor(api.search, q="place:" + place_id + " " + "TheWalkingDead", geocode="39.252099,-76.823111,3000mi").items(10):
    print(status)
