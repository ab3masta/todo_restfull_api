from fastapi import APIRouter, HTTPException
from ..utils.mongodb_crud import *
from ..schemas.schemas import Task

router = APIRouter()


@router.get("/")
async def root():
    return "Todo RestFull API"


@router.post("/tasks")
async def create_todo(task: Task):
    response = mongo_create_task(task=task)
    return {"message": "/task POST. {}".format(response)}


@router.get("/tasks")
async def read_todos(skip: int = 0, limit: int = 100):
    tasks = mongo_get_tasks(skip=skip, limit=limit)
    return {"message": "/tasks GET", "tasks": tasks}


@router.get("/tasks/{taskId}")
async def read_todo(taskId: str):
    task = mongo_get_task(taskId=taskId)
    if task is None:
        return HTTPException(status_code=404, detail="Todo not found")
    return {"message": "/tasks/{} GET".format(taskId), "tasks": task}


@router.put("/tasks/{taskId}")
async def update_todo(taskId: str, task: Task):
    response = mongo_update_task(taskId=taskId, task=task)
    return {"message": "/tasks/{} PUT. {}".format(taskId, response)}


@router.delete("/tasks/{taskId}")
async def delete_todo(taskId: str):
    response = mongo_delete_task(taskId=taskId)
    return {"message": "/tasks/{} DELETE. {}".format(taskId, response)}
