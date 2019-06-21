"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Movie(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Movie model """

    __tablename__ = "movie"
    name = db.Column(db.String(300), primary_key=True)
    genre = db.Column(db.String(300), nullable = True)
    year = db.Column(db.Integer, nullable=True)
    affiche = db.Column(db.String(500), nullable=True)
    notes = db.relationship('Notation', backref=db.backref('notes',uselist = False))
    
def __init__(self, name, genre=None, year=None,affiche = None):
    """ Create a new User """
    self.name = name
    self.genre = genre
    self.year = year 
    self.affiche = affiche 
