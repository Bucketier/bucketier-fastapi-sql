from sqlalchemy import Column, String, Integer
from src.database import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(String, primary_key=True, unique=True)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    score = Column(Integer, index=True)
    review = Column(String, index=True)
        
    def __repr__(self):
        return f"<Item(name={self.name}, score={self.score})>"