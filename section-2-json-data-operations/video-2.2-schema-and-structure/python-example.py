#-------------------------------------------------------------------------------
# Name:        mongodb
# Purpose:     Learn MongoDB
#
# Author:      Daniel Watrous
#
# Created:     08/14/2014
# Copyright:   (c) Daniel Watrous 2014
# Licence:     PackT
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from pymongo import MongoClient
import json

database_name = "coursetracker"
collection_name = "student"

class student:
    name = {}
    email = ""
    major = ""

    def __init__(self, firstname, lastname, email, major):
        self.name = {"first": firstname, "last": lastname}
        self.email = email
        self.major = major

    def to_JSON(self):
        return json.dumps(self.__dict__)

def main():
    # create a new student object
    a_student = student("Daniel", "Watrous", "daniel@mongocourse.com", "Electrical Engineering")

    # connect to MongoDB
    client = MongoClient()
    coursetracker_database = client[database_name]
    student_collection = coursetracker_database[collection_name]

    # insert the student object into MongoDB
    object_id = student_collection.insert(a_student.to_JSON())
    print("New ObjectId: %s" % object_id)

    # retrieve the student object from MongoDB
    retrieved_object = student_collection.find_one()
    print(retrieved_object)

    # create a new student object from the document we got back from MongoDB
    mongo_student = student(retrieved_object["name"]["first"],
                            retrieved_object["name"]["last"],
                            retrieved_object["email"],
                            retrieved_object["major"])
    print(mongo_student.name["first"])
    #print(retrieved_object["name"]["middle"]) # this will throw a KeyError

if __name__ == '__main__':
    main()
