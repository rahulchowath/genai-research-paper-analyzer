import os
from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from src.internal import research_paper_extraction

router = APIRouter()


@router.post(
    "/predict",
    tags=["Predict"],
    responses={
        200: {"description": "Successful Response"},
        400: {"description": "Bad Request"},
        422: {"description": "Validation Error"},
    },
)
async def predict(file: UploadFile = File(...)):
    extracted_data = research_paper_extraction(pdf_file=file)
    return JSONResponse(extracted_data)
