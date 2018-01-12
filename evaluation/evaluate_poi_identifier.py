#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.cross_validation import train_test_split
features_train, features_test,labels_train, labels_test = train_test_split (features,\
	labels, test_size = 0.3, random_state = 42)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
print "accuracy: ", clf.score(features_test, labels_test)

pred = clf.predict(features_test)

num_pois = 0

for i in pred:
	if i == 1:
		num_pois += 1

print "number of POIs predicted: ", num_pois
print "total number of people in test set:", len(pred)

true_positives = 0
false_positives = 0
false_negatives = 0

for i, j in zip(pred,labels_test):
	if i == 1 and j == 1:
		true_positives += 1
	elif i == 1 and j == 0:
		false_positives += 1
	elif i == 0 and j == 0:
		false_negatives += 1

print "true positives: ", true_positives
print "false positives: ", false_positives
print "false negatives: ", false_negatives

print "precision: ", true_positives /(true_positives + false_positives)
print "recall: ", true_positives / (true_positives + false_negatives)

# another way 
from sklearn import metrics
print "precision: ", metrics.precision_score(labels_test, pred)
print "recall: ", metrics.recall_score(labels_test, pred)
