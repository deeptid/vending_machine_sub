from pydantic import BaseModel
from typing import Optional


class ProductCreateRequestModel(BaseModel):
    product_name: str
    price: int
    seller: str


class ProductUpdateRequestModel(BaseModel):
    id: int
    product_name: str
    price: int
    seller: str


class ProductResponseModel(BaseModel):
    id: int
    product_name: str
    price: int
    seller: str
