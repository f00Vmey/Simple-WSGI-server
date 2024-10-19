import os

class Config:
    SECRET_KEY = os.urandom(24)
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

config = {
    'development': Config,
    'production': ProductionConfig
}
