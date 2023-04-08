from fastapi import FastAPI

from app.routers.routes import router as routes

app = FastAPI()

app.include_router(routes)