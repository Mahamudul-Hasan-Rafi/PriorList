from fastapi import APIRouter
from app.api.handlers.user import user_router

router=APIRouter()

router.include_router(user_router)