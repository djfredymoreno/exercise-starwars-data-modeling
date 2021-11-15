import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    person_name = Column(String(250), nullable=False)
    password = Column(Integer)
    email = Column(String(50),unique=True)
    character_favourites = relationship('Character_favourites', backref='User', lazy=True)
    planet_favourites = relationship('Planet_favourites', backref='User', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    character_id = Column(Integer, primary_key=True) 
    character_name = Column(String(250),nullable=False)
    gender = Column(String(25))
    homeworld = Column(String(100))
    character_favourites = relationship('Character_favourites', backref='Character', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(50))
    planet_favourites = relationship('Planet_favourites', backref='Planet', lazy=True)

class Character_favourites(Base):
    __tablename__ = 'character_favourites'
    favourites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    character_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    

class Planet_favourites(Base):
    __tablename__ = 'planet_favorites'
    favourites_id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    planet_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')