import uvicorn
from fastapi import FastAPI
from app.routers.main_routes import router as mainRoutes
from app.routers.firebase_routes import router as firebaseRoutes
from app.routers.mongo_routes import router as mongoRoutes
from app.routers.postgresql_routes import router as postgresqlRoutes


app = FastAPI(title="Todo RestFull Api",
              description="RESTful API for managing tasks, built with FastAPI and Python. The project uses Firebase, MongoDB, and PostgreSQL to store tasks.", version="0.1.0",)


app.include_router(mainRoutes, prefix="", tags=["Root"])
app.include_router(firebaseRoutes, prefix="/use-firebase", tags=["Firebase"])
app.include_router(mongoRoutes, prefix="/use-mongodb", tags=["MongoDB"])
app.include_router(
    postgresqlRoutes, prefix="/use-postgresql", tags=["PostgreSQL"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True, log_level="info")
