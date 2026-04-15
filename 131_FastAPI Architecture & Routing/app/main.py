from fastapi import FastAPI
from app.routers import users, products, orders

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/", tags=["root"])
async def root():
    return {"message": "All routers are successfully mounted"}