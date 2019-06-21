"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "user"
    username = db.Column(db.String(300), primary_key = True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.relationship('Notation', backref=db.backref('notesu',uselist = False))
    #notes = relationship("Notation", back_populates="user")
    def __init__(self, username, age=None):
        """ Create a new User """
        self.username = username
        self.age = age
