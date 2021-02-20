from secrets import token_hex
import os


class Config:
    SECRET_KEY = token_hex(40)
    DEBUG = os.getenv("DEBUG_MODE") in [1, 'true', '1']

    def init_app(self, app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL") or "sqlite:///database.db"


configs = {
    "default": DevelopmentConfig,
    "dev": DevelopmentConfig
}
