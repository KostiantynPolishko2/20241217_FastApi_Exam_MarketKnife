from fastapi import FastAPI
from app_redis.product_router import router as product_router

def init_routes(server: FastAPI)->None:
    server.include_router(product_router)