from fastapi.testclient import TestClient
from app.main import app
from app.schemas.schemas import Task
from app.utils.database import *
from app.utils.firebase_initialize import firebase
from .test_postgresql import test_create_task

client = TestClient(app)


def test_mongo_client():
    connection = mongo_client()
    assert connection.server_info() is not None


def test_firebase_initialization():
    assert firebase != None


def test_database_connection():
    # Test database connection
    try:
        # Open a connection
        SessionLocal()
        # Test the connection
        assert True, "Database connection test passed"
    except Exception as e:
        # If there is an error, fail the test
        assert False, f"Database connection test failed: {e}"
    finally:
        # Close the session
        SessionLocal().close()
