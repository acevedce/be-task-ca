from fastapi import FastAPI
from interfaces.fastapi.routes import item_routes, customer_routes, cart_routes


app = FastAPI(
    title="Shop Clean Architecture API",
    description="API for managing customers, products, and carts using Clean Architecture in FastAPI",
    version="1.0.0",
    contact={
        "name": "César Acevedo",
        "email": "ing.cesaracevedo@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(item_routes.router, prefix="", tags=["Items"])
app.include_router(customer_routes.router, prefix="", tags=["Customers"])
app.include_router(cart_routes.router, prefix="", tags=["Carts"])