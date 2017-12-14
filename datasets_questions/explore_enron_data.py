#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

people = 0
poiCount = 0

print "features for each person", len(enron_data["SKILLING JEFFREY K"])

for person in enron_data:
	people += 1
	if enron_data[person]['poi'] == 1:
		poiCount += 1

print "people:", people 
print "Enron data poi count:", poiCount

poiFile = open("../final_project/poi_names.txt")
poiCount_total = 0
lines = poiFile.readlines()
for line in lines:
	if line[0] == '(':
		poiCount_total +=1
		
print "Total POIs:", poiCount_total

print "James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Wesley Colwell:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]