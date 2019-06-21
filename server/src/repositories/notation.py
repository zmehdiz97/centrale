""" Defines the Notation repository """

from models import Notation
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import inspect
class NotationRepository:
    """ The repository for the notation model """

    @staticmethod
    def get(username, name):
        """ Query a notation by last and first name """
        return Notation.query.filter_by(username = username,name=name).one()

    def update(self, first_name,last_name,name,note):
        """ Update a notation's age """
        notation = self.get(username,name)
        notation.note = note
        return notation.save()

    @staticmethod
    def create(username,name, note):
        """ Create a new notation """
        notation = Notation(username = username, name = name, note = note)
        return notation.save()
    
