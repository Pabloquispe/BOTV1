import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')

config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}
