import pyrebase
import os
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.

FIREBASE_API_KEY = os.environ.get("FIREBASE_API_KEY")
FIREBASE_AUTH_DOMAIN = os.environ.get("FIREBASE_AUTH_DOMAIN")
FIREBASE_DATABASE_URL = os.environ.get("FIREBASE_DATABASE_URL")
FIREBASE_PROJECT_ID = os.environ.get("FIREBASE_PROJECT_ID")
FIREBASE_STORAGE_BUCKET = os.environ.get("FIREBASE_STORAGE_BUCKET")
FIREBASE_MESSAGING_SENDER_ID = os.environ.get("FIREBASE_MESSAGING_SENDER_ID")
FIREBASE_APP_ID = os.environ.get("FIREBASE_APP_ID")
FIREBASE_MEASUREMENT_ID = os.environ.get("FIREBASE_MEASUREMENT_ID")


fireBaseConfig = {
    'apiKey': FIREBASE_API_KEY,
    'authDomain': FIREBASE_AUTH_DOMAIN,
    'databaseURL': FIREBASE_DATABASE_URL,
    'projectId': FIREBASE_PROJECT_ID,
    'storageBucket': FIREBASE_STORAGE_BUCKET,
    'messagingSenderId': FIREBASE_MESSAGING_SENDER_ID,
    'appId': FIREBASE_APP_ID,
    'measurementId': FIREBASE_MEASUREMENT_ID
}

firebase = pyrebase.initialize_app(fireBaseConfig)
auth = firebase.auth()
db = firebase.database()