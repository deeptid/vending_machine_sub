from user.controllers import get_users_by_username
from fastapi import HTTPException, status
from database.connector import DatabaseConnector
from product.models import ProductCreateRequestModel, ProductUpdateRequestModel

database = DatabaseConnector()


def update_product(product_model: ProductUpdateRequestModel) -> int:
    existing_product = get_products_by_product_name(product_model.product_name)
    if len(existing_product) != 0 and existing_product[0]["id"] != product_model.id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="product_name is already in use by another product",
        )
    return database.query_put(
        """
            UPDATE product SET product_name = %s, price = %s, seller = %s WHERE product.id = %s;
        """,
        (
            product_model.product_name,
            product_model.price,
            product_model.seller,
            product_model.id,
        ),
    )


def get_all_products(limit: int = 10, offset: int = 0) -> list[dict]:
    products = database.query_get(
        """
        SELECT product.id, product.product_name, product.price, product.seller FROM product LIMIT %s OFFSET %s
        """,
        (limit, offset),
    )
    return products


def get_products_by_product_name(product_name: str) -> list[dict]:
    products = database.query_get(
        """
        SELECT product.id, product.product_name, product.price, product.seller from product where product_name = %s
        """,
        (product_name),
    )
    return products


def get_product_by_id(id: int) -> dict:
    products = database.query_get(
        """
        SELECT product.id, product.product_name, product.price, product.seller FROM product WHERE id = %s
        """,
        (id),
    )
    if len(products) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="product not found"
        )
    return products[0]


def create_product(product_model: ProductCreateRequestModel):
    database = DatabaseConnector()
    product = get_products_by_product_name(product_model.product_name)
    if len(product) != 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="product_name already exists."
        )
    seller = get_users_by_username(product_model.seller)
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="seller does not exist."
        )

    database.query_put(
        """
        INSERT INTO product(product_name, price, seller) VALUES (%s,%s,%s)
        """,
        (
            product_model.product_name,
            product_model.price,
            product_model.seller,
        ),
    )
    return {
        "product_name": product_model.product_name,
        "price": product_model.price,
        "seller": product_model.seller,
    }


def delete_product_by_id(id: int):
    database.query_put(
        """
        DELETE FROM user WHERE id = %s;
        """,
        (id),
    )