from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from user.controllers import (
    delete_user_by_id,
    update_user,
    get_all_users,
    get_user_by_id,
    create_user,
    get_users_by_username,
)
from user.models import (
    UserCreateRequestModel,
    UserUpdateRequestModel,
    UserResponseModel,
)

router = APIRouter()


@router.get("/v1/users", response_model=list[UserResponseModel])
async def get_all_users_api():
    """
    This users get API allow you to fetch all user data.
    """
    user = get_all_users()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user))


@router.get("/v1/user/{user_id}", response_model=UserResponseModel)
async def get_user_api(user_id: int):
    """
    This user API allow you to fetch specific user data.
    """
    user = get_user_by_id(user_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user))


@router.get("/v1/users/{user_name}", response_model=UserResponseModel)
async def get_user_by_name(user_name: str):
    users = get_users_by_username(user_name)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users[0]))


@router.post("/v1/user/", response_model=UserResponseModel)
async def create_user_api(user_details: UserCreateRequestModel):
    create_user(user_details)
    users = get_users_by_username(user_details.username)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users[0]))


@router.put("/v1/user/{user_id}", response_model=UserResponseModel)
async def update_user_api(user_id: int, user_details: UserUpdateRequestModel):
    """
    This user update API allow you to update user data.
    """
    update_user(user_details)
    user = get_user_by_id(user_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user))


@router.delete("/v1/user/{user_id}")
def delete_user_api(user_id: int):
    delete_user_by_id(user_id)
    message = {"message": "Item deleted"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(message))
