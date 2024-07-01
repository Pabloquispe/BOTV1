from app import create_app
import os

config_name = os.getenv('FLASK_CONFIG') or 'default'
application = create_app(config_name)

if __name__ == "__main__":
    application.run()
