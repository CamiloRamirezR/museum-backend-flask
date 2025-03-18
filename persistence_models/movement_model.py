# persistence_models/movement_model.py
from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from .artist_model import ArtistModel


class MovementModel(db.Model):
    __tablename__ = 'movements'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    country_of_origin: Mapped[str] = mapped_column()

    # Relationship Many-to-Many Artist (secondary: artist_movement)
    artists: Mapped[List["ArtistModel"]] = relationship(
        "ArtistModel",
        secondary="artist_movement",
        back_populates="movements"
    )