import os
from app import create_app

# Obtén la configuración desde las variables de entorno
config_name = os.getenv('FLASK_CONFIG') or 'default'

# Crea la aplicación Flask usando la configuración especificada
application = create_app(config_name)

if __name__ == "__main__":
    application.run()
