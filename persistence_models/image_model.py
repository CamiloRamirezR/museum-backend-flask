# persistence_models/image_model.py
from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from .artwork_model import ArtworkModel


class ImageModel(db.Model):
    __tablename__ = 'images'

    id: Mapped[str] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column()
    alt_text: Mapped[str] = mapped_column()
    height: Mapped[str] = mapped_column()
    width: Mapped[str] = mapped_column()

    # Relationship Many-to-One artwork
    artwork_id: Mapped[Optional[str]] = mapped_column(nullable=True)
    artwork: Mapped[Optional["ArtworkModel"]] = relationship(
        "ArtworkModel",
        back_populates="images"
    )