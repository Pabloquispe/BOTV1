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
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

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
    
    return render_template('register.html')

