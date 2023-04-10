from fastapi import APIRouter
from utils.firebase_initialize import *
from schemas.schemas import Task

router = APIRouter()


@router.post("/tasks")
async def firebase_create_task(task: Task):
    response = firebase.database().child("tasks").push(task.dict())
    return {"message": "/firebase/task POST. {}".format(response)}


@router.get("/tasks")
async def firebase_get_tasks():
    response = firebase.database().child("tasks").get()
    tasks = None
    if response.each() is not None:
        for result in response.each():  # type:ignore
            tasks = result.val()
    return {"message": "/firebase/tasks GET. {}".format(str(tasks))}


@router.get("/tasks/{taskId}")
async def firebase_get_task(taskId: str):
    response = firebase.database().child(
        "tasks").order_by_key().equal_to(taskId).get()
    task = None
    if response.each() is not None:
        for result in response.each():  # type:ignore
            task = result.val()
    return {"message": "/firebase/task/{} GET. {}".format(taskId, str(task))}


@router.put("/tasks/{taskId}")
async def firebase_update_task(taskId: str, task: Task):
    response = firebase.database().child("tasks").child(taskId).update(task.dict())
    return {"message": "/tasks/{} PUT. {}".format(taskId, response)}


@router.delete("/tasks/{taskId}")
async def firebase_delete_task(taskId: str):
    response = firebase.database().child("tasks").child(taskId).remove()
    return {"message": "/tasks/{} DELETE. {}".format(taskId, response)}
