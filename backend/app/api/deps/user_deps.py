from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

resusable_oauth = OAuth2PasswordBearer(
    tokeUrl="/api/auth/login",
    scheme_name="JWT"
)