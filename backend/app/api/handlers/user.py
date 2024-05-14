from fastapi import APIRouter, HTTPException, status
import pymongo.errors
from app.schemas.user_schema import UserAuth, UserOut
from app.services.user_service import UserService
import pymongo

user_router = APIRouter()

@user_router.post("/create", response_model=UserOut)
async def create_user(user: UserAuth):
    try:
        return await UserService.user_create_db(user)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this username or email already exist")
