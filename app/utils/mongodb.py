import os
import pymongo
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.

mongo_uri = os.environ.get("MONGO_URI")


def mongo_client():
    client = pymongo.MongoClient(mongo_uri)
    return client


def mongo_todo_database():
    client = mongo_client()
    db = client["main"]
    return db


def mongo_todo_collection():
    db = mongo_todo_database()
    collection = db["todos"]
    return collection
