import uuid

from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Image(db.Model):
    __tablename__ = 'image'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    source = Column(String(500), nullable=False)
    alt_text = Column(String(500), nullable=False)
    height = Column(Float, nullable=False)
    width =  Column(Float, nullable=False)
    artwork = Column(UUID(as_uuid=True), ForeignKey('artwork.id'))