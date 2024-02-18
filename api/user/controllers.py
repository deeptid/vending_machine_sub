from fastapi import HTTPException, status
from database.connector import DatabaseConnector
from user.models import UserCreateRequestModel, UserUpdateRequestModel

database = DatabaseConnector() 


def update_user(user_model: UserUpdateRequestModel) -> int:
    existing_user = get_users_by_username(user_model.username)
    if existing_user["id"] != user_model.id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username is already in use by another user",
        )
    return database.query_put(
        """
            UPDATE user SET username = %s, role = %s, WHERE user.id = %s;
        """,
        (
            user_model.username,
            user_model.role,
            user_model.id,
        ),
    )


def get_all_users(limit: int = 10, offset: int = 0) -> list[dict]:
    users = database.query_get(
        """
        SELECT user.id, user.username, user.role FROM user LIMIT %s OFFSET %s
        """,
        (limit, offset),
    )
    return users


def get_users_by_username(username: str):
    users = database.query_get(
        """
        SELECT user.id, user.username, user.role from user where username = %s
        """,
        (username),
    )
    return users[0] if len(users) > 0 else None


def get_user_by_id(id: int) -> dict:
    users = database.query_get(
        """
        SELECT user.id, user.username, user.role FROM user WHERE id = %s
        """,
        (id),
    )
    if len(users) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return users[0]


def create_user(user_model: UserCreateRequestModel):
    database = DatabaseConnector()
    user = get_users_by_username(user_model.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="username already exists."
        )
    if user_model.role not in ["seller", "buyer"]:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Role is not valid"
        )
    database.query_put(
        """
        INSERT INTO user(username, password, role) VALUES (%s,%s,%s)
        """,
        (
            user_model.username,
            user_model.password,
            user_model.role,
        ),
    )
    return {
        "username": user_model.username,
        "role": user_model.role,
    }


def delete_user_by_id(id: int):
    database.query_put(
        """
        DELETE FROM user WHERE id = %s;
        """,
        (id),
    )
