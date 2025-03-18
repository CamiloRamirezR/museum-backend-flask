# persistence_models/artwork_model.py
from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

from models import ArtworkType

from .museum_model import MuseumModel
from .exhibition_model import ExhibitionModel
from .artist_model import ArtistModel
from .image_model import ImageModel


class ArtworkModel(db.Model):
    __tablename__ = 'artworks'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    type: Mapped[ArtworkType] = mapped_column()
    main_image: Mapped[str] = mapped_column()

    # Relationship Many-to-One museum
    museum_id: Mapped[Optional[str]] = mapped_column(nullable=True)
    museum: Mapped[Optional["MuseumModel"]] = relationship(
        "MuseumModel",
        back_populates="artworks"
    )

    # Relationship Many-to-One exhibition
    exhibition_id: Mapped[Optional[str]] = mapped_column(nullable=True)
    exhibition: Mapped[Optional["ExhibitionModel"]] = relationship(
        "ExhibitionModel",
        back_populates="artworks"
    )

    # Relationship One-to-Many Images
    images: Mapped[List["ImageModel"]] = relationship(
        "ImageModel",
        back_populates="artwork",
        cascade="all, delete-orphan"
    )

    # Relationship Many-to-One artist
    artist_id: Mapped[Optional[str]] = mapped_column(nullable=True)
    artist: Mapped[Optional["ArtistModel"]] = relationship(
        "ArtistModel",
        back_populates="artworks"
    )
