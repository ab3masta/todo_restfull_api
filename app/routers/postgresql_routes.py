from fastapi import APIRouter, Depends,HTTPException
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
    response = create_task(db, task=task)
    if response is not None:
        return Response(status="Ok",
                        code="200",
                        message="Task Created", result=None).dict(exclude_none=True)
    else:
        raise HTTPException(status_code=401, detail="Task not created")


@router.get('/tasks')
async def postgres_get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _tasks = get_tasks(db, skip, limit)
    return Response(status="Ok",
                    code="200",
                    message="Successfully get all tasks", result=_tasks).dict(exclude_none=True)


@router.get('/tasks/{taskId}')
async def postgres_get_task(taskId: int, db: Session = Depends(get_db)):
    _task = get_task(db, id=taskId)
    if _task is not None:
        return Response(status="Ok",
                        code="200",
                        message="Successfully get task", result=_task).dict(exclude_none=False)
    else:
        return Response(status="Ok",
                        code="200",
                        message="Task with this given id not found", result=_task).dict(exclude_none=False)


@router.put("/tasks/{taskId}")
async def postgres_update_task(taskId: int, task: Task, db: Session = Depends(get_db)):
    task = update_task(db, id=taskId,
                        title=task.title, description=task.description)
    if task is not None:
        return Response(status="Ok",
                        code="200",
                        message="Successfully update task").dict(exclude_none=False)
    else:
        return Response(status="Ok",
                        code="200",
                        message="Task with this given id not found").dict(exclude_none=False)


@router.delete("/tasks/{taskId}")
async def postgres_delete_task(taskId: int, db: Session = Depends(get_db)):
    response = remove_task(db, id=taskId)
    return Response(status="Ok",
                    code="200",
                    message="Successfully delete task", result=response).dict(exclude_none=False)
