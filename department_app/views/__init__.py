"""
Initialize page Blueprint and import all submodules from views.
"""

from flask import Blueprint

page = Blueprint('page', __name__)

from . import auth
from . import views_employee
from . import views_departments
