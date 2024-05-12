from sqlalchemy.orm import Session

from db.models.blog import Blog
from schemas.blog import BlogCreate


def create_new_user(blog: BlogCreate, db: Session):
    blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        is_active=blog.is_active
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog
    