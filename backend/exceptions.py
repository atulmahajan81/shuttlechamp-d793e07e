# exceptions.py

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse


def setup_exception_handlers(app: FastAPI):

    @app.exception_handler(HTTPException)
    async def custom_http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"message": "Internal Server Error"},
        )