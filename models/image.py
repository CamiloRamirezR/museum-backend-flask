# models/image.py
from dataclasses import dataclass
from typing import Optional

from .artwork import Artwork


@dataclass
class Image:
    id: str
    source: str
    alt_text: str
    height: str
    width: str
    artwork: Optional[Artwork] = None # Many to One: many images - one artwork
