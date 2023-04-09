from fastapi import APIRouter, HTTPException
from ..utils.mongodb_crud import *
from ..schemas.schemas import Task
from ..utils.firebase_initialize import *
router = APIRouter()


@router.get("/")
async def root():
    return "Todo RestFull API"


@router.post("/usemongodb/tasks")
async def mongodb_create_task(task: Task):
    response = mongo_create_task(task=task)
    return {"message": "/task POST. {}".format(response)}


@router.get("/usemongodb/tasks")
async def mongodb_get_tasks(skip: int = 0, limit: int = 100):
    tasks = mongo_get_tasks(skip=skip, limit=limit)
    return {"message": "/tasks GET", "tasks": tasks}


@router.get("/usemongodb/tasks/{taskId}")
async def mongodb_get_task(taskId: str):
    task = mongo_get_task(taskId=taskId)
    if task is None:
        return HTTPException(status_code=404, detail="Todo not found")
    return {"message": "/tasks/{} GET".format(taskId), "tasks": task}


@router.put("/usemongodb/tasks/{taskId}")
async def mongodb_update_task(taskId: str, task: Task):
    response = mongo_update_task(taskId=taskId, task=task)
    return {"message": "/tasks/{} PUT. {}".format(taskId, response)}


@router.delete("/usemongodb/tasks/{taskId}")
async def mongodb_delete_task(taskId: str):
    response = mongo_delete_task(taskId=taskId)
    return {"message": "/tasks/{} DELETE. {}".format(taskId, response)}


# ---------------------

@router.post("/firebase/tasks")
async def firebase_create_task(task: Task):
    response = firebase.database().child("tasks").push(task.dict())
    return {"message": "/firebase/task POST. {}".format(response)}


@router.get("/firebase/tasks")
async def firebase_get_tasks():
    response = firebase.database().child("tasks").get()
    tasks = None
    if response.each() is not None:
        for result in response.each():
            tasks = result.val()
    return {"message": "/firebase/tasks GET. {}".format(str(tasks))}


@router.get("/firebase/tasks/{taskId}")
async def firebase_get_task(taskId: str):
    response = firebase.database().child(
        "tasks").order_by_key().equal_to(taskId).get()
    task = None
    if response.each() is not None:
        for result in response.each():
            task = result.val()
    return {"message": "/firebase/task/{} GET. {}".format(taskId, str(task))}


@router.put("/firebase/tasks/{taskId}")
async def firebase_update_task(taskId: str, task: Task):
    response = firebase.database().child("tasks").child(taskId).update(task.dict())
    return {"message": "/tasks/{} PUT. {}".format(taskId, response)}


@router.delete("/firebase/tasks/{taskId}")
async def firebase_delete_task(taskId: str):
    response = firebase.database().child("tasks").child(taskId).remove()
    return {"message": "/tasks/{} DELETE. {}".format(taskId, response)}
