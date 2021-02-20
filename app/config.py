from secrets import token_hex


class Config:
    SECRET_KEY = token_hex(40)

    def init_app(self, app):
        pass


class DevelopmentConfig(Config):
    pass


configs = {
    "default": Config,
    "dev": DevelopmentConfig
}
