from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class UserAuth(BaseModel):
    username: str = Field(..., min_length=10, max_length=20, description="username")
    email: str = Field(..., min_length=10, max_length=25, description="email address")
    hashed_password: str = Field(..., min_length=5, max_length=20, description="password")

class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]=False
