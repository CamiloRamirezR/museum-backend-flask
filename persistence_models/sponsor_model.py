# persistence_models/sponsor_model.py
from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from .exhibition_model import ExhibitionModel


class SponsorModel(db.Model):
    __tablename__ = 'sponsors'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    # Relationship One-to-One exhibition
    exhibition_id: Mapped[str] = mapped_column()
    exhibition: Mapped["ExhibitionModel"] = relationship(
        "ExhibitionModel",
        back_populates="sponsor",
        uselist=False
    )