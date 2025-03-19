from dependency_injector import providers, containers
from db import db
from repositories import MuseumRepository
from repositories.sql import MuseumSqlRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["blueprints"])

    # DB sessions
    db_session = providers.Factory(lambda: db.session)

    # Repositories
    museum_repository: providers.Provider[MuseumRepository] = providers.Factory(
        MuseumSqlRepository,
        session=db_session
    )