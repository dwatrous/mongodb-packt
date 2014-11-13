#!/usr/bin/env python
from pymongo import MongoClient, ReadPreference
import ssl

def main():
    # open connection and authenticate as read only user
    client = MongoClient('mongodb://localhost:27017/statsdb',
                         read_preference=ReadPreference.SECONDARY)

    # get handle for statsdb and statistics collection
    db = client.statsdb
    collection = db.statistics
    
    # retrieve and output one document
    print collection.find_one()

if __name__ == '__main__':
    main()
