""" Defines the Movie repository """

from models import Movie


class MovieRepository:
    """ The repository for the movie model """

    @staticmethod
    def get(name):
        """ Query a movie by last and first name """
        return Movie.query.filter_by(name=name).one()

    def update(self, name, genre, year,affiche):
        """ Update a movie's age """
        movie = self.get(name)
        movie.year = year
        movie.genre = genre
        movie.affiche = affiche
        return movie.save()
    def getAll():
        return Movie.query.all()
    @staticmethod
    def create(name, genre, year,affiche):
        """ Create a new movie """
        movie = Movie(name=name, genre=genre, year=year,affiche = affiche)
	
        return movie.save()
