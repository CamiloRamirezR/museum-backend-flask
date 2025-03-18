from db import db
from sqlalchemy import Column, String, ForeignKey, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid

from .artwork_type import ArtworkType


class Artwork(db.Model):
    __tablename__ = 'artwork'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(128), nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String(500), nullable=False)
    type = Column(Enum(ArtworkType))
    main_image = Column(String(500), nullable=False)
    museum = Column(UUID(as_uuid=True), ForeignKey('museum.id'))
    exhibition = Column(UUID(as_uuid=True), ForeignKey('exhibition.id'))
    images = db.relationship(
        'Image',
        cascade='all, delete, delete-orphan'
    )
    artist = Column(UUID(as_uuid=True), ForeignKey('artist.id'))

