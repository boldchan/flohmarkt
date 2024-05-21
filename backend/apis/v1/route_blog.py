from typing import Annotated
from typing import Optional

from apis.v1.route_login import get_current_user
from db.models.user import User
from db.repository.blog import create_new_blog
from db.repository.blog import delete_blog
from db.repository.blog import retreive_all_blogs
from db.repository.blog import retreive_blog
from db.repository.blog import update_blog
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.templating import Jinja2Templates
from schemas.blog import BlogCreate
from schemas.blog import BlogShow
from schemas.blog import BlogUpdate
from sqlalchemy.orm import Session


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", include_in_schema=False)
def home(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    alert: Optional[str] = None,
):
    blogs = retreive_all_blogs(db)
    return templates.TemplateResponse(
        "blog/home.html", {"request": request, "blogs": blogs, "alert": alert}
    )


@router.post("/", response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def create_blog(
    blog: BlogCreate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    blog = create_new_blog(blog=blog, db=db, author_id=current_user.id)
    return blog


@router.get("/{id}", response_model=BlogShow)
def get_blog(id: int, request: Request, db: Annotated[Session, Depends(get_db)]):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return templates.TemplateResponse(
        "blog/detail.html", {"request": request, "blog": blog}
    )


@router.put("/{id}", response_model=BlogShow)
def update_a_blog(
    id: int,
    blog: BlogUpdate,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    blog = update_blog(id=id, blog=blog, db=db, author_id=current_user.id)
    return blog


@router.get("/", response_model=list[BlogShow])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = retreive_all_blogs(db=db)
    if not blogs:
        raise HTTPException(detail="No blogs", status_code=status.HTTP_204_NO_CONTENT)
    return blogs


@router.delete("/{id}")
def delete_a_blog(
    id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    message = delete_blog(id=id, db=db, author_id=current_user.id)
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"msg": f"Successfully deleted blog with id {id}"}
