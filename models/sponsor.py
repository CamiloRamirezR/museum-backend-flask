import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Sponsor(db.Model):
    __tablename__ = 'sponsor'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(128), nullable=False)
    description = Column(String(500), nullable=False)
    website = Column(String(500), nullable=False)
    exhibition = Column(UUID(as_uuid=True), ForeignKey('exhibition.id'))