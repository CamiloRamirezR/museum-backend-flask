from models import Museum


class MuseumRepository:
    def find_all(self) -> list[Museum]:
        raise NotImplementedError

    def find_one(self, id: str) -> Museum | None:
        raise NotImplementedError

    def create(self, museum_dict: dict[str, any]) -> Museum:
        raise NotImplementedError

    def update(self, id: str, museum: Museum) -> Museum:
        raise NotImplementedError

    def delete(self, id: str) -> bool:
        raise NotImplementedError