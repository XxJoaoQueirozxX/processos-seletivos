from secrets import token_hex
import os


class Config:
    SECRET_KEY = token_hex(40)
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.googlemail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.getenv("USER_EMAIL")
    MAIL_PASSWORD = os.getenv("USER_PASSWORD")
    MAIL_SUBJECT_PREFIX = '[Processo Seletivo]'
    MAIL_SENDER = f'Processo Seletivo <{os.getenv("USER_EMAIL")}>'

    def init_app(self, app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL") or "sqlite:///database.db"


class TestConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL") or "sqlite:///"
    TESTING = True


configs = {
    "default": DevelopmentConfig,
    "dev": DevelopmentConfig,
    "testing": TestConfig
}
