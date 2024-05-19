from db.models.blog import Blog
from schemas.blog import BlogCreate
from schemas.blog import BlogUpdate
from sqlalchemy.orm import Session


def create_new_blog(blog: BlogCreate, db: Session, author_id: int):
    blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=author_id,
        is_active=True,
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retreive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def update_blog(id: int, blog: BlogUpdate, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error": f"Blog with id {id} does not exist"}
    if not blog_in_db.author_id == author_id:  # new
        return {"error": "Only the author can modify the blog"}
    blog_in_db.title = (blog.title,)
    blog_in_db.content = (blog.content,)
    blog_in_db.author_id = (author_id,)
    blog_in_db.is_active = True

    db.add(blog_in_db)
    db.commit()
    db.refresh(blog_in_db)
    return blog_in_db


def retreive_all_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs


def delete_blog(id: int, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    if not blog_in_db.first():
        return {"error": f"Could not find blog with id {id}"}
    if not blog_in_db.first().author_id == author_id:  # new
        return {"error": "Only the author can delete a blog"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"deleted blog with id {id}"}
