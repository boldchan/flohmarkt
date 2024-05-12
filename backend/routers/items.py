from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
async def read_items():
    return [
        {"name": "Toy1", "image-link": "http://www.fjkej.fej", "owner": "Paul", "market-name": "MarketA"},
        {"name": "Canon AE1", "image-link": "http://www.keefwfefjef.fej", "owner": "Tom", "market-name": "MarketB"}
    ]