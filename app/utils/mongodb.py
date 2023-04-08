import pymongo


def mongo_client():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    return client


def mongo_todo_database():
    client = mongo_client()
    db = client["main"]
    return db


def mongo_todo_collection():
    db = mongo_todo_database()
    collection = db["todos"]
    return collection
