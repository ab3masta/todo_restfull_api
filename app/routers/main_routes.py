from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"api": "Todo RestFull API"}
