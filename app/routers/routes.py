from fastapi import APIRouter, HTTPException, Depends
from ..utils.mongodb_crud import *
from ..schemas.schemas import Task
from ..utils.firebase_initialize import *

from ..schemas.schemas import Task as SchemaTask
from ..schemas.schemas import Task
from ..models.models import Task as ModelTask
from fastapi_sqlalchemy import db

from ..utils.database import SessionLocal
from sqlalchemy.orm import Session

from ..utils.postgres_crud import *

from ..schemas.schemas import Response

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def root():
    return "Todo RestFull API"

# --------------------- MongoDB


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


# --------------------- Firebase

@router.post("/usefirebase/tasks")
async def firebase_create_task(task: Task):
    response = firebase.database().child("tasks").push(task.dict())
    return {"message": "/firebase/task POST. {}".format(response)}


@router.get("/usefirebase/tasks")
async def firebase_get_tasks():
    response = firebase.database().child("tasks").get()
    tasks = None
    if response.each() is not None:
        for result in response.each():  # type:ignore
            tasks = result.val()
    return {"message": "/firebase/tasks GET. {}".format(str(tasks))}


@router.get("/usefirebase/tasks/{taskId}")
async def firebase_get_task(taskId: str):
    response = firebase.database().child(
        "tasks").order_by_key().equal_to(taskId).get()
    task = None
    if response.each() is not None:
        for result in response.each():  # type:ignore
            task = result.val()
    return {"message": "/firebase/task/{} GET. {}".format(taskId, str(task))}


@router.put("/usefirebase/tasks/{taskId}")
async def firebase_update_task(taskId: str, task: Task):
    response = firebase.database().child("tasks").child(taskId).update(task.dict())
    return {"message": "/tasks/{} PUT. {}".format(taskId, response)}


@router.delete("/usefirebase/tasks/{taskId}")
async def firebase_delete_task(taskId: str):
    response = firebase.database().child("tasks").child(taskId).remove()
    return {"message": "/tasks/{} DELETE. {}".format(taskId, response)}

# ---------------------  POSTGRES


@router.post('/usepostgres/tasks')
async def postgres_create_task(task: Task, db: Session = Depends(get_db)):
    create_task(db, task=task)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully", result=None).dict(exclude_none=True)


@router.get('/usepostgres/tasks')
async def postgres_get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _tasks = get_tasks(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_tasks)


@router.get('/usepostgres/tasks/{taskId}')
async def postgres_get_task(taskId: int, db: Session = Depends(get_db)):
    _tasks = get_task(db, id=taskId)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_tasks)


@router.put("/usepostgres/tasks/{taskId}")
async def postgres_update_task(taskId: int, task: Task, db: Session = Depends(get_db)):
    _book = update_task(db, id=taskId,
                        title=task.title, description=task.description)
    return Response(status="Ok", code="200", message="Success update data", result=_book)


@router.delete("/usepostgres/tasks/{taskId}")
async def postgres_delete_task(taskId: int, db: Session = Depends(get_db)):
    remove_task(db, id=taskId)
    return Response(status="Ok", code="200", message="Success delete data", result=None).dict(exclude_none=True)
