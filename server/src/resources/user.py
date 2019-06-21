"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(username):
        """ Return an user key information based on his name """
        m = UserRepository.get(username=username)
        d = {}
        d['username'] = m.username
        d['age'] = m.age
        d['films'] = []
        for l in m.notes : 
            d['films'].append(l.name)
        return(jsonify(d))          


    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/POST.yml")
    def post(username, age):
        """ Create an user based on the sent information """
        user = UserRepository.create(
            username=username, age=age
        )
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the user.")
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(username, age):
        """ Update an user based on the sent information """
        repository = UserRepository()
        user = repository.update(username=username, age=age)
        return jsonify({"user": user.json})
