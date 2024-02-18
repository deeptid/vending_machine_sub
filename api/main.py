from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user.routers import router as user_router
from product.routers import router as product_router
from deposit.routers import router as deposit_router
from purchase.routers import router as purchase_router

# Set API info
app = FastAPI(
    title="Vending Machine API",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    openapi_url="/v1/openapi.json",
)

# Set CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:4000",
    "http://localhost:19006",
]

# Set middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
User APIs
Provides user CRUD APIs.
"""

app.include_router(user_router)
app.include_router(product_router)
app.include_router(deposit_router)
app.include_router(purchase_router)
