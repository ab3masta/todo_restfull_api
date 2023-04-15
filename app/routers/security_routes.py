from fastapi import APIRouter, Depends
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from app.admin.authorization import firebaseAdminAuth

router = APIRouter()


@router.get("/docs", include_in_schema=False)
async def get_swagger_documentation(username: str = Depends(firebaseAdminAuth)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@router.get("/redoc", include_in_schema=False)
async def get_redoc_documentation(username: str = Depends(firebaseAdminAuth)):
    return get_redoc_html(openapi_url="/openapi.json", title="docs")
