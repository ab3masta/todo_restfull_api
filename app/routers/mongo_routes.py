from fastapi import APIRouter, HTTPException
from utils.mongodb_crud import *
from schemas.schemas import Task

router = APIRouter()


@router.post("/tasks")
async def mongodb_create_task(task: Task):
    response = mongo_create_task(task=task)
    return {"message": "/task POST. {}".format(response)}


@router.get("/tasks")
async def mongodb_get_tasks(skip: int = 0, limit: int = 100):
    tasks = mongo_get_tasks(skip=skip, limit=limit)
    return {"message": "/tasks GET", "tasks": tasks}


@router.get("/tasks/{taskId}")
async def mongodb_get_task(taskId: str):
    task = mongo_get_task(taskId=taskId)
    if task is None:
        return HTTPException(status_code=404, detail="Todo not found")
    return {"message": "/tasks/{} GET".format(taskId), "tasks": task}


@router.put("/tasks/{taskId}")
async def mongodb_update_task(taskId: str, task: Task):
    response = mongo_update_task(taskId=taskId, task=task)
    return {"message": "/tasks/{} PUT. {}".format(taskId, response)}


@router.delete("/usemongodb/tasks/{taskId}")
async def mongodb_delete_task(taskId: str):
    response = mongo_delete_task(taskId=taskId)
    return {"message": "/tasks/{} DELETE. {}".format(taskId, response)}
