from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base_class import Base

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    blogs: Mapped[List["Blog"]] = relationship(back_populates="author")