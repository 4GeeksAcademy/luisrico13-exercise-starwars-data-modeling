import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er 

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    planet = relationship(Planet)
    Character = relationship(Character)

# class Post(Base):
#     __tablename__ = 'Post'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     post_comment = Column(String(250), nullable=False)
#     Post_id = Column(Integer, ForeignKey('User.id'))
#     post = relationship(User)

class Favorite_Character(Base):
    __tablename__ = 'Favorite_character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    character = relationship(User)
    character_id = Column(Integer, ForeignKey('Character.id'))
    character1_id = relationship(Character)

class Favorite_Planet(Base):
    __tablename__ = 'Favorite_planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    character_id = relationship(User)
    planet_id = Column(Integer, ForeignKey('Planet.id'))
    planet1_id = relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
