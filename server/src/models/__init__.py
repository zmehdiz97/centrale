from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
db = SQLAlchemy()

from .user import User
from .movie import Movie
from .notation import Notation
