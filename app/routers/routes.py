from fastapi import APIRouter, Depends


router = APIRouter()


@router.get("/")
async def root():
    return "Todo RestFull API"


@router.get("/todos")
async def read_todos():
    return {"message": "/todos GET"}


@router.get("/todos/{todo_id}")
async def read_todo():
    return {"message": "/todos/{todo_id} GET"}


@router.post("/todos")
async def create_todo():
    return {"message": "/todos GET"}


@router.put("/todos/{todo_id}")
async def update_todo():
    return {"message": "/todos/{todo_id} PUT"}


@router.delete("/todos/{todo_id}")
async def delete_todo():
    return {"message": "/todos/{todo_id} DELETE"}
