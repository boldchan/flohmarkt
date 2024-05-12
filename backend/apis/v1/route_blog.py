from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.repository.blog import create_new_blog
from db.session import get_db
from schemas.blog import BlogCreate, BlogShow


router = APIRouter()

@router.post("/", response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db)
    return blog