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
    planet_id = Column(String(250), nullable=False)
    planet_name = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(String(250), nullable=False)
    character_name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    favorite_planet = Column(Integer, ForeignKey('Planet.id'))
    planet = relationship(Planet)
    favorite_character = Column(Integer, ForeignKey('Character.id'))
    Character = relationship(Character)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_comment = Column(String(250), nullable=False)
    Post_id = Column(Integer, ForeignKey('User.id'))
    post = relationship(User)
  



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
