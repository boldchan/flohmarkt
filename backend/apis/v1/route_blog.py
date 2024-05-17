from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.blog import create_new_blog, retreive_blog, retreive_all_blogs, update_blog, delete_blog
from db.session import get_db
from schemas.blog import BlogCreate, BlogShow, BlogUpdate


router = APIRouter()

@router.post("/", response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db)
    return blog

@router.get("/{id}", response_model=BlogShow)
def get_blog(id:int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist.", 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return blog

@router.put("/{id}", response_model=BlogShow)
def update_a_blog(id: int, blog: BlogUpdate, db: Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, db=db)
    return blog

@router.get("/", response_model=list[BlogShow])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = retreive_all_blogs(db=db)
    if not blogs:
        raise HTTPException(detail="No blogs", status_code=status.HTTP_204_NO_CONTENT)
    return blogs

@router.delete("/{id}")
def delete_a_blog(id: int, db: Session = Depends(get_db)):
    message = delete_blog(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code= status.HTTP_400_BAD_REQUEST)
    return {"msg":f"Successfully deleted blog with id {id}"}