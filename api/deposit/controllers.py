from deposit.models import DepositCreateRequestModel, DepositResetRequestModel
from fastapi import HTTPException, status
from database.connector import DatabaseConnector
from user.models import UserCreateRequestModel, UserUpdateRequestModel

database = DatabaseConnector()


def get_all_deposits(limit: int = 10, offset: int = 0):
    users = database.query_get(
        """
        SELECT deposit.id, deposit.username, deposit.amount from deposit LIMIT %s OFFSET %s
        """,
        (limit, offset),
    )
    return users


def get_deposit_by_user_name(username: str):
    deposits = database.query_get(
        """
        SELECT deposit.id, deposit.username, deposit.amount from deposit where username = %s
        """,
        (username),
    )
    return deposits


def create_deposit(deposit_model: DepositCreateRequestModel):
    database = DatabaseConnector()
    existing_deposits = get_deposit_by_user_name(deposit_model.username)
    if len(existing_deposits) != 0:
        database.query_put(
            """
                UPDATE deposit SET amount = %s WHERE username = %s;
            """,
            (
                deposit_model.amount,
                deposit_model.username,
            ),
        )
    else:
        database.query_put(
            """
            INSERT INTO deposit(username, amount) VALUES (%s,%s)
            """,
            (
                deposit_model.username,
                deposit_model.amount,
            ),
        )
    
    return {
        "username": deposit_model.username,
        "amount": deposit_model.amount,
    }


def reset_deposit(reset_model: DepositResetRequestModel):
    database = DatabaseConnector()
    existing_deposits = get_deposit_by_user_name(reset_model.username)
    if len(existing_deposits) != 0:
        database.query_put(
            """
                UPDATE deposit SET amount = 0 WHERE username = %s;
            """,
            (
                reset_model.username,
            ),
        )
    
    return {
        "username": reset_model.username,
    }
