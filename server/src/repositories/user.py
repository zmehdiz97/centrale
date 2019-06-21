""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(username):
        """ Query a user by last and first name """
        return User.query.filter_by(username = username).one()

    def update(self, username, age):
        """ Update a user's age """
        user = self.get(username)
        user.age = age

        return user.save()

    @staticmethod
    def create(username, age):
        """ Create a new user """
        user = User(username = username, age=age)

        return user.save()
