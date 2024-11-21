from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, UserMixin, login_user, login_required
from models.usuariop import User

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='views')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/taller1modulo3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Clave secreta para manejar sesiones y seguridad
    app.config['SECRET_KEY'] = os.urandom(24)  # Genera una clave aleatoria



    db.init_app(app)
    # Configurar LoginManager
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Ruta para login obligatorio

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)  # Lógica para cargar el usuario desde la DB


    from controllers.controller import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

 