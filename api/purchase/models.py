from pydantic import BaseModel


class PurchaseRequestModel(BaseModel):
    buyer: str
    productId: int
    quantity: int
