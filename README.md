# HashWizard
A program that predicts and suggests Twitter Hashtags based on a given tweet.
Created by Team Hotline Bling for CMSC471.

## IMPORTANT NOTE FOR GROUP MEMBERS
When creating commits, make sure you're only adding/modifying important files.
If you're using PyCharm (highly recommended), DO NOT commit any files from the 
.idea folder, as those files are specific to your PyCharm workspace.
Using PyCharm's built-in Version Control Software should prevent any headaches.

Also, before you start working and before you commit anything, 
PULL FROM THE REPO FIRST!
Merging can be a headache when dealing with conflicting files.

## Dependencies
 - Python (Anaconda Python 2.7 Recommended: https://www.continuum.io/downloads)
 - Tweepy (https://github.com/tweepy/tweepy#installation)
 - gensim (http://radimrehurek.com/gensim/apiref.html)

## TODO
 - Classification using simple word frequency
 - More advanced classification using Word2Vec to improve accuracy maybe

## Notes
 - Twitter API only allows fetching tweets from the past week, so our hashtag labels should be fairly current
 