# models/sponsor.py
from dataclasses import dataclass
from typing import Optional

from .exhibition import Exhibition

@dataclass
class Sponsor:
    id: str
    name: str
    description: str
    exhibition: Optional[Exhibition] = None # One to One: one sponsor - one exhibition

