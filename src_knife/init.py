from fastapi import FastAPI
from handlers.exception_handler import *
from routing.product_router import router as product_router

def init_routes(server: FastAPI)->None:
    server.include_router(product_router)

    server.add_exception_handler(RequestValidationError, validation_exception_handler)
    server.add_exception_handler(HTTPException, http_exception_handler)
    server.add_exception_handler(Exception, base_exception_handler)
    server.add_exception_handler(KnifeException404, knife_exception_handler)
