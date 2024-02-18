from pydantic import BaseModel
from typing import Optional


class UserCreateRequestModel(BaseModel):
    username: str
    password: str
    role: str


class UserUpdateRequestModel(BaseModel):
    id: int
    username: str
    password: str
    role: str


class UserResponseModel(BaseModel):
    id: int
    username: str
    role: str
