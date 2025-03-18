from db import db
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Museum(db.Model):
    __tablename__ = 'museum'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(128), nullable=False)
    description = Column(String(500), nullable=False)
    address = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    image = Column(String(128), nullable=False)
    exhibitions = db.relationship(
        'Exhibition',
        cascade='all, delete, delete-orphan'
    )
    artworks = db.relationship(
        'Artwork',
        cascade='all, delete, delete-orphan'
    )