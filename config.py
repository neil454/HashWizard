"""
File: config.py (Project 1 - HashWizard)
Authors:    Ai Onda		        aionda1@umbc.edu
            Michael Vu		    mvu2@umbc.edu
            Neil Joshi		    njoshi2@umbc.com
            Patrick Jenkins	    pjenk1@umbc.edu
            Tae Song		    jw65293@umbc.edu
Date: 12/10/15
Class: CMSC 471, Fall 2015
Instructor: Abhay Kashyap
Section: 02

    This file has any universal constants, flags, etc. for HashWizard

"""
# All 16 Hashtags (all data collected)
# LABELS = ["BlackLivesMatter", "PlannedParenthood", "TheWalkingDead", "GameOfThrones",  "PrayForParis", "BlackFriday", "HappyThanksgiving", "FeelTheBern", "ClimateMarch", "NFL", "SyrianRefugees", "Trump", "MLB", "NBA", "NHL", "Soccer"]

# Best 10 performing classes
LABELS = ["PlannedParenthood", "TheWalkingDead", "FeelTheBern", "ClimateMarch", "NFL", "Trump", "MLB", "NBA", "NHL", "Soccer"]

# Genre-specific Hashtags:
# LABELS = ["TheWalkingDead", "GameOfThrones"]      # Television
# LABELS = ["NFL", "MLB", "NBA", "NHL", "Soccer"]   # Sports
# LABELS = ["FeelTheBern", "Trump"]                 # Politics

LANGUAGE_FILTER = "en"
TWEET_FETCH_LIMIT = 10000