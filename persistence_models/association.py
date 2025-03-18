# persistence_models/association.py
from db import db
from sqlalchemy import Column, String, ForeignKey

artist_movement = db.Table(
    'artist_movement',
    db.metadata,
    Column('artist_id', String, ForeignKey('artists.id'), primary_key=True),
    Column('movement_id', String, ForeignKey('movements.id'), primary_key=True)
)