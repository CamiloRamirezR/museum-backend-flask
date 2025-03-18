from db import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

artists_movements = db.Table(
    'artist_movement',
    Column(
        'artist_id',
        UUID(as_uuid=True),
        ForeignKey('artist.id'),
        primary_key=True
    ),
    Column(
        'movement_id',
        UUID(as_uuid=True),
        ForeignKey('movement.id'),
        primary_key=True
    )
)