from fastapi import FastAPI
from app_auth.handlers.exception_handler import *
from app_auth.routing.auth_router import router as auth_router

def init_routes(server: FastAPI, is_connect = True)->None:
    if not is_connect:
        return

    server.include_router(auth_router)
    server.add_exception_handler(RequestValidationError, validation_exception_handler)
    server.add_exception_handler(HTTPException, http_exception_handler)
    server.add_exception_handler(Exception, base_exception_handler)
