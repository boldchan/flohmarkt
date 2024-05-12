from pydantic import BaseModel, Field

class BlogCreate(BaseModel):
    title: str
    slug: str
    content: str
    is_active: bool
    

class BlogShow(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    is_active: bool
    
    class Config():
        orm_mode = True