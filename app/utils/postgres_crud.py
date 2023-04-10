from sqlalchemy.orm import Session
from models.models import Task as TaskModel
from schemas.schemas import Task as TaskSchema


def create_task(db: Session, task: TaskSchema):
    _task = TaskModel(title=task.title, description=task.description,
                      completed=task.completed, due_date=task.due_date)
    db.add(_task)
    db.commit()
    db.refresh(_task)
    return _task


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TaskModel).offset(skip).limit(limit).all()


def get_task(db: Session, id: int):
    return db.query(TaskModel).filter(TaskModel.id == id).first()


def remove_task(db: Session, id: int):
    _task = get_task(db=db, id=id)
    db.delete(_task)
    db.commit()


def update_task(db: Session, id: int, title: str | None, description: str | None):
    _task = get_task(db=db, id=id)
    _task.title = title  # type:ignore
    _task.description = description  # type:ignore
    db.commit()
    db.refresh(_task)
    return _task
