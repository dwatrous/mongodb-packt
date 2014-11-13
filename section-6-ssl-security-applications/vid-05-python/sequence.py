#!/usr/bin/env python
from pymongo import MongoClient
from bson.objectid import ObjectId
import ssl
import datetime

def main():
    # open connection and authenticate as read only user
    client = MongoClient('mongodb://statsdb_rw:secret@localhost:16687/statsdb',
                         ssl=True,
                         ssl_certfile='/etc/ssl/mongo-client.pem',
                         ssl_ca_certs='/etc/ssl/mongod.pem')

    # get handle for statsdb and statistics collection
    db = client.statsdb
    collection = db.statistics
    
    # create a document to insert
    stats_doc = {
        "request_ip": "1.1.1.1",
        "owner": ObjectId('543f227c0208373c53ba4b28'),
        "request_date": datetime.datetime.utcnow(),
        "request_method": "GET",
        "request_uri": "api.myapplication.com/v1/document/f9b09e246.py",
        "action": "VIEW",
        "request_time_milliseconds": 12,
        "loc": [-121.89, 37.3378],
        "cookies": ["python"]
    }
    
    # insert the new document
    collection.insert(stats_doc)
    
    # retrieve and display the new document
    print collection.find_one({"request_ip": "1.1.1.1"})

if __name__ == '__main__':
    main()
