import tweepy
from keys import *

WOEID_UNITED_STATE = 23424977

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)     # actually we don't need this unless we access our personal timeline

api = tweepy.API(auth)

# for status in tweepy.Cursor(api.user_timeline).items(200):
#     print status

# trends = api.trends_place(WOEID_UNITED_STATE, include="hashtags")
#
# hashtags = [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]
# for hashtag in hashtags:
#     print hashtag

places = api.geo_search(query="United States", granularity="country")
place_id = places[0].id

# for status in tweepy.Cursor(api.search, q="place:" + place_id + " " + "HurricaneSandy", geocode="39.252099,-76.823111,3000mi").items(10):
#     print(status)

for status in tweepy.Cursor(api.search, q="BlackLivesMatter", lang="en").items(10):
    raw_tweet = status.text.encode('UTF-8').replace('\n',' ')
    print raw_tweet
