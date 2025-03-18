# persistence_models/museum_model.py
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

from .exhibition_model import ExhibitionModel
from .artwork_model import ArtworkModel


class MuseumModel(db.Model):
    __tablename__ = 'museums'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    image: Mapped[str] = mapped_column()

    # Relationship: One museum has many exhibitions and many artworks
    exhibitions: Mapped[List["ExhibitionModel"]] = relationship(
        "ExhibitionModel",
        back_populates="museum",
        cascade="all, delete-orphan"
    )

    artworks: Mapped[[List["ArtworkModel"]]] = relationship(
        "ArtworkModel",
        back_populates="museum",
        cascade="all, delete-orphan"
    )