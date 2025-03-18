import uuid

from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Artist(db.Model):
    __tablename__ = 'artist'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(128), nullable=False)
    birthplace = Column(String(128), nullable=False)
    birthdate = Column(Date, nullable=False)
    image = Column(String(500), nullable=False)
    artworks = db.relationship(
        'Artwork',
        cascade='all, delete, delete-orphan'
    )
    movements = db.relationship(
        'Movement',
        secondary='artist_movement',
        back_populates='artists'
    )