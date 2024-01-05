from fastapi import APIRouter

from app.api.api_v1.endpoints import register

api_router = APIRouter()

api_router.include_router(register.router, tags=["register"])
