from fastapi import APIRouter, HTTPException
from app.utils.firebase_initialize import *
from app.schemas.schemas import Task
from app.schemas.schemas import Response

router = APIRouter()


@router.post("/tasks")
async def firebase_create_task(task: Task):
    response = firebase.database().child("tasks").push(task.dict())

    if response is not None:
        return Response(status="Ok",
                        code="200",
                        message="Task Created", result=None).dict(exclude_none=True)
    else:
        raise HTTPException(status_code=401, detail="Task not created")


@router.get("/tasks")
async def firebase_get_tasks():
    response = firebase.database().child("tasks").get()
    tasks = []
    if response.each() is not None:
        for result in response.each():  # type:ignore
            tasks.append(result.val())
    return Response(status="Ok",
                    code="200",
                    message="Successfully get all tasks", result=tasks).dict(exclude_none=True)


@router.get("/tasks/{taskId}")
async def firebase_get_task(taskId: str):
    response = firebase.database().child(
        "tasks").order_by_key().equal_to(taskId).get()
    task = None
    if response.each() is not None:
        for result in response.each():  # type:ignore
            task = result.val()

    if task is not None:
        return Response(status="Ok",
                        code="200",
                        message="Successfully get task", result=task).dict(exclude_none=False)
    else:
        return Response(status="Ok",
                        code="200",
                        message="Task with this given id not found").dict(exclude_none=False)


@router.put("/tasks/{taskId}")
async def firebase_update_task(taskId: str, task: Task):
    response = firebase.database().child("tasks").child(taskId).update(task.dict())
    if response is not None:
        return Response(status="Ok",
                        code="200",
                        message="Successfully update task").dict(exclude_none=False)
    else:
        return Response(status="Ok",
                        code="200",
                        message="Task with this given id not found").dict(exclude_none=False)


@router.delete("/tasks/{taskId}")
async def firebase_delete_task(taskId: str):
    response = firebase.database().child("tasks").child(taskId).remove()
    return Response(status="Ok",
                    code="200",
                    message="Successfully delete task", result=response).dict(exclude_none=False)
