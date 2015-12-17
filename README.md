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
 - Numpy (http://www.numpy.org/) - Included in Anaconda Python
 - Scikit-learn (http://scikit-learn.org/stable/) - Included in Anaconda Python
 
## Usage Instructions
 - Modify LABELS in config.py to change the type of class problem desired
 - Use fetch_raw_data.py to get raw twitter data (already done)
 - Use preprocess_data.py to clean the raw twitter data (already done)
 - Run classification.py to calculate accuracy and allow user input

## TODO
 - Improve accuracy (low-priority)
     - Use Word2Vec to group similar words
     - Heavier pre-processing on raw data
     - Tweak some variables

## Notes
 - Twitter API only allows fetching tweets from the past week, so our hashtag labels should be fairly current
 