import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Directorio base de la aplicación
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configuración base utilizada para todas las configuraciones."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de horarios de servicios
    HORARIO_INICIO_MANANA = '09:00'
    HORARIO_FIN_MANANA = '12:00'
    HORARIO_INICIO_TARDE = '13:00'
    HORARIO_FIN_TARDE = '18:00'

    # Configuración de Flask-Mail (opcional)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'localhost')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 25))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'no-reply@example.com')

class DevelopmentConfig(Config):
    """Configuración utilizada durante el desarrollo."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')

class TestingConfig(Config):
    """Configuración utilizada durante las pruebas."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
    DEBUG = True
    MAIL_SUPPRESS_SEND = True  # Esto suprimirá el envío de correos electrónicos en pruebas

class ProductionConfig(Config):
    """Configuración utilizada en producción."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')
    MAIL_SUPPRESS_SEND = False  # Habilitar el envío de correos en producción

# Diccionario para facilitar el acceso a las configuraciones
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
