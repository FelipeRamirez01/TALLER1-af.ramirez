from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):

    def __init__(self, id, username, password, es_admin=False):
        self.id = id
        self.username = username
        self.password = password
        #self.password = generate_password_hash(password)
        self.es_admin = es_admin
    
    # Simular base de datos
    USERS = {
        "1": {"username": "admin", "password": "123", "es_admin": True},
        "2": {"username": "usuario", "password": "123", "es_admin": False},
    }

    @classmethod
    def get(cls, user_id):
        user_data = cls.USERS.get(user_id)
        if user_data:
            return cls(
                id=user_id,
                username=user_data['username'],
                password=user_data['password'],
                es_admin=user_data['es_admin']
            )
        return None