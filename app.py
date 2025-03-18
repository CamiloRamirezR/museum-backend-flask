from flask import Flask
from db import db
from container import Container
from env_variables import DB_USER, DB_HOST, DB_PASSWORD, DB_NAME, DB_PORT


class FlaskMicroservice(Flask):
    container: Container

def create_app(database=None) -> FlaskMicroservice:
    app = FlaskMicroservice(__name__)
    app.container = Container()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = database or \
                                            f'postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Blueprints

    return app


