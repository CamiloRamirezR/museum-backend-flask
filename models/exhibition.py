from db import db
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Exhibition(db.Model):
    __tablename__ = 'exhibition'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(128), nullable=False)
    description = Column(String(500), nullable=False)
    museum = Column(UUID(as_uuid=True), ForeignKey('museum.id'))
    artworks = db.relationship(
        'Artwork',
        cascade='all, delete, delete-orphan'
    )
    sponsor = Column(UUID(as_uuid=True), ForeignKey('sponsor.id'))
