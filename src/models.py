import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(250), nullable=False)
    Name = Column(Integer, primary_key=True)
    User = Column(String(250), nullable=False)
    
    
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Name = Column(Integer, primary_key=True)
    Gender = Column(String(250), nullable=False)
    

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)
    population = Column(String(250), nullable=False) 
    terrain = Column(String(250), nullable=False)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False) 
    crew = Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')