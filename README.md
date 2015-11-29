# HashWizard
A program that predicts and suggests Twitter Hashtags based on a given tweet.
Created by Team Hotline Bling for CMSC471.

## IMPORTANT NOTE FOR GROUP MEMBERS
When creating commits, make sure you're only adding/modifying important files.
If you're using PyCharm (highly recommended), DO NOT commit any files from the 
.idea folder, as those files are specific to your PyCharm workspace.
Using PyCharm's built-in Version Control Software should prevent any headaches.

## Dependencies
 - Python (Anaconda Python 2.7 Recommended: https://www.continuum.io/downloads)
 - Tweepy (https://github.com/tweepy/tweepy#installation)

## TODO
 - Finalize list of hashtag labels (Narrow down to 5 or 10?)
 - Finalize method of fetching tweets (should be good now, ~~but we should narrow to English tweets only~~)
 - Fetch 1000? tweets for each hashtag
 - Preprocess data:
    - Filter out garbage tweets somehow?
    - ~~Remove excess tweet metadata (only use actual tweet for now)~~
    - ~~Remove label hashtag in actual tweet (remove other hashtags as well?)~~
    - ~~Remove other tweet junk (links, etc.)~~
    - ~~Filter out unimportant key words in tweet (unless we can use tools to do this for us)~~
 - Look for some libraries that can automatically do classification based on text content (Word2Vec is good)
    - If it can filter out unimportant parts of the text data, that would help a lot

## Notes
 - Twitter API only allows fetching tweets from the past week, so our hashtag labels should be fairly current
 - 