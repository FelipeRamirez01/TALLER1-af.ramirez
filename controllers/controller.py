from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user
from models.usuariop import User
from models.perrop import Perro
from db import db


main = Blueprint('main', __name__)

def authenticate_user(username, password):
    for user_id, user_data in User.USERS.items():
        if user_data['username'] == username and user_data['password'] == password:
            return User.get(user_id)
    return None

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/ruta-logueada')
@login_required
def ruta():
    return render_template("ruta-logueada.html", username=current_user.username)

@main.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        user = authenticate_user(username, password)
        if user:
            login_user(user)
            if user.es_admin:
                return redirect(url_for('main.admin'))
            return redirect(url_for('main.ruta'))
        else:
            flash('Usuario o contraseña incorrectos.')
    return render_template('login.html')
            
@main.route('/logout')
@login_required
def logout():
    logout_user()
    #flash('Has cerrado sesión', 'info')
    return redirect(url_for('main.login'))

@main.route('/admin')
@login_required
def admin():
    if not current_user.es_admin:
        return redirect(url_for('main.login'))
    
    perros= Perro.get_all()
    return render_template('admin.html', username=current_user.username, perros=perros)