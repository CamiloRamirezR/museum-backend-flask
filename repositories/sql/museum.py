from repositories import MuseumRepository
from db import db
from models import Museum
import uuid


class MuseumSqlRepository(MuseumRepository):
    def __init__(self, session):
        self.session = session

    def find_all(self) -> list[Museum]:
        return Museum.query.all()

    def find_one(self, id: str) -> Museum | None:
        museum = self.session.get(Museum, id)
        if not museum:
            return None
        return  museum

    def create(self, museum_dict: dict[str, any]) -> Museum:
        new_museum = Museum(
            id=str(uuid.uuid4()),
            name=museum_dict['name'],
            description=museum_dict['description'],
            address=museum_dict['address'],
            city=museum_dict['city'],
            image=museum_dict['image']
        )
        self.session.add(new_museum)
        self.session.commit()
        return new_museum

    def update(self, id: str, museum: Museum) -> Museum:
        # TODO: Implement this method
        pass

    def delete(self, id: str) -> bool:
        museum = self.find_one(id)
        if not museum:
            return False
        self.session.delete(museum)
        return True

