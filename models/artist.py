# models/artist.py
from dataclasses import dataclass, field
from datetime import date
from typing import List

from .artwork import Artwork
from .movement import Movement


@dataclass
class Artist:
    id: str
    name: str
    birthplace: str
    birthdate: date
    image: str
    artworks: List[Artwork] = field(default_factory=list) # One to Many: one artist - many artworks
    movements: List[Movement] = field(default_factory=list) # Many to Many: may artists - many movements
