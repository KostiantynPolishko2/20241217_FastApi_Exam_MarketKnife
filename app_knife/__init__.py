from fastapi import FastAPI
from app_knife.handlers.exception_handler import *
from routing.product_router import router as product_router
from routing.product_admin_router import router as product_admin_router
from infrastructures.knife_exception import KnifeException404

def init_routes(server: FastAPI)->None:
    server.include_router(product_router)
    server.include_router(product_admin_router)

    server.add_exception_handler(RequestValidationError, validation_exception_handler)
    server.add_exception_handler(HTTPException, http_exception_handler)
    server.add_exception_handler(Exception, base_exception_handler)
    server.add_exception_handler(KnifeException404, knife_exception_handler)
