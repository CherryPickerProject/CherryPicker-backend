# A MongoDB Atlas DB cluster has been set up
from pymongo import MongoClient
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
now = datetime.now()
now_in_singapore = now.astimezone(SGT)

# ensure only latest 3 collections in DB at any one time
existingCollections = db.list_collection_names()

if(len(existingCollections) > 2):
    minDate = existingCollections[0].split('_')[1]
    for i in range(1,len(existingCollections)):
        if(existingCollections[i].split('_')[1]<minDate):
            minDate = existingCollections[i].split('_')[1]
    db.drop_collection('venue_'+minDate)
    collections = db.list_collection_names()
    

venue = db['venue_'+now.strftime("%Y-%m-%d %H:%M:%S")]

# load data to mongo
for filename in os.listdir(directory):
    if filename.endswith('.json'):
       print("Seeding ", os.path.splitext(os.path.basename(filename))[0], "into DB")
       data =[]
       with open(directory+filename, encoding='utf-8') as write_file:
           json_data = json.load(write_file)
       venue.insert_many(json_data)

