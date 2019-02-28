class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = '\x1a\x1d\xfc\xce\xf5z-:\xb1\xf7\xeb\xd2\x93\x94\xf1\xae\xb2\x9f\x9e\x15\x99\xb6Hn'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = '\x85\xcb\xb4\xf3\x84T\xbbW8q]*\x1b\xa6\x97\x85\x92\xac\x12\xbe\xa8:T\x17'
