"""
Define the REST verbs relative to the notations
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import NotationRepository
from util import parse_params


class NotationResource(Resource):
    """ Verbs relative to the notations """

    @staticmethod
    @swag_from("../swagger/notation/GET.yml")
    def get(username,name):
        """ Return an notation key information based on his name """
        notation = NotationRepository.get(username = username,name=name)
        return jsonify(notation.note)

    @staticmethod
    @parse_params(
        Argument("note", location="json", required=True, help="The note of the notation.")
    	
    )

    @swag_from("../swagger/notation/POST.yml")
    def post( username,name,note):
        """ Create an notation based on the sent information """
        notation = NotationRepository.create(
            username = username ,name = name ,note = note
        )
        return jsonify({"name": notation.name, "username" : notation.username, "note" : notation.note})

    @staticmethod
    @parse_params(
        Argument("note", location="json", required=True, help="The genre of the notation.")
    	
    )
    @swag_from("../swagger/notation/PUT.yml")
    def put(first_name,last_name,name,note):
        """ Update an notation based on the sent information """
        repository = NotationRepository()
        notation = repository.update(first_name = first_name, last_name = last_name, name = name, note = note)
        return jsonify({"notation": notation.json})


