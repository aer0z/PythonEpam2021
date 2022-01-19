from flask import Blueprint
from flask_restful import Api
from . import employee_api
rest = Blueprint('rest', __name__)
api = Api(rest)