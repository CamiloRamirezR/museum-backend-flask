# models/museum.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from .artwork import Artwork
from .exhibition import Exhibition


@dataclass
class Museum:
    id: str
    name: str
    description: str
    city: str
    address: str
    image: str
    exhibitions: List[Exhibition] = field(default_factory=list) # One to Many: one museum - many exhibitions
    artworks: List[Artwork] = field(default_factory=list) # One to Many: one museum - many artworks