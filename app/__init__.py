from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import configs


db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()


def create_app(configuration="default"):
    app = Flask(__name__)
    app.config.from_object(configs[configuration])

    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .processo import processo as processo_blueprint
    app.register_blueprint(processo_blueprint)

    return app
