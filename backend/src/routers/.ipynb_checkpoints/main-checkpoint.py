from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/", tags=["Main"])
async def read_root():
    return JSONResponse({"name": "GenAI Backend API"})
