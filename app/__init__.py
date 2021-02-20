from flask import Flask
from .config import configs


def create_app(configuration="default"):
    app = Flask(__name__)
    app.config.from_object(configs[configuration])

    return app
