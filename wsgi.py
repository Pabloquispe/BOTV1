import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG', 'prod')
app = create_app(config_name)
