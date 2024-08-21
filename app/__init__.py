from flask import Flask
from flask_sqlalchemy import SQLALchemy
from flask_migrate import Migrate
from config import Config

db = SQLALchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    return app