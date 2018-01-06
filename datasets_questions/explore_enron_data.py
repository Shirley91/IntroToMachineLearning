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

most_paid = ''
highest_payment = 0

for key in ('LAY KENNETH L', 'FASTOW ANDREW S', 'SKILLING JEFFREY K'):
	if enron_data[key]['total_payments'] > highest_payment:
		highest_payment = enron_data[key]['total_payments']
		most_paid = key
print most_paid, highest_payment

# how is an unfilled feature denoted?
print(enron_data['SKILLING JEFFREY K'])

# how many folks have a quantified salary?
print len(dict((key,value) for key, value in enron_data.items() if value["salary"] != 'NaN'))

# how many with a known email address?
print len(dict((key,value) for key, value in enron_data.items() if value["email_address"] != 'NaN'))

# percentage of people in the dataset have 'NaN' for their total payments?
no_total_payments = len(dict((key,value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))
print float(no_total_payments) / len(enron_data) * 100

#percentage of POIs in the data have 'NaN' for their total payments?
POIs = dict((key,value) for key, value in enron_data.items() if value['poi'] == True)
no_total_payments_POIs = len(dict((key,value) for key, value in POIs.items() if value["total_payments"] == 'NaN'))
print float(no_total_payments_POIs) / len(POIs) * 100

# new number of people with NaN total_payments with adding 10 POIs with NaN total_payments
print len(enron_data) + 10
print no_total_payments + 10
print len(POIs) + 10
print float(10) / (len(POIs) + 10) * 100