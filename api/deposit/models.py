from pydantic import BaseModel
from typing import List, Optional


class DepositCoinsRequestModel(BaseModel):
    username: str
    coins: List[int]


class DepositCreateRequestModel(BaseModel):
    username: str
    amount: int


class DepositResponseModel(BaseModel):
    id: int
    username: str
    amount: str


class DepositResetRequestModel(BaseModel):
    username: str
