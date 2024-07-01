# wsgi.py
from app import create_app

config_name = os.getenv('FLASK_CONFIG') or 'default'
application = create_app(config_name)
