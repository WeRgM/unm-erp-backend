from flask_restful import Api, Resource
from .models import User
from . import db


def init_app(app):
    api = Api(app)

    class UserResource():
        pass