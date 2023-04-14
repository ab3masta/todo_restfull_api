from fastapi.testclient import TestClient
from app.main import app
from app.schemas.schemas import Task
import json

client = TestClient(app)


def test_create_task():
    task = Task(title="New Task create by test_firebase.py",
                description="Decription of new Task create by test_firebase.py", completed=False)
    response = client.post("/use-firebase/tasks/", json=task.dict())
    successResponse = {
        "message": "Task Created"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]


def test_get_tasks():
    response = client.get("/use-firebase/tasks/")
    successResponse = {
        "message": "Successfully get all tasks"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]


def test_get_task():
    tastId = "-NSwFSzM1GNHdWzMB9mh"
    response = client.get("/use-firebase/tasks/{}".format(tastId))
    successResponse = {
        "message": "Successfully get task"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]


def test_update_task():
    tastId = "-NSwFSzM1GNHdWzMB9mh"
    task = Task(title="Update New Task create by test_firebase.py",
                description="Update Decription of new Task create by test_firebase.py", completed=False)
    response = client.put(
        "/use-firebase/tasks/{}".format(tastId), json=task.dict())
    successResponse = {
        "message": "Successfully update task"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]


def test_delete_task():
    tastId = "-NSwFSzM1GNHdWzMB9mh"
    response = client.delete(
        "/use-firebase/tasks/{}".format(tastId))
    successResponse = {
        "message": "Successfully delete task"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]
