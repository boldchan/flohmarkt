from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def read_users():
    return [
        {"name": "Paul", "collections": [], "items": ["Toy1"]},
        {"name": "Tom", "collections": [], "items": ["Canon AE1"]}
    ]
    
@router.get("/register/", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse(request=request, name="users/registry.html")