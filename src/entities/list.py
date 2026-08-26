from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from src.database import Base


class List(Base):
    __tablename__ = 'lists'

    id = Column(String, primary_key=True, unique=True)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    user_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    user_display_name = Column(String, nullable=False)
    user_color = Column(String, nullable=False)

    def __repr__(self):
        return f"<List(name={self.name})>"
