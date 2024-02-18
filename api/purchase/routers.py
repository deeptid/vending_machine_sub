from user.controllers import get_users_by_username
from product.controllers import get_product_by_id
from purchase.models import PurchaseRequestModel
from deposit.controllers import create_deposit, get_deposit_by_user_name
from deposit.models import DepositCreateRequestModel
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/v1/buy/", response_model=dict)
async def buy_product(purchase: PurchaseRequestModel):
    buyer = get_users_by_username(purchase.buyer)
    if buyer and buyer['role'] != "buyer":
        raise HTTPException(status_code=403, detail="Permission denied")

    product = get_product_by_id(purchase.productId)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    total_cost = product['price'] * purchase.quantity
    user_deposits = get_deposit_by_user_name(purchase.buyer)
    if len(user_deposits) == 0:
        raise HTTPException(status_code=404, detail="No Deposit found for this user")

    curr_deposit = user_deposits[0]['amount']

    if curr_deposit < total_cost:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    change = curr_deposit - total_cost
    model = DepositCreateRequestModel(username=purchase.buyer, amount=change)
    create_deposit(model)

    return {
        "total_spent": total_cost,
        "products_purchased": purchase.quantity,
        "change": change
    }