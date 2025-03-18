# models/movement.py
from dataclasses import dataclass, field
from typing import List

from .artist import Artist

@dataclass
class Movement:
    id: str
    name: str
    description: str
    country_of_origin: str
    artists: List[Artist] = field(default_factory=list) # Many to Many: many movements - many artists