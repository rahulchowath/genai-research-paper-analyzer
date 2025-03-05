from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.routers import (
    health_router,
    predict_router,
    main_router,
)

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exception):
    response_message = {"error": {"message": exception.detail}}
    return JSONResponse(
        content=response_message,
        status_code=exception.status_code,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exception):
    response_message = {"message": "Validation failed", "details": exception.errors()}
    return JSONResponse(
        content=jsonable_encoder(response_message),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request, exception):
    response_message = {"error": {"message": str(exception)}}
    return JSONResponse(
        content=response_message,
        status_code=500,
    )


app.include_router(health_router)
app.include_router(predict_router)
app.include_router(main_router)
