from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import configs


db = SQLAlchemy()


def create_app(configuration="default"):
    app = Flask(__name__)
    app.config.from_object(configs[configuration])

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
