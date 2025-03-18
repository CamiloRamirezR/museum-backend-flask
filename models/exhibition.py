# models/exhibition.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from .museum import Museum
from .sponsor import Sponsor
from .artwork import Artwork


@dataclass
class Exhibition:
    id: str
    name: str
    description: str
    museum: Optional[Museum] = None # Many to One: many exhibitions - one museum
    sponsor: Optional[Sponsor] = None # One to One: one exhibition - one sponsor
    artworks: List[Artwork] = field(default_factory=list) # One to Many: one exhibition - many artworks