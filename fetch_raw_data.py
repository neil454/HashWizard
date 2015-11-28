"""
File: fetch_raw_data.py (Project 1 - HashWizard)
Authors:    Ai Onda		        aionda1@umbc.edu
            Michael Vu		    mvu2@umbc.edu
            Neil Joshi		    njoshi2@umbc.com
            Patrick Jenkins	    pjenk1@umbc.edu
            Tae Song		    jw65293@umbc.edu
Date: 12/10/15
Class: CMSC 471, Fall 2015
Instructor: Abhay Kashyap
Section: 02

    This script fetches tweets with specified hashtags using the Twitter API

"""

import tweepy
from keys import *
from config import *

TWEET_FETCH_LIMIT = 10

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
# auth.set_access_token(access_token, access_secret)     # actually we don't need this unless we access our personal timeline

api = tweepy.API(auth)

for label in LABELS:
    with open(name="./temp/" + label + ".txt", mode='w') as data_file:
        for status in tweepy.Cursor(api.search, q=label, lang=LANGUAGE_FILTER).items(TWEET_FETCH_LIMIT):
            raw_tweet = status.text.encode('UTF-8').replace('\n', ' ')
            data_file.write(raw_tweet+"\n")
            # print raw_tweet
