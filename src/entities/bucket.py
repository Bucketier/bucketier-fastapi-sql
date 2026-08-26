import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from src.database import Base


class Bucket(Base):
    __tablename__ = 'buckets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    owner_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    owner_display_name = Column(String, nullable=False)
    owner_color = Column(String, nullable=False)

    def __repr__(self):
        return f"<Bucket(name={self.name})>"
