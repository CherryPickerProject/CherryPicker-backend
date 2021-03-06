# A MongoDB Atlas DB cluster has been set up
from pymongo import MongoClient, TEXT
from datetime import datetime
import pytz
import os
import json

SGT = pytz.timezone('Asia/Singapore')

directory = './Data/'
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
print("connecting to mongoDB")
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.get_database('CherryPickerDB')

db.drop_collection('venues')
venue = db['venues']
now = datetime.now()
now_in_singapore = now.astimezone(SGT).strftime("%Y-%m-%d %H:%M:%S")

# load data to mongo
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        print("Seeding ", os.path.splitext(
            os.path.basename(filename))[0], "into DB")
        data = []
        with open(directory+filename, encoding='utf-8') as write_file:
            json_data = json.load(write_file)
            # add in updateOn attribute into each of the venue object
            for data in json_data:
                data["updatedOn"] = now_in_singapore
                print(data)

        venue.insert_many(json_data)

# TODO: (Explore MongoDB Atlas Full search Text -> This part creates the indexes in the collection)
# (MongoDB Full text search is still the secondary backup source we use for querying hence not doing this now)
# https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.index_information
# # Create Index on mongo

# print(venue.index_information())
# if (venue.index_information().length() == 0):
#     print("Creating Index in db")
#     venue.create_index(
#         [("description", TEXT), ("tags", TEXT),
#          ("location", TEXT), ("title", TEXT), ("facilities", TEXT)]
#     )
# else:
#     print("Index already existing")
