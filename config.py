import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    HORARIO_INICIO_MANANA = '09:00'
    HORARIO_FIN_MANANA = '12:00'
    HORARIO_INICIO_TARDE = '13:00'
    HORARIO_FIN_TARDE = '18:00'

    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = os.path.join(BASE_DIR, 'flask_session')
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_FILE_THRESHOLD = 100
    SESSION_FILE_MODE = 0o600
    SESSION_COOKIE_NAME = 'my_session'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')

config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}

