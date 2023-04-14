from fastapi import APIRouter, HTTPException
from app.utils.mongodb_crud import *
from app.schemas.schemas import Task
from app.schemas.schemas import Response

router = APIRouter()


@router.post("/tasks")
async def mongodb_create_task(task: Task):
    response = mongo_create_task(task=task)
    if response is not None:
        return Response(status="Ok",
                        code="200",
                        message="Task Created", result=None).dict(exclude_none=True)
    else:
        raise HTTPException(status_code=401, detail="Task not created")


@router.get("/tasks")
async def mongodb_get_tasks(skip: int = 0, limit: int = 100):
    tasks = mongo_get_tasks(skip=skip, limit=limit)
    return Response(status="Ok",
                    code="200",
                    message="Successfully get all tasks", result=tasks).dict(exclude_none=True)


@router.get("/tasks/{taskId}")
async def mongodb_get_task(taskId: str):
    task = mongo_get_task(taskId=taskId)
    if task is not None:
        return Response(status="Ok",
                        code="200",
                        message="Successfully get task", result=task).dict(exclude_none=False)
    else:
        return Response(status="Ok",
                        code="200",
                        message="Task with this given id not found").dict(exclude_none=False)


@router.put("/tasks/{taskId}")
async def mongodb_update_task(taskId: str, task: Task):
    response = mongo_update_task(taskId=taskId, task=task)
    if response is not None:
        return Response(status="Ok",
                        code="200",
                        message="Successfully update task").dict(exclude_none=False)
    else:
        return Response(status="Ok",
                        code="200",
                        message="Task with this given id not found").dict(exclude_none=False)


@router.delete("/usemongodb/tasks/{taskId}")
async def mongodb_delete_task(taskId: str):
    response = mongo_delete_task(taskId=taskId)
    return Response(status="Ok",
                    code="200",
                    message="Successfully delete task", result=response).dict(exclude_none=False)
