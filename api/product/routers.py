from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from product.controllers import (
    delete_product_by_id,
    update_product,
    get_all_products,
    get_product_by_id,
    create_product,
    get_products_by_product_name,
)
from product.models import (
    ProductCreateRequestModel,
    ProductUpdateRequestModel,
    ProductResponseModel,
)

router = APIRouter()


@router.get("/v1/products", response_model=list[ProductResponseModel])
def get_all_products_api():
    """
    This products get API allow you to fetch all product data.
    """
    product = get_all_products()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(product))


@router.get("/v1/product/{product_id}", response_model=ProductResponseModel)
def get_product_api(product_id: int):
    """
    This product API allow you to fetch specific product data.
    """
    product = get_product_by_id(product_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(product))


@router.get("/v1/products/{product_name}", response_model=ProductResponseModel)
def get_product_by_name(product_name: str):
    products = get_products_by_product_name(product_name)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(products[0]))


@router.post("/v1/product/", response_model=ProductResponseModel)
async def create_product_api(product_details: ProductCreateRequestModel):
    create_product(product_details)
    products = get_products_by_product_name(product_details.productname)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(products[0]))


@router.put("/v1/product/{product_id}", response_model=ProductResponseModel)
def update_product_api(product_id: int, product_details: ProductUpdateRequestModel):
    """
    This product update API allow you to update product data.
    """
    update_product(product_details)
    product = get_product_by_id(product_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(product))


@router.delete("/v1/product/{product_id}")
def delete_product_api(product_id: int):
    delete_product_by_id(product_id)
    message = {"message": "Item deleted"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(message))

