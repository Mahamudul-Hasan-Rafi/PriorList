from passlib.context import CryptContext 
from typing import Union, Any
from datetime import datetime, timedelta
from app.core.config import settings
from jose import jwt

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def create_access_token(subject: Union[str, Any], expires_delta: int = None):
    if expires_delta is not None:
        expires_delta=datetime.utcnow()+expires_delta
    else:
        expires_delta=datetime.utcnow()+timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode={'exp':expires_delta, 'sub':subject}

    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)


def get_password(password_):
    return password_context.hash(password_)

def verify_password(password_, hashed_password):
    return password_context.verify(password_, hashed_password)