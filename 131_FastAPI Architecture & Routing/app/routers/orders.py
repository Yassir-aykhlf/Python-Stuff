from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/orders",
    tags=["orders"]
)

@router.get("/")
async def get_orders():
    return [
        {"order_id": 101, "status": "shipped"}, 
        {"order_id": 102, "status": "pending"}
    ]
