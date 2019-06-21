"""
Define the REST verbs relative to the movies
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
import json
from repositories import MovieRepository
from util import parse_params


class MovieResource(Resource):
    """ Verbs relative to the movies """

    @staticmethod
    @swag_from("../swagger/movie/GET.yml")
    def get(name):
        """ Return an movie key information based on his name """
        m = MovieRepository.get(name=name)
        d = {}
        d['name'] = m.name
        d['year'] = m.year
        d['genre'] = m.genre
        d['notes'] = 0
        d['affiche'] = m.affiche
        t =[]
        for l in m.notes : 
            t.append(l.note)
        if len(t) != 0 : 
            d['notes'] = sum(t)/len(t)  
        else : 
            d['notes'] = -1
        return(jsonify(d))          

    @staticmethod
    @parse_params(
        Argument("genre", location="json", required=True, help="The genre of the movie."),Argument("year", location="json", required=True,help="The year of the movie."),Argument("affiche", location="json", required=True, help="The affiche of the movie.")
    	
    )

    @swag_from("../swagger/movie/POST.yml")
    def post(name,genre,year,affiche):
        """ Create an movie based on the sent information """
        movie = MovieRepository.create(
            name=name, genre=genre, year=year,affiche = affiche
        )
        return jsonify({"movie": movie.json})

    @staticmethod
    @parse_params(
        Argument("genre", location="json", required=True, help="The genre of the movie."),Argument("year", location="json", required=True,help="The year of the movie."),Argument("affiche", location="json", required=True, help="The affiche of the movie.")
    	
    )
    @swag_from("../swagger/movie/PUT.yml")
    def put(name, genre, year,affiche):
        """ Update an movie based on the sent information """
        repository = MovieRepository()
        movie = repository.update(name=name, genre=genre, year=year,affiche = affiche)
        return jsonify({"movie": movie.json})

class Movie2Resource(Resource):
    """ Verbs relative to the movies """

    @staticmethod
    @swag_from("../swagger/movie/GETALL.yml")
    def get():
        """ Return an movie key information based on his name """
        movie = MovieRepository.getAll()
        result = []
        for m in movie :
            d = {}
            d['name'] = m.name
            d['year'] = m.year
            d['genre'] = m.genre
            d['notes'] = 0
            d['affiche'] = m.affiche
            t =[]
            for l in m.notes : 
                t.append([l.note,l.username])
            c=0
            if len(t) != 0 :
                for i in t:
                    c+=i[0]
                d['notes'] = c/len(t)
            else : 
                d['notes'] = -1
            d['liste notes']=t
            result.append((d))          
        return(jsonify([l for l in result]))             
        #return([l for l in m.notes for m in movie])
#        return ([jsonify(m.json) for m in movie])

    





