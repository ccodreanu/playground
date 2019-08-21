import pymongo
import datetime
import pprint

from pymongo import MongoClient

client = MongoClient('172.28.128.3', 27017)

db = client.yuge_deitabeis

stuff = db.pile_of_stuff

single_stuff = {
    "name": "this stuff has a name",
    "tags": [
        "good",
        "stuff"
    ],
    "date": datetime.datetime.utcnow()
}

what_was_inserted = stuff.insert_one(single_stuff)

print("=== printintg the obj id of the inserted doc")
print(what_was_inserted.inserted_id)

print("=== retrieving a doc by its name")
pprint.pprint(stuff.find_one({"name": "this stuff has a name"}))

print("=== retrieving no more than 3 docs")
for ss, kk in zip(stuff.find(), range(3)):
    pprint.pprint(ss)