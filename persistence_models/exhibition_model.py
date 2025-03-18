# persistence_models/exhibition_model.py
from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

from .museum_model import MuseumModel
from .sponsor_model import SponsorModel
from .artwork_model import ArtworkModel


class ExhibitionModel(db.Model):
    __tablename__ = 'exhibitions'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    # Relationship with Museum (many exhibitions are owned by a museum)
    museum_id: Mapped[str] = mapped_column()
    museum: Mapped["MuseumModel"] = relationship(
        "MuseumModel",
        back_populates="exhibitions"
    )

    # Relationship One-to-One with sponsor
    sponsor: Mapped[Optional["SponsorModel"]] = relationship(
        "SponsorModel",
        back_populates="exhibition",
        uselist=False
    )

    # Relationship: One exhibition has many artworks
    artworks: Mapped[List["ArtworkModel"]] = relationship(
        "ArtworkModel",
        back_populates="exhibition",
        cascade="all, delete-orphan"
    )

