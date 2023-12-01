import os

from flask import  Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from .task_app import task
from .auth_app import auth
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI'),
        JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
    )

    # podpięcie db
    db.init_app(app)

    JWTManager(app)

    # podpięcie systemu migracje
    migrate = Migrate()
    migrate.init_app(app, db)

    # podpięcie bluprintów
    app.register_blueprint(task)
    app.register_blueprint(auth)
    return app
