from fastapi import APIRouter

router = APIRouter(prefix="/markets", tags=["Markets"])

@router.get("/")
async def read_markets():
    return [
        {"name": "MarketA", "address": "Musterstr. 1"},
        {"name": "MarketB", "address": "Musterstr. 2"}
    ]