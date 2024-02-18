from deposit.controllers import create_deposit, get_all_deposits, get_deposit_by_user_name, reset_deposit
from deposit.models import DepositCoinsRequestModel, DepositCreateRequestModel, DepositResetRequestModel, DepositResponseModel
from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/v1/deposits", response_model=list[DepositResponseModel])
async def get_all_users_api():
    """
    This users get API allow you to fetch all user data.
    """
    user = get_all_deposits()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user))


@router.post("/v1/deposit/", response_model=int)
async def deposit_coins(deposit: DepositCoinsRequestModel):
    valid_coins = {5, 10, 20, 50, 100}
    for coin in deposit.coins:
        if coin not in valid_coins:
            raise HTTPException(status_code=400, detail=f"Invalid coin: {coin}")

    total_amount = sum(deposit.coins)
    existing_deposits = get_deposit_by_user_name(deposit.username)
    if len(existing_deposits) != 0:
        total_amount += existing_deposits[0].amount

    model = DepositCreateRequestModel()
    model.username = deposit.username
    model.amount = total_amount

    create_deposit(model)
    return total_amount

@router.post("/v1/reset/", response_model=int)
async def reset_deposit_api(reset: DepositResetRequestModel):
    # if current_user.role != "buyer":
    #     raise HTTPException(status_code=403, detail="Permission denied")
    existing_deposits = get_deposit_by_user_name(reset.username)
    deposited_amount = 0
    if len(existing_deposits) != 0:
        deposited_amount += existing_deposits[0].amount
    reset_deposit(reset)
    return deposited_amount