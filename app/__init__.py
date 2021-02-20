from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import configs


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(configuration="default"):
    app = Flask(__name__)
    app.config.from_object(configs[configuration])

    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
