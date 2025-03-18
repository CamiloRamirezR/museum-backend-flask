# persistence_models/artist_model.py
from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date

from .artwork_model import ArtworkModel
from .movement_model import MovementModel


class ArtistModel(db.Model):
    __tablename__ = 'artists'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    birthplace: Mapped[str] = mapped_column()
    birthdate: Mapped[date] = mapped_column()
    image: Mapped[str] = mapped_column()

    # Relationship One-to-Many artworks
    artworks: Mapped[List["ArtworkModel"]] = relationship(
        "ArtworkModel",
        back_populates="artist",
        cascade="all, delete-orphan"
    )

    # Relationship Many-to-Many movements
    movements: Mapped[List["MovementModel"]] = relationship(
        "MovementModel",
        secondary="artist_movement",
        back_populates="artists"
    )