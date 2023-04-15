from fastapi import FastAPI, Depends
from app.routers.main_routes import router as mainRoutes
from app.routers.firebase_routes import router as firebaseRoutes
from app.routers.mongo_routes import router as mongoRoutes
from app.routers.postgresql_routes import router as postgresqlRoutes
from app.routers.security import router as securityRoutes
from fastapi.openapi.utils import get_openapi
from app.routers.security import get_current_username

app = FastAPI(title="Todo RestFull Api",

              description="RESTful API for managing tasks, built with FastAPI and Python. The project uses Firebase, MongoDB, and PostgreSQL to store tasks.", version="0.1.0",
              docs_url=None,
              redoc_url=None,
              openapi_url=None,)

# Use it directly here to avoid this error ==> Error loading ASGI app. Could not import module "app.main".
@app.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(get_current_username)):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)

app.include_router(mainRoutes, prefix="", tags=["Root"])
app.include_router(firebaseRoutes, prefix="/use-firebase", tags=["Firebase"])
app.include_router(mongoRoutes, prefix="/use-mongodb", tags=["MongoDB"])
app.include_router(
    postgresqlRoutes, prefix="/use-postgresql", tags=["PostgreSQL"])
app.include_router(
    securityRoutes, tags=["Security"])
