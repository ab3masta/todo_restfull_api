from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool
    due_date: Optional[str] = None

    def dict(self) -> dict:
        return {
            "title": str(self.title),
            "description": self.description,
            "completed": self.completed,
            "due_date":  self.due_date,
        }

    class Config:
        orm_mode = True


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
