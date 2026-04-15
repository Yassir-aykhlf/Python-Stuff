from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/v1/products",
    tags=["products"]
)

class ProductUpdate(BaseModel):
    name: str
    price: float

@router.put("/{product_id}")
async def update_product(product_id: int, product: ProductUpdate):
    return {
        "message": f"Product {product_id} updated",
        "new_data": product
        }

@router.delete("/{product_id}")
async def delete_product(product_id: int):
    return {
        "message": f"Product {product_id} successfully deleted"
    }