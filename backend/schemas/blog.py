from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, computed_field

class BlogCreate(BaseModel):
    title: str
    content: str

    @computed_field
    @property
    def slug(self) -> str:
        return self.title.replace(" ","-").lower()
    

class BlogUpdate(BlogCreate):
    pass
        
    

class BlogShow(BaseModel):
    title: str
    content: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)