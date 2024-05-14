from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_service import UserService
from app.core.security import create_access_token

auth_router = APIRouter()

@auth_router.post('/login')
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user=await UserService.authenticate(form_data.username, form_data.password)

    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    
    return {
        "access_token": create_access_token(user.username)
    }