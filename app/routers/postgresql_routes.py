from fastapi import APIRouter, Depends
from app.schemas.schemas import Task

from app.utils.database import SessionLocal
from sqlalchemy.orm import Session

from app.utils.postgres_crud import *

from app.schemas.schemas import Response

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/tasks')
async def postgres_create_task(task: Task, db: Session = Depends(get_db)):
    create_task(db, task=task)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully", result=None).dict(exclude_none=True)


@router.get('/tasks')
async def postgres_get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _tasks = get_tasks(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_tasks)


@router.get('/tasks/{taskId}')
async def postgres_get_task(taskId: int, db: Session = Depends(get_db)):
    _tasks = get_task(db, id=taskId)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_tasks)


@router.put("/tasks/{taskId}")
async def postgres_update_task(taskId: int, task: Task, db: Session = Depends(get_db)):
    _book = update_task(db, id=taskId,
                        title=task.title, description=task.description)
    return Response(status="Ok", code="200", message="Success update data", result=_book)


@router.delete("/tasks/{taskId}")
async def postgres_delete_task(taskId: int, db: Session = Depends(get_db)):
    remove_task(db, id=taskId)
    return Response(status="Ok", code="200", message="Success delete data", result=None).dict(exclude_none=True)
