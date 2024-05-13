from pydantic import BaseModel, ConfigDict, Field

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
    
    model_config = ConfigDict(from_attributes=True)