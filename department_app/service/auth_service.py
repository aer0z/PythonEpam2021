"""
CRUD operations for User
"""

from department_app import login_manager, db
from department_app.models.user_model import User


@login_manager.user_loader
def load_user(id):
    """
       Load user from database by id.
       :param id: id of user
       :return: User object
    """
    return User.query.get(int(id))


def new_user(email, pass_hash, first_name):
    """
    Add new user to db
    :param email: user's email
    :param pass_hash: user's hashed password
    :param first_name: user's name
    """
    user = User(email=email, password=pass_hash, first_name=first_name)
    db.session.add(user)
    db.session.commit()


def email_exists(email):
    '''
    Function to check if email exists in db
    :param email: email to check
    :return: If email exist return True else False
    '''
    user = User.query.filter_by(email=email).first()
    return bool(user)
