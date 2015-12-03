import random
import time
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

from config import *
import preprocess_data

PERCENT_TEST_SET = 10   # Percent of data to go towards testing, remaining will go to training
VOCAB_SIZE = 10000      # Leave this at 5000, 10000 doesn't add much accuracy and takes 2x the time
NUM_CORES_UTILIZED = -1  # Leave this at -1 unless you don't want this process to hog your CPU
# Change classes by modifying LABELS in config.py

# Step 1: Load preprocessed data into all_data, which is an array of tuples (tweet, label/hashtag)
print "Loading data..."
all_data = []
for label in LABELS:
    with open(name="./corpus_preproc/" + label + ".txt", mode="r") as label_file:
        for tweet in label_file.read().splitlines():
            all_data.append((tweet, label))

# Step 2: Split data for training and testing (PERCENT_TEST_SET% for testing, the rest for training)
# Randomize the data before splitting
print "Splitting data into training and testing sets..."
random.seed = 9000
random.shuffle(all_data)
# Get tweets and labels from array of tuples (prob a better way to do this, no time)
all_tweets = list(x[0] for x in all_data)
all_labels = list(x[1] for x in all_data)
# Get data/tweets and labels/hashtags for training and testing
train_data = all_tweets[:int(len(all_data)*(100-PERCENT_TEST_SET)/100.0)]
train_labels = all_labels[:int(len(all_labels)*(100-PERCENT_TEST_SET)/100.0)]
test_data = all_tweets[int(len(all_data)*(100-PERCENT_TEST_SET)/100.0):]
test_labels = all_labels[int(len(all_labels)*(100-PERCENT_TEST_SET)/100.0):]

# Step 3: Create bag of words and generate vocabulary
print "Creating the bag of words..."
# Initialize the "CountVectorizer" object, which is scikit-learn's bag of words tool.
vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=VOCAB_SIZE)

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of
# strings. Then convert to a numpy array for ease of use.
train_data_features = vectorizer.fit_transform(train_data)
train_data_features = train_data_features.toarray()

# Step 4 (optional): Vocabulary analysis
vocab = vectorizer.get_feature_names()
# print vocab

# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features, axis=0)
# Create a list of the vocabulary words, sorted by their frequency
word_count = []
for tag, count in zip(vocab, dist):
    word_count.append((count, tag))
print "Top 50 words in vocab:", sorted(word_count, reverse=True)[:50]

# Step 5: Random Forest Classification - Training
print "\nTraining the random forest (this will take a while)..."
# Initialize a Random Forest classifier with 100 trees, use multi-threading
forest = RandomForestClassifier(n_estimators=100, n_jobs=NUM_CORES_UTILIZED)

# Fit the forest to the training set, using the bag of words as
# features and the sentiment labels as the response variable
#
# This part will take a few minutes to run
start_time = time.clock()
forest = forest.fit(train_data_features, train_labels)
print "Training done in", (time.clock() - start_time) / 60.0, "minutes"

# Step 6: Random Forest Classification - Testing
# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform(test_data)
test_data_features = test_data_features.toarray()

# Use the random forest to make label predictions
results = forest.predict(test_data_features)

# Step 7: Generate results/statistics
# Iterate through results, count the number of correct predictions
correct_count = 0.0
with open("./results/predictions.txt", "w") as results_file:
    for i in range(len(test_labels)):
        results_file.write("Tweet:     " + test_data[i] + "\nPredicted: " + results[i] + "\nActual:    " + test_labels[i] + "\n\n")
        if results[i] == test_labels[i]:
            correct_count += 1

# Print results and other information
print "\n=====RESULTS====="
print "Training Size: " + str(len(train_data)) + ", Testing Size: " + str(len(test_data)) + " (TOTAL=" + str(len(all_data)) + ")"
print "# of Classes/Labels: " + str(len(LABELS))
print "LABELS: ", sorted(LABELS)
print "Vocabulary Size:", VOCAB_SIZE

print "\nPREDICTION ACCURACY:", correct_count/len(test_labels)

# Generate a confusion matrix
my_confusion_matrix = confusion_matrix(test_labels, results, labels=sorted(LABELS))
print "Confusion Matrix:"
print "                     -Predicted-"
print "-Actual-            ",
for label in sorted(LABELS):
    print ("#"+label).ljust(20),
print ""
for row in range(len(LABELS)):
    print ("#"+sorted(LABELS)[row]).ljust(20),
    for col in range(len(LABELS)):
        print str(my_confusion_matrix[row][col]).ljust(20),
    print ""
print "================="

# Step 8: Let user input their own tweets for the classifier to predict the hashtags for
print "\nClassification complete! Moving to user input mode..."
user_tweet = ""
while True:
    user_tweet_raw = raw_input("Enter a tweet (or type \'exit\'): ")
    if user_tweet_raw == "exit":
        break
    user_tweet = preprocess_data.preprocess_tweet(user_tweet_raw)
    user_tweet_features = vectorizer.transform([user_tweet])
    user_tweet_features = user_tweet_features.toarray()
    predicted_label = forest.predict(user_tweet_features)
    print "Suggested Hashtag: #" + str(predicted_label[0])
