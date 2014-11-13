#-------------------------------------------------------------------------------
# Name:        generate-log-data
# Purpose:     This module generates fictitious log data to expore
#              aggregation framework
#
# Author:      Daniel Watrous
#
# Created:     10/15/2014
# Copyright:   (c) Daniel Watrous 2014
# Python ver:  3.x
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import random, string, csv

actions = ['VIEW', 'DOWNLOAD', 'UPDATE']
cookies = [['auth', 'lastpage', 'firstvisit'], ['session', 'guest', 'lastpage'], ['session', 'admin']]

with open('generate-log-data-objectids.txt') as f:
    objectids = f.read().splitlines()

with open('generate-log-data-objectids-owner.txt') as f:
    owner_objectids = f.read().splitlines()

with open('generate-log-data-ipaddresses.txt') as f:
    ipaddresses = f.read().splitlines()

with open('generate-log-data-documents.txt') as f:
    documents = f.read().splitlines()

cities = [] # http://www.golombek.com/locations.html
with open('generate-log-data-cities.csv') as f:
    next(f)
    reader = csv.reader(f, quoting=csv.QUOTE_ALL)
    for row in reader:
        cities.append(row)

for objectid in objectids:
    city = random.choice(cities)
    action = random.choice(actions)
    document = 'db.statistics.insert({"_id": ObjectId("%s"), "request_ip": "%s", "owner": ObjectId("%s"), "request_date": ISODate("2014-%02d-%02dT%02d:%02d:%02d.%03dZ"), "request_method": "GET", "request_uri": "api.myapplication.com/v1/document/%s", "action": "%s", "request_time_milliseconds": %d,"loc": [%s, %s], cookies: [%s]})' % (
                 objectid,
                 random.choice(ipaddresses),
                 random.choice(owner_objectids),
                 random.randrange(8,11), random.randrange(1,29), random.randrange(0,23), random.randrange(0,59), random.randrange(0,59), random.randrange(0,999),
                 random.choice(documents),
                 action,
                 random.randrange(24,468 if action == "VIEW" else 1073),
                 float(city[2]), float(city[1]),
                 ",".join(map(repr, random.choice(cookies))))
    print(document)

    #print("2014-%02d-%02dT%02d:%02d:%02d.%03dZ" % (random.randrange(8,11), random.randrange(1,29), random.randrange(0,23), random.randrange(0,59), random.randrange(0,59), random.randrange(0,999)))
    #print(".".join(map(str, (random.randint(0, 255) for _ in range(4)))))  # IP Address
    #print(''.join(random.choice(string.hexdigits.lower()) for _ in range(9)))  # document ID

