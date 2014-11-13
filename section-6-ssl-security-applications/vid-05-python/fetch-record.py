#!/usr/bin/env python
from pymongo import MongoClient
import ssl

def main():
    # open connection and authenticate as read only user
    client = MongoClient('mongodb://statsdb_ro:secret@localhost:16687/statsdb',
                         ssl=True,
                         ssl_certfile='/etc/ssl/mongo-client.pem',
                         ssl_ca_certs='/etc/ssl/mongod.pem')

    # get handle for statsdb and statistics collection
    db = client.statsdb
    collection = db.statistics
    
    # retrieve and output one document
    print collection.find_one()

if __name__ == '__main__':
    main()
