from sqlalchemy import Column, Integer, String
from core.database import Base
from schemas.post import PostResponse


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    content = Column(String)

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.c}

    def as_response(self):
        return PostResponse(**self.dict())