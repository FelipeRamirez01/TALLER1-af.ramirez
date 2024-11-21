
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Perro(UserMixin):

    def __init__(self, id, nombre, raza, edad,peso):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

 # Simular base de datos
    Perros = {
        "1": {"nombre": "Bella", "raza": "Pitbull", "edad": 4, "peso": 4.8},
        "3": {"nombre": "Oreo", "raza": "Pincher", "edad": 2, "peso": 1.8},
        "4": {"nombre": "Max", "raza": "Golden", "edad": 3, "peso": 8.8},
        "5": {"nombre": "Tito", "raza": "Chandoberman", "edad": 1, "peso": 4.1},
    }

    @classmethod
    def get_all(cls):
        """Devuelve todos los perros como una lista de objetos Perro."""
        return [
            cls(id, data["nombre"], data["raza"], data["edad"], data["peso"])
            for id, data in cls.Perros.items()
        ]

    @classmethod
    def get_by_id(cls, id):
        """Devuelve un perro por su ID."""
        data = cls.Perros.get(str(id))
        if data:
            return cls(id, data["nombre"], data["raza"], data["edad"], data["peso"])
        return None
    
    @classmethod
    def get(cls, perro_id):
        perro_data = cls.Perros.get(perro_id)
        if perro_data:
            return cls(
                id=perro_id,
                nombre=perro_data['nombre'],
                raza=perro_data['nombre'],
                edad=perro_data['edad'],
                peso=perro_data['peso']
            )
        return None