"""
Defines the blueprint for the movies
"""
from flask import Blueprint
from flask_restful import Api

from resources import MovieResource
from resources import Movie2Resource
MOVIE_BLUEPRINT = Blueprint("movie", __name__)
Api(MOVIE_BLUEPRINT).add_resource(
    MovieResource, "/movie/<string:name>"
)
Api(MOVIE_BLUEPRINT).add_resource(
    Movie2Resource, "/movie/getall"
)
