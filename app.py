<<<<<<< HEAD
from dotenv import load_dotenv
import os
from flask import Flask, render_template
from flask_migrate import Migrate
from config import config_by_name
from modelos.models import db
from controladores.admin_routes import admin_bp
from controladores.user_routes import user_bp
from controladores.auth_routes import auth_bp
from controladores.main_routes import main_bp
from flask_mail import Mail
import logging
from logging.handlers import RotatingFileHandler

# Cargar variables de entorno
load_dotenv()

# Inicializar Flask-Mail
mail = Mail()

def create_app(config_name):
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__, template_folder='vistas/templates', static_folder='vistas/static')
    app.config.from_object(config_by_name[config_name])
=======
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modelos.models import db, Usuario, Vehiculo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Usuario.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_role'] = user.rol
            if user.rol == 'administrador':
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('user.perfil'))
        else:
            flash('Correo electrónico o contraseña incorrectos', 'error')
>>>>>>> 2943027bcd9dc31cd3f716a0d516ea590f8f3f70
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

<<<<<<< HEAD
    # Inicializar Flask-Mail solo si las credenciales están presentes
    if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
        mail.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
=======
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        pais = request.form['pais']
        fecha_nacimiento = request.form['fecha_nacimiento']
        genero = request.form['genero']
        marca = request.form['marca']
        modelo = request.form['modelo']
        anio = request.form['anio']
        password = request.form['password']
        
        # Verificar si el correo electrónico ya está registrado
        if Usuario.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado.', 'error')
            return redirect(url_for('auth.register'))
        
        # Crear un nuevo usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion,
            pais=pais,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            rol='administrador' if 'admin@dominio.com' in email else 'usuario'
        )
        nuevo_usuario.set_password(password)
        
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Crear un nuevo vehículo
        nuevo_vehiculo = Vehiculo(
            usuario_id=nuevo_usuario.id,
            marca=marca,
            modelo=modelo,
            año=anio
        )
        
        db.session.add(nuevo_vehiculo)
        db.session.commit()
        
        flash('Usuario y vehículo registrados con éxito. Por favor, inicie sesión.', 'success')
        return redirect(url_for('auth.login'))
>>>>>>> 2943027bcd9dc31cd3f716a0d516ea590f8f3f70
    
    return render_template('register.html')

<<<<<<< HEAD
    # Configuración de logs
    configure_logging(app)

    # Manejo de errores personalizados
    configure_error_handlers(app)

    return app

def configure_logging(app):
    """Configura los logs de la aplicación."""
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        )
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Aplicación iniciada')

def configure_error_handlers(app):
    """Configura los manejadores de errores."""
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), 500

if __name__ == "__main__":
    config_name = os.getenv('FLASK_CONFIG', 'default')  # Configuración predeterminada
    app = create_app(config_name)
    app.run(debug=(config_name == 'development'))
=======
>>>>>>> 2943027bcd9dc31cd3f716a0d516ea590f8f3f70
