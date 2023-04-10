from ..schemas.schemas import Task
from .database import mongo_todo_collection
from bson.objectid import ObjectId


def mongo_create_task(task: Task):
    try:
        collection = mongo_todo_collection()
        collection.insert_one(task.dict())
        return "success create task"
    except Exception as e:
        return "Mongo create task error: {}. Task => {} ".format(e, task.dict())


def mongo_get_tasks(skip: int, limit: int):
    try:
        collection = mongo_todo_collection()
        tasks = list(collection.find(skip=skip, limit=limit))
        return str(tasks) # TODO chenge type
    except:
        return "Mongo get tasks: something went wrong"


def mongo_get_task(taskId: str):
    try:
        collection = mongo_todo_collection()
        task = collection.find_one({"_id": ObjectId(taskId)})
        return str(task) # TODO chenge type
    except:
        return "Mongo get task: something went wrong"


def mongo_update_task(taskId: str, task: Task):
    try:
        collection = mongo_todo_collection()
        # filter
        filter = {"_id": ObjectId(taskId)}
        # Values to be updated.
        newvalues = {"$set": task.dict()}
        collection.update_one(filter, newvalues)
        return "success update task"
    except Exception as e:
        return "Mongo update task error: {}. ".format(e)


def mongo_delete_task(taskId: str):
    try:
        collection = mongo_todo_collection()
        collection.delete_one({"_id": ObjectId(taskId)})
        return "success delete task"
    except:
        return "Mongo delete task: something went wrong"
