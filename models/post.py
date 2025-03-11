from sqlalchemy import Column, Integer, String
from core.database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    content = Column(String)

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.c}