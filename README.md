#  Vending Machine 

Design an API for a vending machine, allowing users with a “seller” role to add, update or remove products, while users with a “buyer” role can deposit coins into the machine and make purchases. Your vending machine should only accept 5, 10, 20, 50 and 100 cent coins

## Tasks
- Framework of choices must be FastAPI
- REST API should be implemented consuming and producing “application/json”
- Implement CRUD for users (POST shouldn’t require authentication)
- Implement CRUD for a product model (GET can be called by anyone, while POST, PUT and DELETE can be called only by the seller user who created the product)
- Implement /deposit endpoint so users with a “buyer” role can deposit 5, 10, 20, 50 and 100 cent coins into their vending machine account
- Implement /buy endpoint (accepts productId, amount of products) so users with a “buyer” role can buy products with the money they’ve deposited. API should return total they’ve spent, products they’ve purchased and their change if there’s any (in 5, 10, 20, 50 and 100 cent coins)
- Implement /reset endpoint so users with a “buyer” role can reset their deposit


## Manual setup
Install [`Docker` and `Docker compose`](https://www.docker.com/) first.
After installation, run the following command to create a local Docker container.

```sh
docker-compose up
```

- API server: http://localhost:8000
- API Docs: http://localhost:8000/v1/docs
- DB server: http://localhost:3306