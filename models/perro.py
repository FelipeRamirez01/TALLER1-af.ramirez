from db import db

class Perro(db.Model):
    __tablename__ = 'perros'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(30), nullable=True)
    edad = db.Column(db.Integer, nullable=True)
    peso = db.Column(db.Float, nullable=True)
