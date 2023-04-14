from fastapi.testclient import TestClient
from app.main import app
from app.schemas.schemas import Task

client = TestClient(app)


def test_create_task():
    task = Task(title="New Task create by test_firebase.py",
                description="Decription of new Task create by test_firebase.py", completed=False)
    response = client.post("/use-postgresql/tasks/", json=task.dict())
    successResponse = {
        "message": "Task Created"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]


def test_get_tasks():
    response = client.get("/use-postgresql/tasks/")
    successResponse = {
        "message": "Successfully get all tasks"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]


def test_get_task():
    tastId = 5
    response = client.get("/use-postgresql/tasks/{}".format(tastId))
    assert response.status_code == 200


def test_update_task():
    tastId = 6
    task = Task(title="Update New Task create by test_firebase.py",
                description="Update Decription of new Task create by test_firebase.py", completed=False)
    response = client.put(
        "/use-postgresql/tasks/{}".format(tastId), json=task.dict())
    assert response.status_code == 200


def test_delete_task():
    tastId = 9
    response = client.delete(
        "/use-postgresql/tasks/{}".format(tastId))
    successResponse = {
        "message": "Successfully delete task"
    }
    assert response.status_code == 200
    assert response.json()["message"] == successResponse["message"]
