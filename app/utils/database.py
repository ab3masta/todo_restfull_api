from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

mongo_uri = os.environ.get("MONGO_URI")
postgres_uri = os.environ.get("POSTGRES_URI")

# ----------------  MongoDB


def mongo_client():
    client = pymongo.MongoClient(mongo_uri)
    return client


def mongo_task_database():
    client = mongo_client()
    db = client["main"]
    return db


def mongo_task_collection():
    db = mongo_task_database()
    collection = db["tasks"]
    return collection

# ----------------  Postgres


engine = create_engine(postgres_uri)  # type:ignore
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
