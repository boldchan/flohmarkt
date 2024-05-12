from fastapi import APIRouter

router = APIRouter(prefix="/collections", tags=["Collections"])

@router.get("/")
async def read_collections():
    return [
        {"name": "useful", "user-name": "Paul", "items": ["Toy1"]},
        {"name": "vantage", "user-name": "Tom", "items": ["Canon AE1"]}
    ]