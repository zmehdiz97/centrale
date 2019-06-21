"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

class Notation(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "notation"

    username = db.Column(db.String(300),ForeignKey('user.username'), primary_key=True)
    name = db.Column(db.String(300),ForeignKey('movie.name'), primary_key=True)
    note = db.Column(db.Integer, nullable=True)
    #user = relationship("User", back_populates="notes")
    #movie = relationship("Movie", back_populates="notes")
    def __init__(self, username, name, note=None):
        """ Create a new User """
        self.username = username
        self.name = name
        self.note = note
