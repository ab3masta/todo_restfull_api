from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
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

