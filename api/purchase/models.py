from pydantic import BaseModel
from typing import List, Optional


class PurchaseRequestModel(BaseModel):
    username: str
    coins: List[int]
