from pymongo import MongoClient
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevets

def insert(data_dict):

    # update the one race named mybrevet - upsert = create if not found
    db.races.update_one({'name' : 'mybrevet'}, {'$set' : data_dict}, upsert=True)

def display():
    
    query = db.races.find_one()

    if query is None:
        return {}

    query.pop("_id") # mongodb id object is not serializable (important for jsonify)
    return query