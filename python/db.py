from pymongo import MongoClient
from config.settings import MONGODB_URI, MONGODB_DB_NAME, MONGODB_COLLECTION_NAME


client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]
collection = db[MONGODB_COLLECTION_NAME]


def save_flight(flight):
    flight_data = flight.to_dict()
    result = collection.insert_one(flight_data)
    return result.inserted_id
