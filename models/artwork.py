from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from .enums import ArtworkType

from .museum import Museum
from .exhibition import Exhibition
from .artist import Artist
from .image import Image

@dataclass
class Artwork:
    id: str
    name: str
    year: int
    description: str
    type: ArtworkType
    main_image: str
    museum: Optional[Museum] = None # Many to One: many artworks - one museum
    exhibition: Optional[Exhibition] = None # Many to One: many artworks - one exhibition
    images: List[Image] = field(default_factory=list) # One to Many: one artwork - many images
    artist: Optional[Artist] = None # Many to One: many artworks - one artist

