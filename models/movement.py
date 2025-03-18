import uuid

from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Movement(db.Model):
    __tablename__ = 'movement'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(128), nullable=False)
    description = Column(String(500), nullable=False)
    country_origin = Column(String(128), nullable=False)
    artists = db.relationship(
        'Artist',
        secondary='artist_movement',
        back_populates='movements'
    )